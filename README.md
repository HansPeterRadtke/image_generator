# Image Generator Project

This project is a modular image generation toolkit built in Python. It provides the following components:

- `make_ai_image`: Fetches AI-generated images from a remote service.
- `make_text`: Creates text-based transparent overlays.
- `make_meme`: Composes memes by combining AI images and text.
- `generate_images.py`: Randomly generates geometric images.

All modules can be used as command-line tools or as importable Python modules.

---

## Installation

Install dependencies using:

```bash
pip install -r requirements.txt
```

Make sure `Pillow` and `requests` are installed.

---

## 1. generate_images.py
Generates random images with colored rectangles in different formats.

### CLI usage:
```bash
python3 generate_images.py
```
Saves images in JPEG, PNG, and GIF formats to `/var/www/html/images`.

---

## 2. make_ai_image
Fetches an AI-generated image based on a text prompt from `pollinations.ai`.

### CLI usage:
```bash
python3 -m make_ai_image --prompt "a futuristic city" --width 512 --height 512 --output ./output.jpg
```

### Import usage:
```python
from make_ai_image import make_image

make_image(prompt="sunset beach", width=640, height=480, output="ai_image.jpg")
```

### Optional arguments:
- `base_url`: Service base URL
- `save_dir`: Directory to save output
- `file_prefix`, `file_ext`: Naming
- `timeout`: Request timeout
- `add_hash`: Whether to append a hash to filename
- `random_range`: Tuple for random ID suffix

---

## 3. make_text
Creates transparent PNGs with overlay text.

### CLI usage:
```bash
python3 -m make_text --text "Top Meme" --width 500 --height 250 --output ./text.png
```

### Import usage:
```python
from make_text import make_text

make_text(text="Overlay", width=400, height=200, save_path="text_overlay.png")
```

### Optional arguments:
- `rotation`: Rotate text
- `alignment`: Position (center, topleft, bottomright)
- `padding`: Margin
- `color`: Text color
- `font`: Font path

---

## 4. make_meme
Creates a meme by combining an AI-generated image and a text overlay.

### CLI usage:
```bash
python3 -m make_meme --text "Hello" --prompt "sunset city" --save_dir ./output
```

### Import usage:
```python
from make_meme import make_meme

make_meme(text="Caption", prompt="futuristic scene", save_dir="./output")
```

### Notes:
- Internally calls `make_text` and `make_ai_image` via subprocess.
- Output includes `_text`, `_ai`, and `_final` image files.

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

## Output Example
- `result_text.png`: text overlay
- `result_ai.png`: AI-generated image
- `result_final.png`: combined meme

All images default to saving in `/var/www/html/images`, unless overridden.

---

## License
MIT
