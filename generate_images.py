import os
import random
from PIL import Image, ImageDraw

def create_random_image(width, height, color):
  img    = Image.new("RGB", (width, height), color)
  draw   = ImageDraw.Draw(img)
  for _ in range(10):
    x0 = random.randint(0, width)
    y0 = random.randint(0, height)
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    shape = [(min(x0, x1), min(y0, y1)), (max(x0, x1), max(y0, y1))]
    draw.rectangle(shape, fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
  return img

def save_images(output_path):
  os.makedirs(output_path, exist_ok=True)
  formats = ['JPEG', 'PNG', 'GIF']
  for i in range(1, 4):
    w = random.randint(200, 800)
    h = random.randint(200, 800)
    img = create_random_image(w, h, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    for fmt in formats:
      ext = fmt.lower() if fmt != 'JPEG' else 'jpg'
      filename = os.path.join(output_path, f"{i:04d}.{ext}")
      img.save(filename, fmt)
      print(f"Saved {filename}")

if __name__ == '__main__':
  save_images("/var/www/html/images")
