import argparse
import traceback
from make_ai_image.core import make_image

def parse_args():
  parser = argparse.ArgumentParser(description="AI Image Generator")
  parser.add_argument("--prompt", type=str, default="")
  parser.add_argument("--width", type=int, default=512)
  parser.add_argument("--height", type=int, default=512)
  parser.add_argument("--output", type=str, default="output.jpg")
  return parser.parse_args()

def main():
  print("[DEBUG] CLI main called")
  try:
    args = parse_args()
    result = make_image(
      prompt=args.prompt,
      width=args.width,
      height=args.height,
      output=args.output
    )
    if result:
      print(f"result='{result}'")
  except Exception as e:
    print("[EXCEPTION]", str(e))
    print("[TRACEBACK]", traceback.format_exc())

if __name__ == '__main__':
  main()