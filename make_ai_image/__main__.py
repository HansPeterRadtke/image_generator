import sys
from .core import make_ai_image

def main():
  if len(sys.argv) < 2:
    print("Usage: python -m make_ai_image 'prompt text'", flush=True)
    sys.exit(1)
  make_ai_image(sys.argv[1])

if __name__ == '__main__':
  main()