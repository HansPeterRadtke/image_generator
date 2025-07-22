from make_meme.core import parse_args, generate_with_scripts
import sys

if __name__ == '__main__':
  print("[DEBUG] make_meme.__main__ sys.argv:", sys.argv, flush=True)
  args = parse_args()
  generate_with_scripts(
    args.text,
    args.prompt,
    text_args=args.text_args,
    image_args=args.image_args,
    save_dir=args.save_dir,
    file_prefix=args.file_prefix,
    file_ext=args.file_ext
  )