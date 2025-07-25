from make_ai_image.core import make_image

def test_make_ai_image_import():
  result = make_image(
    prompt="import test image",
    width=512,
    height=512,
    output="/var/www/html/images/test_make_ai_image_import.jpg"
  )
  assert result is not None