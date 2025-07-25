from make_meme.core import make_meme

def test_make_meme_import():
  result = make_meme(
    text="MEME TEST TEXT",
    prompt="a silly hat on a cat",
    text_args=["--width", "500", "--height", "300", "--rotation", "25"],
    image_args=[],
    save_dir="/var/www/html/images",
    file_prefix="test_make_meme_import",
    file_ext=".png"
  )
  assert result is not None