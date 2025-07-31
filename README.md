# Image Generator Project

This modular toolkit generates and composes images through AI, text overlays, and basic shapes. Each module works both via CLI and as a Python import.

---

## Installation

You must have:
- `Pillow`
- `requests`

To install dependencies:
```bash
pip install pillow requests
```

---

## 1. generate_images.py

Generates geometric images with random rectangles and colors.

### CLI Usage:
```bash
python3 generate_images.py
```

**Output:** Saves JPEG, PNG, and GIF images to `/var/www/html/images`

**Parameters:** None.

---

## 2. make_ai_image

Fetches an AI-generated image using `pollinations.ai` and saves it locally.

### CLI Usage:
```bash
python3 -m make_ai_image --prompt "a futuristic city" --width 512 --height 512 --output ./output.jpg
```

**Parameters:**
- `--prompt` (str, required): text prompt to generate the image.
- `--width` (int, default=512): image width in pixels.
- `--height` (int, default=512): image height in pixels.
- `--output` (str, default="output.jpg"): path to save the image.

### Python Import Usage:
```python
from make_ai_image import make_image

make_image(
  prompt        = "sunset beach",
  width         = 640,
  height        = 480,
  output        = "ai_image.jpg",
  base_url      = "https://pollinations.ai/p/",
  save_dir      = "/var/www/html/images",
  file_prefix   = "ai_",
  file_ext      = ".jpg",
  timeout       = 60,
  add_hash      = True,
  random_range  = (1000, 9999)
)
```

---

## 3. make_text

Creates a transparent PNG image with overlayed text.

### CLI Usage:
```bash
python3 -m make_text --text "Top Meme" --width 500 --height 250 --output ./text.png
```

**Parameters:**
- `--text` (str, required): the text content.
- `--width` (int, default=512): image width in pixels.
- `--height` (int, default=512): image height in pixels.
- `--rotation` (int, default=0): rotation angle in degrees.
- `--align` (str, default="center"): text alignment.
- `--padding` (int, default=10): padding in pixels.
- `--color` (str, default="#000000"): hex color code.
- `--font` (str, optional): path to a TTF font file.
- `--output` (str, required): path to save the PNG.

### Python Import Usage:
```python
from make_text import make_text

make_text(
  text       = "Overlay Text",
  width      = 400,
  height     = 200,
  rotation   = 15,
  align      = "topright",
  padding    = 20,
  fontcolor  = "#FF00FF",
  font       = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
  save_path  = "/var/www/html/images/text.png"
)
```

---

## 4. make_meme

Combines AI image and text overlay into a single meme image.

### CLI Usage:
```bash
python3 -m make_meme \
  --text "Hello" \
  --prompt "sunset city" \
  --save_dir ./output \
  --text_args "--width 500 --height 250" \
  --file_prefix meme \
  --file_ext .jpg
```

**Parameters:**
- `--text` (str, required): text to render.
- `--prompt` (str, required): prompt for the AI image.
- `--text_args` (str, optional): quoted string of CLI args for make_text.
- `--image_args` (str, optional): quoted string of CLI args for make_ai_image.
- `--save_dir` (str, default="."): directory to save all images.
- `--file_prefix` (str, default="result_"): prefix for all outputs.
- `--file_ext` (str, default=".png"): file extension for all outputs.

### Python Import Usage:
```python
from make_meme import make_meme

make_meme(
  text        = "Caption here",
  prompt      = "futuristic architecture",
  text_args   = ["--width", "500"],
  image_args  = ["--width", "400", "--height", "400"],
  save_dir    = "./output",
  file_prefix = "demo",
  file_ext    = ".jpg"
)
```

**Output files:**
- `<prefix>_text.<ext>`
- `<prefix>_ai.<ext>`
- `<prefix>_final.<ext>`

---

## Project Structure
```
image_generator/
├── generate_images.py
├── make_ai_image/
│   ├── core.py
│   ├── __init__.py
│   └── __main__.py
├── make_text/
│   ├── core.py
│   ├── __init__.py
│   └── __main__.py
├── make_meme/
│   ├── core.py
│   ├── __init__.py
│   └── __main__.py
├── test/
│   ├── test_make_*.py
├── setup.py
```

---

## License
MIT