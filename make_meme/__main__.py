import argparse
import traceback
from make_meme.core import make_meme

def parse_args():
  parser = argparse.ArgumentParser(description="Make Meme CLI")
  parser.add_argument("--text", type=str, default="")
  parser.add_argument("--prompt", type=str, default="")
  parser.add_argument("--text_args", type=str, default="")
  parser.add_argument("--image_args", type=str, default="")
  parser.add_argument("--save_dir", type=str, default=".")
  parser.add_argument("--file_prefix", type=str, default="result_")
  parser.add_argument("--file_ext", type=str, default=".png")
  return parser.parse_args()

def main():
  print("[DEBUG] CLI main called")
  try:
    args = parse_args()
    text_args = args.text_args.split() if args.text_args else []
    image_args = args.image_args.split() if args.image_args else []

    result = make_meme(
      text=args.text,
      prompt=args.prompt,
      text_args=text_args,
      image_args=image_args,
      save_dir=args.save_dir,
      file_prefix=args.file_prefix,
      file_ext=args.file_ext
    )
    if result:
      print(f"result='{result}'")
  except Exception as e:
    print("[EXCEPTION]", str(e))
    print("[TRACEBACK]", traceback.format_exc())

if __name__ == '__main__':
  main()