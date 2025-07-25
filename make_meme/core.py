import os
import traceback
import subprocess
from PIL import Image

def make_meme(
  text: str = "",
  prompt: str = "",
  text_args: list = None,
  image_args: list = None,
  save_dir: str = ".",
  file_prefix: str = "result",
  file_ext: str = ".png"
) -> str:
  print("[DEBUG] make_meme called")
  try:
    text_args = text_args or []
    image_args = image_args or []

    text_output = os.path.join(save_dir, f"{file_prefix}_text{file_ext}")
    text_cmd = [
      "python3", "-m", "make_text",
      "--text", text,
      "--output", text_output
    ] + text_args

    print("[TEXT COMMAND]", ' '.join(text_cmd))
    text_result = subprocess.run(text_cmd, capture_output=True, check=True, text=True)
    print("[TEXT STDOUT]", text_result.stdout)

    if not os.path.isfile(text_output):
      raise RuntimeError(f"Text module did not produce file: {text_output}")

    ai_output = os.path.join(save_dir, f"{file_prefix}_ai{file_ext}")
    image_cmd = [
      "python3", "-m", "make_ai_image",
      "--prompt", prompt,
      "--output", ai_output
    ] + image_args

    print("[IMAGE COMMAND]", ' '.join(image_cmd))
    image_result = subprocess.run(image_cmd, capture_output=True, check=True, text=True)
    print("[IMAGE STDOUT]", image_result.stdout)

    if not os.path.isfile(ai_output):
      raise RuntimeError(f"AI image not generated: {ai_output}")

    final_output = os.path.join(save_dir, f"{file_prefix}_final{file_ext}")

    base = Image.open(ai_output).convert("RGBA")
    overlay = Image.open(text_output).convert("RGBA").resize(base.size)

    composite = Image.alpha_composite(base, overlay)
    composite.convert("RGB").save(final_output)

    return final_output

  except Exception as e:
    print("[EXCEPTION]", str(e))
    print("[TRACEBACK]", traceback.format_exc())
    return None