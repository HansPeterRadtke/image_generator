from setuptools import setup, find_packages

setup(
  name="image_generator",
  version="0.1",
  packages=find_packages(),
  entry_points={
    'console_scripts': [
      'make-ai-image = make_ai_image.__main__',
      'make-text     = make_text.__main__',
      'make-meme     = make_meme.__main__'
    ]
  },
  install_requires=[
    'Pillow',
    'requests'
  ],
  python_requires='>=3.6'
)