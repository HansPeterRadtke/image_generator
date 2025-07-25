from make_text.core import make_text

def test_make_text_import():
  result = make_text(
    text="IMPORT TEST TEXT",
    width=400,
    height=200,
    rotation=15,
    align="topright",
    padding=20,
    fontcolor="#FF00FF",
    font="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    save_path="/var/www/html/images/test_make_text_import.png"
  )
  assert result is not None