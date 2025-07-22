import subprocess
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def test_make_text_cli_all_params():
  subprocess.run(["python3", "-c", "import os; print('[SUBPROCESS] Current directory:', os.getcwd())"])
  cmd    = [
    "python3", "-m", "make_text",
    "CLI Boom Text", "500", "300", "50", "bottomright", "15", "#00FF00", "result_test_text.png"
  ]
  result = subprocess.check_output(cmd, universal_newlines=True)
  print("[TEST OUTPUT]", result)