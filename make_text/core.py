import os
from PIL import Image, ImageDraw, ImageFont
import traceback

def make_text(text, width=400, height=200, fontsize=20, align="center", rotation=0,
              fontcolor="#000000", padding=10,
              font="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              save_path="output.png"):
  try:
    print("[make_text] Starting with params:", locals())
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    try:
      font_obj = ImageFont.truetype(font, fontsize)
    except Exception as fe:
      print("[make_text] Font load error:", str(fe))
      font_obj = ImageFont.load_default()

    text_bbox = draw.textbbox((0, 0), text, font=font_obj)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    if align == "center":
      position = ((width - text_width) // 2, (height - text_height) // 2)
    elif align == "topleft":
      position = (padding, padding)
    elif align == "bottomright":
      position = (width - text_width - padding, height - text_height - padding)
    else:
      position = (padding, padding)

    temp_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
    temp_draw = ImageDraw.Draw(temp_img)
    temp_draw.text(position, text, font=font_obj, fill=fontcolor)

    rotated = temp_img.rotate(rotation, expand=1)
    final_img = Image.new("RGBA", rotated.size, (0, 0, 0, 0))
    final_img.paste(rotated, (0, 0), rotated)

    dirpath = os.path.dirname(save_path)
    if dirpath:
      os.makedirs(dirpath, exist_ok=True)
    final_img.save(save_path)
    print("[make_text] Image saved to", save_path)
    return save_path
  except Exception as e:
    print("[make_text] Error:", str(e))
    print(traceback.format_exc())
    return None