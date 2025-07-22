import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from make_ai_image.core import make_ai_image

def test_make_ai_image_module_all_params():
  path = make_ai_image(
    prompt="sunrise over mountain lake",
    base_url="https://pollinations.ai/p/",
    save_dir="/var/www/html/images",
    file_prefix="testmod_ai_",
    file_ext=".jpg",
    timeout=60,
    add_hash=True,
    random_range=(1000, 9999)
  )
  assert path is not None
  assert os.path.isfile(path)
  assert os.path.getsize(path) > 0