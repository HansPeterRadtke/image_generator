import os, sys, traceback
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from core import parse_args, make_ai_image

if __name__ == "__main__":
  try:
    args = parse_args()
    result_image = make_ai_image(prompt=args.prompt, save_path=args.save_path)
    if result_image is None:
      print("[ERROR] make_ai_image returned None", flush=True)
    else:
      print("result='" + result_image + "'", flush=True)
  except Exception as e:
    print("[EXCEPTION in make_ai_image __main__]", flush=True)
    print(traceback.format_exc(), flush=True)