import sys
import os
import random
import traceback
from PIL import Image, ImageDraw, ImageFont

def main():
  try:
    if len(sys.argv) < 2:
      print("Usage: MakeText.py 'text' [width height fontsize align rotation font]", flush=True)
      sys.exit(1)

    text     = sys.argv[1]
    width    = int(sys.argv[2])  if len(sys.argv) > 2 else 400
    height   = int(sys.argv[3])  if len(sys.argv) > 3 else 200
    fontsize = int(sys.argv[4])  if len(sys.argv) > 4 else 40
    align    = sys.argv[5]       if len(sys.argv) > 5 else 'center'
    rotation = int(sys.argv[6])  if len(sys.argv) > 6 else 0
    fontname = sys.argv[7]       if len(sys.argv) > 7 else '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

    img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(fontname, fontsize)
    bbox = draw.textbbox((0, 0), text, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]

    if align == 'center':
      position = ((width - w) // 2, (height - h) // 2)
    elif align == 'topleft':
      position = (0, 0)
    elif align == 'topright':
      position = (width - w, 0)
    elif align == 'bottomleft':
      position = (0, height - h)
    elif align == 'bottomright':
      position = (width - w, height - h)
    else:
      position = ((width - w) // 2, (height - h) // 2)

    draw.text(position, text, font=font, fill=(255, 255, 255, 255))
    img = img.rotate(rotation, expand=True)

    outname = f"text_{random.randint(1000,9999)}.png"
    outpath = os.path.join("/var/www/html/images", outname)
    img.save(outpath)
    print(f"Saved: {outpath}", flush=True)
    print(f"result='{outpath}'", flush=True)

  except Exception:
    print("Error in MakeText:", flush=True)
    print(traceback.format_exc(), flush=True)

if __name__ == '__main__':
  main()
