import subprocess
import os
import sys
import traceback
import argparse

def test_make_meme_cli():
  try:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_folder", type=str, default="")
    args, _ = parser.parse_known_args()

    env = os.environ.copy()
    env['PYTHONPATH'] = f"{os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))}:{env.get('PYTHONPATH', '')}"
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../make_meme/__main__.py'))

    cmd = [
      "python3", script_path,
      "--text", "MEME TEST TEXT",
      "--prompt", "a silly hat on a cat",
      "--text_args=--width 500 --height 300 --rotation 25",
      "--save_dir", "/var/www/html/images",
      "--file_prefix", "test_make_meme_cli",
      "--file_ext", ".png"
    ]
    print("[COMMAND]", ' '.join(cmd))
    result = subprocess.run(cmd, check=True, capture_output=True, text=True, env=env)
    print("[STDOUT]", result.stdout)
    print("[STDERR]", result.stderr)
  except Exception as e:
    print("[EXCEPTION]", str(e))
    print("[TRACEBACK]", traceback.format_exc())

if __name__ == '__main__':
  test_make_meme_cli()