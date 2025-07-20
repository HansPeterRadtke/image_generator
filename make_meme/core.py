import os
import subprocess
import traceback
import re
from PIL import Image


def extract_result(output):
  match = re.search(r"result='([^']+)'", output)
  return match.group(1) if match else None


def overlay_images(base_path, overlay_paths):
  try:
    base = Image.open(base_path).convert("RGBA")
    for path in overlay_paths:
      overlay = Image.open(path).convert("RGBA")
      base.alpha_composite(overlay)

    outname = os.path.join("/var/www/html/images", f"meme_{os.getpid() % 10000}.png")
    base.save(outname)
    print(f"Meme saved to: {outname}"             , flush=True)
    print(f"result='{outname}'"                   , flush=True)
    return outname

  except Exception:
    print("Error overlaying images:"             , flush=True)
    print(traceback.format_exc()                 , flush=True)
    return None


def generate_with_scripts(text, prompt):
  try:
    text_out_raw = subprocess.check_output([
      "python3", "-m", "make_text", text
    ], universal_newlines=True)
    text_path = extract_result(text_out_raw)
    print     (f"Text image path: {text_path}"    , flush=True)

    prompt_out_raw = subprocess.check_output([
      "python3", "-m", "make_ai_image", prompt
    ], universal_newlines=True)
    prompt_path = extract_result(prompt_out_raw)
    print       (f"Prompt image path: {prompt_path}", flush=True)

    return overlay_images(prompt_path, [text_path])

  except Exception:
    print("Error generating image or text:"      , flush=True)
    print(traceback.format_exc()                 , flush=True)
    return None