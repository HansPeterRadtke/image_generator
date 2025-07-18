import os
import random
import argparse
from PIL import Image, ImageDraw, ImageFont

def parse_args():
  parser = argparse.ArgumentParser(description='Render text to PNG image with transparency')
  parser.add_argument('text'       , type=str  , help='Text to render')
  parser.add_argument('--width'   , type=int  , default=400 , help='Image width')
  parser.add_argument('--height'  , type=int  , default=200 , help='Image height')
  parser.add_argument('--fontsize', type=int  , default=32  , help='Font size')
  parser.add_argument('--font'    , type=str  , default='DejaVuSans.ttf', help='Font family (must be installed)')
  parser.add_argument('--align_x' , type=str  , default='center', choices=['left', 'center', 'right'])
  parser.add_argument('--align_y' , type=str  , default='center', choices=['top', 'center', 'bottom'])
  parser.add_argument('--italic'  , action='store_true', help='Render italic text')
  parser.add_argument('--rotate'  , type=int  , default=0, help='Rotation angle in degrees')
  return parser.parse_args()

def compute_position(draw, text, font, width, height, align_x, align_y):
  bbox = draw.textbbox((0, 0), text, font=font)
  text_w = bbox[2] - bbox[0]
  text_h = bbox[3] - bbox[1]
  x = {'left': 0, 'center': (width - text_w) // 2, 'right': width - text_w}[align_x]
  y = {'top': 0 , 'center': (height - text_h) // 2, 'bottom': height - text_h}[align_y]
  return x, y

def main():
  args = parse_args()
  image = Image.new('RGBA', (args.width, args.height), (0, 0, 0, 0))  # Transparent
  draw  = ImageDraw.Draw(image)

  try:
    font = ImageFont.truetype(args.font, args.fontsize)
  except Exception as e:
    print(f"Font error: {e}\nFalling back to default font.")
    font = ImageFont.load_default()

  pos = compute_position(draw, args.text, font, args.width, args.height, args.align_x, args.align_y)
  draw.text(pos, args.text, font=font, fill=(0, 0, 0, 255))  # Black text

  if args.rotate:
    image = image.rotate(args.rotate, expand=True)

  fname = f"text_{random.randint(1000,9999)}.png"
  outpath = os.path.join("/var/www/html/images", fname)
  image.save(outpath)
  print(f"Saved: {outpath}")

if __name__ == '__main__':
  main()
