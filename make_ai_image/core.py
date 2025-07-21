import os
import requests
import urllib.parse
import random
import traceback
import hashlib

def make_ai_image(
  prompt              ,
  base_url      = "https://pollinations.ai/p/",
  save_dir      = "/var/www/html/images"      ,
  file_prefix   = "ai_"                        ,
  file_ext      = ".jpg"                      ,
  timeout       = 60                           ,
  add_hash      = True                         ,
  random_range  = (1000, 9999)
):
  try:
    encoded_prompt = urllib.parse.quote(prompt)
    url            = f"{base_url}{encoded_prompt}?nologo=true"
    print         (f"Requesting: {url}"                                     , flush=True)

    response = requests.get(url, timeout=timeout, stream=True)
    response.raise_for_status()
    content  = response.content

    digest   = hashlib.md5(content).hexdigest()
    print   (f"Image hash: {digest}"                                      , flush=True)

    rand_num = random.randint(*random_range)
    hash_tag = f"_{digest[:8]}" if add_hash else ""
    filename = f"{file_prefix}{rand_num}{hash_tag}{file_ext}"
    outpath  = os.path.join(save_dir, filename)

    os.makedirs(save_dir, exist_ok=True)
    with open(outpath, 'wb') as f:
      f.write(content)

    print   (f"Saved: {outpath}"                                         , flush=True)
    print   (f"result='{outpath}'"                                      , flush=True)
    return outpath

  except requests.RequestException:
    print("Request failed:"                                            , flush=True)
    print(traceback.format_exc()                                      , flush=True)
  except IOError:
    print("File write error:"                                          , flush=True)
    print(traceback.format_exc()                                      , flush=True)
  except Exception:
    print("Unexpected error:"                                          , flush=True)
    print(traceback.format_exc()                                      , flush=True)
  return None