import os
import random
import traceback
from PIL import Image, ImageDraw, ImageFont, ImageColor

def make_text(*args):
  try:
    text     = args[0]
    width    = int(args[1]) if len(args) > 1 else 400
    height   = int(args[2]) if len(args) > 2 else 200
    fontsize = int(args[3]) if len(args) > 3 else 40
    align    = args[4]       if len(args) > 4 else 'center'
    rotation = int(args[5])  if len(args) > 5 else 0
    fontcolor = args[6]      if len(args) > 6 else None

    img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", fontsize)
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

    fillcolor = (255, 255, 255, 255)
    if fontcolor:
      try:
        rgb = ImageColor.getrgb(fontcolor)
        fillcolor = rgb + (255,)
      except:
        pass

    draw.text(position, text, font=font, fill=fillcolor)
    img = img.rotate(rotation, expand=True)

    outname = f"text_{random.randint(1000,9999)}.png"
    outpath = os.path.join("/var/www/html/images", outname)
    img.save(outpath)
    print(f"Saved: {outpath}", flush=True)
    print(f"result='{outpath}'", flush=True)
    return outpath

  except Exception:
    print("Error in make_text:", flush=True)
    print(traceback.format_exc(), flush=True)
    return None
