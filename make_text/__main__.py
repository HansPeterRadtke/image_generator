import os, sys, traceback
print("[DEBUG __main__] sys.argv:", sys.argv)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from core import parse_args_grouped, make_text

if __name__ == "__main__":
  try:
    args = parse_args_grouped()
    result_image = make_text(
      args.text,
      args.width,
      args.height,
      args.font_size,
      args.position,
      args.outline,
      args.color,
      args.save_path
    )
    if result_image is None:
      print("[ERROR] make_text returned None", flush=True)
    else:
      print("result='" + result_image + "'", flush=True)
  except Exception as e:
    print("[EXCEPTION in make_text __main__]", flush=True)
    print(traceback.format_exc(), flush=True)