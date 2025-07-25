import argparse
from make_text.core import make_text
import traceback

if __name__ == '__main__':
  print("[make_text.__main__] CLI started")
  try:
    parser = argparse.ArgumentParser()
    parser.add_argument('--text'     , default="Hello World")
    parser.add_argument('--width'    , type=int, default=400)
    parser.add_argument('--height'   , type=int, default=200)
    parser.add_argument('--rotation' , type=int, default=0)
    parser.add_argument('--alignment', default="center")
    parser.add_argument('--padding'  , type=int, default=10)
    parser.add_argument('--color'    , default="#000000")
    parser.add_argument('--font'     , default="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    parser.add_argument('--output'   , default="output.png")
    args = parser.parse_args()

    print("[make_text.__main__] Parsed args:", vars(args))

    result = make_text(
      text      = args.text,
      width     = args.width,
      height    = args.height,
      rotation  = args.rotation,
      align     = args.alignment,
      padding   = args.padding,
      font      = args.font,
      fontcolor = args.color,
      save_path = args.output
    )
    if result:
      print(f"result='{result}'")
    else:
      print("[make_text.__main__] No result generated")
  except Exception as e:
    print("[make_text.__main__] EXCEPTION:", str(e))
    print(traceback.format_exc())