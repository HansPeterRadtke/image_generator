import sys
from .core import make_text

def main():
  make_text(*sys.argv[1:])

if __name__ == '__main__':
  main()