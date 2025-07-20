import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from make_ai_image import make_ai_image

def test_make_ai_image():
  path = make_ai_image("a blue sunset over the mountains")
  assert path is not None, "make_ai_image returned None"
  assert os.path.exists(path), f"Output file does not exist: {path}"
  assert path.endswith(".jpg"), f"Unexpected file format: {path}"