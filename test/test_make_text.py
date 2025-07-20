import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from make_text import make_text

def test_make_text():
  path = make_text("Test", 400, 200, 30, "center", 0, "#00FF00")
  assert path is not None, "make_text returned None"
  assert os.path.exists(path), f"Output file does not exist: {path}"
  assert path.endswith(".png"), f"Unexpected file format: {path}"