import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from make_meme.core import generate_with_scripts

def test_make_meme_module_all_params():
  result_path = generate_with_scripts(
    text="Test Meme Module",
    prompt="sunrise over mountain lake",
    text_args=["600", "300", "60", "bottomleft", "5", "#FF00FF"],
    image_args=[],
    save_dir="/var/www/html/images",
    file_prefix="testmod_meme_",
    file_ext=".png"
  )
  assert result_path is not None
  assert os.path.isfile(result_path)
  assert os.path.getsize(result_path) > 0