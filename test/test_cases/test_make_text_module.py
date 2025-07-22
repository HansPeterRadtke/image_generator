import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from make_text.core import make_text

def test_make_text_module_all_params():
  path = make_text(
    text="CLI Test Text",
    width=500,
    height=300,
    fontsize=50,
    align="bottomright",
    rotation=15,
    fontcolor="#00FF00",
    save_dir="/var/www/html/images",
    file_prefix="testmod_",
    file_ext=".png"
  )
  assert path is not None
  assert os.path.isfile(path)
  assert os.path.getsize(path) > 0