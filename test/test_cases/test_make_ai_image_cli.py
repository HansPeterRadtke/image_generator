import os
import sys
import subprocess
import re

print("[TEST] Current directory:", os.getcwd())

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def extract_result(output):
  match = re.search(r"result='([^']+)'", output)
  return match.group(1) if match else None

def test_make_ai_image_cli():
  subprocess.run(["python3", "-c", "import os; print('[SUBPROCESS] Current directory:', os.getcwd())"])
  cmd    = ["python3", "-m", "make_ai_image", "sunrise over mountain lake", "/var/www/html/images/test_ai.jpg"]
  result = subprocess.check_output(cmd, universal_newlines=True)
  path   = extract_result(result)
  assert path is not None
  assert os.path.isfile(path)
  assert os.path.getsize(path) > 0