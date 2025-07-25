import os
import requests
import urllib.parse
import random
import traceback
import hashlib
import argparse

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("prompt"          , type=str)
  parser.add_argument("save_path"       , type=str)
  parser.add_argument("--base_url"      , type=str, default="https://pollinations.ai/p/")
  parser.add_argument("--save_dir"      , type=str, default="/var/www/html/images")
  parser.add_argument("--file_prefix"   , type=str, default="ai_")
  parser.add_argument("--file_ext"      , type=str, default=".jpg")
  parser.add_argument("--timeout"       , type=int, default=60)
  parser.add_argument("--add_hash"      , action='store_true')
  parser.add_argument("--rand_min"      , type=int, default=1000)
  parser.add_argument("--rand_max"      , type=int, default=9999)
  return parser.parse_args()

def make_image(prompt,
               width        = 512,
               height       = 512,
               output       = None,
               base_url     = "https://pollinations.ai/p/",
               save_dir     = "/var/www/html/images",
               file_prefix  = "ai_",
               file_ext     = ".jpg",
               timeout      = 60,
               add_hash     = True,
               random_range = (1000, 9999)):
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

    outpath = output or os.path.join(save_dir, filename)

    os.makedirs(os.path.dirname(outpath) or '.', exist_ok=True)
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