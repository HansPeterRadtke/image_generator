import os
import sys
import subprocess
from PIL import Image
import traceback
import re

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
    print(f"Meme saved to: {outname}", flush=True)
  except Exception:
    print("Error overlaying images:", flush=True)
    print(traceback.format_exc(), flush=True)

def generate_with_scripts(text, prompt):
  try:
    text_out_raw = subprocess.check_output([
      "python3", "/home/hans/dev/GPT/github/image_generator/MakeText.py", text
    ], universal_newlines=True)
    text_path = extract_result(text_out_raw)
    print(f"Text image path: {text_path}", flush=True)

    prompt_out_raw = subprocess.check_output([
      "python3", "/home/hans/dev/GPT/github/image_generator/CreateAIImage.py", prompt
    ], universal_newlines=True)
    prompt_path = extract_result(prompt_out_raw)
    print(f"Prompt image path: {prompt_path}", flush=True)

    overlay_images(prompt_path, [text_path])
  except Exception:
    print("Error generating image or text:", flush=True)
    print(traceback.format_exc(), flush=True)

def main():
  if '--text' in sys.argv and '--prompt' in sys.argv:
    try:
      text_idx = sys.argv.index('--text') + 1
      prompt_idx = sys.argv.index('--prompt') + 1
      text = sys.argv[text_idx]
      prompt = sys.argv[prompt_idx]
      generate_with_scripts(text, prompt)
    except Exception:
      print("Error parsing arguments", flush=True)
      print(traceback.format_exc(), flush=True)
  elif len(sys.argv) > 2:
    background = sys.argv[1]
    overlays = sys.argv[2:]
    overlay_images(background, overlays)
  else:
    print("Usage: Meme.py <background> <overlay1> <overlay2> ...", flush=True)
    print("   or: Meme.py --text 'Hello' --prompt 'a cat in space'", flush=True)

if __name__ == '__main__':
  main()
