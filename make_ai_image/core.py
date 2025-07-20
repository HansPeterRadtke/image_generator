import sys
import os
import requests
import urllib.parse
import random
import traceback
import hashlib

def make_ai_image(prompt):
  try:
    encoded_prompt = urllib.parse.quote(prompt)
    url            = f"https://pollinations.ai/p/{encoded_prompt}?nologo=true"
    print         (f"Requesting: {url}"                 , flush=True)

    response = requests.get(url, timeout=60, stream=True)
    response.raise_for_status()
    content  = response.content
    digest   = hashlib.md5(content).hexdigest()
    print   (f"Image hash: {digest}"                    , flush=True)

    outname = f"ai_{random.randint(1000,9999)}.jpg"
    outpath = os.path.join("/var/www/html/images", outname)
    with open(outpath, 'wb') as f:
      f.write(content)

    print   (f"Saved: {outpath}"                         , flush=True)
    print   (f"result='{outpath}'"                      , flush=True)
    return outpath

  except requests.RequestException:
    print("Request failed:"                            , flush=True)
    print(traceback.format_exc()                      , flush=True)
  except IOError:
    print("File write error:"                          , flush=True)
    print(traceback.format_exc()                      , flush=True)
  except Exception:
    print("Unexpected error:"                          , flush=True)
    print(traceback.format_exc()                      , flush=True)
  return None