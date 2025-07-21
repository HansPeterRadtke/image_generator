import os
import subprocess
import traceback
import re
from PIL import Image

def extract_result(output):
  match = re.search(r"result='([^']+)'", output)
  return match.group(1) if match else None

def overlay_images(
  base_path     ,
  overlay_paths ,
  save_dir      = "/var/www/html/images",
  file_prefix   = "meme_"                 ,
  file_ext      = ".png"
):
  try:
    base = Image.open(base_path).convert("RGBA")
    for path in overlay_paths:
      overlay = Image.open(path).convert("RGBA")
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

def generate_with_scripts(
  text                     ,
  prompt                  ,
  text_args     = None    ,
  image_args    = None    ,
  save_dir      = "/var/www/html/images",
  file_prefix   = "meme_"                 ,
  file_ext      = ".png"
):
  try:
    text_args     = text_args or []
    image_args    = image_args or []

    text_out_raw  = subprocess.check_output(
      ["python3", "-m", "make_text", text, *text_args],
      universal_newlines=True
    )
    text_path     = extract_result(text_out_raw)
    print        (f"Text image path: {text_path}"     , flush=True)

    prompt_out_raw= subprocess.check_output(
      ["python3", "-m", "make_ai_image", prompt, *image_args],
      universal_newlines=True
    )
    prompt_path   = extract_result(prompt_out_raw)
    print        (f"Prompt image path: {prompt_path}" , flush=True)

    return overlay_images(
      prompt_path,
      [text_path],
      save_dir=save_dir,
      file_prefix=file_prefix,
      file_ext=file_ext
    )

  except Exception:
    print("Error generating image or text:"      , flush=True)
    print(traceback.format_exc()                 , flush=True)
    return None