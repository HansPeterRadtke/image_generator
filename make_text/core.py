import os
import random
import traceback
from PIL import Image, ImageDraw, ImageFont, ImageColor

def make_text(
  text               ,
  width        = 400 ,
  height       = 200 ,
  fontsize     = 40  ,
  align        = 'center',
  rotation     = 0   ,
  fontcolor    = '#FFFFFF',
  font_path    = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
  save_dir     = "/var/www/html/images" ,
  file_prefix  = "text_" ,
  file_ext     = ".png" ,
  random_range = (1000, 9999)
):
  try:
    img   = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw  = ImageDraw.Draw(img)
    font  = ImageFont.truetype(font_path, fontsize)

    bbox  = draw.textbbox((0, 0), text, font=font)
    w, h  = bbox[2] - bbox[0], bbox[3] - bbox[1]

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

    try:
      rgb = ImageColor.getrgb(fontcolor)
      fillcolor = rgb + (255,)
    except:
      fillcolor = (255, 255, 255, 255)

    draw.text(position, text, font=font, fill=fillcolor)
    img = img.rotate(rotation, expand=True)

    rand_num = random.randint(*random_range)
    filename = f"{file_prefix}{rand_num}{file_ext}"
    outpath  = os.path.join(save_dir, filename)

    os.makedirs(save_dir, exist_ok=True)
    img.save(outpath)
    print(f"Saved: {outpath}"    , flush=True)
    print(f"result='{outpath}'", flush=True)
    return outpath

  except Exception:
    print("Error in make_text:" , flush=True)
    print(traceback.format_exc(), flush=True)
    return None