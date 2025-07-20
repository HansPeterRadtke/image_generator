import sys
from .core import generate_with_scripts, overlay_images

def main():
  if '--text' in sys.argv and '--prompt' in sys.argv:
    try:
      text_idx   = sys.argv.index('--text') + 1
      prompt_idx = sys.argv.index('--prompt') + 1
      text       = sys.argv[text_idx]
      prompt     = sys.argv[prompt_idx]
      generate_with_scripts(text, prompt)
    except Exception as e:
      print("Error parsing arguments", flush=True)
      print(e, flush=True)
  elif len(sys.argv) > 2:
    background = sys.argv[1]
    overlays   = sys.argv[2:]
    overlay_images(background, overlays)
  else:
    print("Usage: python -m make_meme <background> <overlay1> <overlay2> ...", flush=True)
    print("   or: python -m make_meme --text 'Hello' --prompt 'a cat in space'", flush=True)

if __name__ == '__main__':
  main()