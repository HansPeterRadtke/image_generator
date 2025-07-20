import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from make_meme import generate_with_scripts

def test_generate_with_scripts():
  path = generate_with_scripts("Boom!", "a cartoon explosion")
  assert path is not None, "generate_with_scripts returned None"
  assert os.path.exists(path), f"Output file does not exist: {path}"
  assert path.endswith(".png"), f"Unexpected file format: {path}"