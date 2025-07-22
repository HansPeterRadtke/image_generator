import os
import subprocess
import traceback
import re
import argparse
from PIL import Image, ImageStat
import math

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--text"       , type=str, required=True)
  parser.add_argument("--prompt"     , type=str, required=True)
  parser.add_argument("--text_args"  , nargs='*', default=[])
  parser.add_argument("--image_args" , nargs='*', default=[])
  parser.add_argument("--save_dir"   , type=str, default="/var/www/html/images")
  parser.add_argument("--file_prefix", type=str, default="meme_")
  parser.add_argument("--file_ext"   , type=str, default=".png")
  return parser.parse_args()

def parse_args_grouped():
  parser = argparse.ArgumentParser(exit_on_error=False)
  parser.add_argument("--text"       , type=str, required=True)
  parser.add_argument("--prompt"     , type=str, required=True)
  parser.add_argument("width"        , type=int)
  parser.add_argument("height"       , type=int)
  parser.add_argument("font_size"    , type=int)
  parser.add_argument("position"     , type=str)
  parser.add_argument("outline"      , type=int)
  parser.add_argument("color"        , type=str)
  parser.add_argument("save_path"    , type=str)
  parser.add_argument("--image_args" , nargs=2 , required=True)
  parser.add_argument("--file_prefix", type=str, default="meme_")
  return parser.parse_args()

def generate_with_scripts(text, prompt, text_args=None, image_args=None, save_dir="/var/www/html/images", file_prefix="meme_", file_ext=".png"):
  try:
    text_args  = [str(x) for x in (text_args or [])]
    image_args = [str(x) for x in (image_args or [])]

    cmd_text = ["python3", "-m", "make_text", text] + text_args
    print("[DEBUG] CMD make_text:", cmd_text, flush=True)
    try:
      text_out_raw = subprocess.check_output(cmd_text, universal_newlines=True)
      print("[DEBUG] OUTPUT make_text:", text_out_raw, flush=True)
      text_path = extract_result(text_out_raw)
      if text_path is None:
        print("[ERROR] Failed to extract text result", flush=True)
        return None
    except Exception:
      print("[EXCEPTION] make_text subprocess failed:", flush=True)
      print(traceback.format_exc(), flush=True)
      return None

    cmd_image = ["python3", "-m", "make_ai_image", prompt] + image_args
    print("[DEBUG] CMD make_ai_image:", cmd_image, flush=True)
    try:
      prompt_out_raw = subprocess.check_output(cmd_image, universal_newlines=True)
      print("[DEBUG] OUTPUT make_ai_image:", prompt_out_raw, flush=True)
      prompt_path = extract_result(prompt_out_raw)
      if prompt_path is None:
        print("[ERROR] Failed to extract prompt result", flush=True)
        return None
    except Exception:
      print("[EXCEPTION] make_ai_image subprocess failed:", flush=True)
      print(traceback.format_exc(), flush=True)
      return None

    return overlay_images(prompt_path, [text_path], save_dir=save_dir, file_prefix=file_prefix, file_ext=file_ext)

  except Exception:
    print("Error generating image or text:", flush=True)
    print(traceback.format_exc(), flush=True)
    return None

def extract_result(output):
  match = re.search(r"result='([^']+)'", output)
  return match.group(1) if match else None

def analyze_contrast(base, overlay):
  try:
    mask = overlay.split()[-1]  # alpha channel
    bounds = mask.getbbox()
    if not bounds:
      print("Overlay has no visible content", flush=True)
      return
    cropped_base = base.crop(bounds).convert("RGB")
    stat = ImageStat.Stat(cropped_base)
    r, g, b = stat.mean
    luminance_bg = 0.2126 * r + 0.7152 * g + 0.0722 * b

    overlay_rgb = overlay.convert("RGB")
    stat_overlay = ImageStat.Stat(overlay_rgb, mask)
    r2, g2, b2 = stat_overlay.mean
    luminance_fg = 0.2126 * r2 + 0.7152 * g2 + 0.0722 * b2

    L1, L2 = max(luminance_fg, luminance_bg), min(luminance_fg, luminance_bg)
    contrast_ratio = (L1 + 0.05) / (L2 + 0.05)
    print(f"Contrast ratio (WCAG): {contrast_ratio:.2f}" , flush=True)
    if contrast_ratio < 4.5:
      print("WARNING: Low contrast between text and background!", flush=True)
  except Exception:
    print("Error analyzing contrast:"                       , flush=True)
    print(traceback.format_exc()                          , flush=True)

def overlay_images(base_path, overlay_paths, save_dir="/var/www/html/images", file_prefix="meme_", file_ext=".png"):
  try:
    base = Image.open(base_path).convert("RGBA")
    for path in overlay_paths:
      overlay = Image.open(path).convert("RGBA")
      analyze_contrast(base, overlay)
      base.alpha_composite(overlay)

    filename = f"{file_prefix}{os.getpid() % 10000}{file_ext}"
    outpath  = os.path.join(save_dir, filename)
    os.makedirs(save_dir, exist_ok=True)
    base.save(outpath)

    print(f"Meme saved to: {outpath}"  , flush=True)
    print(f"result='{outpath}'"        , flush=True)
    return outpath

  except Exception:
    print("Error overlaying images:"  , flush=True)
    print(traceback.format_exc()    , flush=True)
    return None