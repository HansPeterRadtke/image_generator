import subprocess
import os
import sys
import traceback
import argparse

def test_make_ai_image_cli():
  try:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_folder", type=str, default="")
    args, _ = parser.parse_known_args()

    env = os.environ.copy()
    env['PYTHONPATH'] = f"{os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))}:{env.get('PYTHONPATH', '')}"
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../make_ai_image/__main__.py'))

    cmd = [
      "python3", script_path,
      "--prompt", "CLI test AI image",
      "--width", "400",
      "--height", "400",
      "--output", "/var/www/html/images/test_make_ai_image_cli.jpg"
    ]
    print("[COMMAND]", ' '.join(cmd))
    result = subprocess.run(cmd, check=True, capture_output=True, text=True, env=env)
    print("[STDOUT]", result.stdout)
    print("[STDERR]", result.stderr)
  except Exception as e:
    print("[EXCEPTION]", str(e))
    print("[TRACEBACK]", traceback.format_exc())

if __name__ == '__main__':
  test_make_ai_image_cli()