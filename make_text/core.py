import os
import random
import traceback
import argparse
from PIL import Image, ImageDraw, ImageFont, ImageColor

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("text"      , type=str)
  parser.add_argument("width"     , type=int)
  parser.add_argument("height"    , type=int)
  parser.add_argument("font_size", type=int)
  parser.add_argument("position" , type=str)
  parser.add_argument("outline"   , type=int)
  parser.add_argument("color"     , type=str)
  parser.add_argument("save_path", type=str)
  return parser.parse_args()

def parse_args_grouped():
  parser = argparse.ArgumentParser()
  parser.add_argument("text"      , type=str)
  parser.add_argument("width"     , type=int)
  parser.add_argument("height"    , type=int)
  parser.add_argument("font_size", type=int)
  parser.add_argument("position" , type=str)
  parser.add_argument("outline"   , type=int)
  parser.add_argument("color"     , type=str)
  parser.add_argument("save_path", type=str)
  return parser.parse_args()

def make_text(
  text,
  width,
  height,
  font_size,
  position,
  outline,
  color,
  save_path
):
  try:
    print("[DEBUG make_text] text=", text)
    print("[DEBUG make_text] width=", width, "height=", height)
    print("[DEBUG make_text] font_size=", font_size, "position=", position)
    print("[DEBUG make_text] outline=", outline, "color=", color)
    print("[DEBUG make_text] save_path=", save_path)

    img   = Image.new("RGBA", (int(width), int(height)), (255, 255, 255, 0))
    draw  = ImageDraw.Draw(img)
    font  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(font_size))

    bbox  = draw.textbbox((0, 0), text, font=font)
    w, h  = bbox[2] - bbox[0], bbox[3] - bbox[1]

    if position == 'center':
      pos = ((int(width) - w) // 2, (int(height) - h) // 2)
    elif position == 'topleft':
      pos = (0, 0)
    elif position == 'topright':
      pos = (int(width) - w, 0)
    elif position == 'bottomleft':
      pos = (0, int(height) - h)
    elif position == 'bottomright':
      pos = (int(width) - w, int(height) - h)
    else:
      pos = ((int(width) - w) // 2, (int(height) - h) // 2)

    try:
      rgb = ImageColor.getrgb(color)
      fillcolor = rgb + (255,)
    except:
      fillcolor = (255, 255, 255, 255)

    draw.text(pos, text, font=font, fill=fillcolor)
    img = img.rotate(int(outline), expand=True)

    directory = os.path.dirname(save_path)
    if directory:
      os.makedirs(directory, exist_ok=True)
    img.save(save_path)
    print(f"Saved: {save_path}"    , flush=True)
    print(f"result='{save_path}'", flush=True)
    return save_path

  except Exception:
    print("Error in make_text:" , flush=True)
    print(traceback.format_exc(), flush=True)
    return None