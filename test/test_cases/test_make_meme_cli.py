import os
import sys
import subprocess
import re

print("[TEST] Current directory:", os.getcwd())

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def extract_result(output):
  match = re.search(r"result='([^']+)'", output)
  return match.group(1) if match else None

def test_make_meme_cli():
  subprocess.run(["python3", "-c", "import os; print('[SUBPROCESS] Current directory:', os.getcwd())"])
  save_path = "result_test.png"
  cmd = [
    "python3", "-m", "make_meme",
    "--text", "CLI Meme Test",
    "--prompt", "sunrise over mountain lake",
    "--text_args", "500", "300", "50", "bottomright", "15", "#00FF00", save_path,
    "--image_args", "500", "300",
    "--file_prefix", "test_meme"
  ]
  result = subprocess.check_output(cmd, universal_newlines=True)
  path = extract_result(result)
  assert path is not None
  assert os.path.isfile(path)
  assert os.path.getsize(path) > 0