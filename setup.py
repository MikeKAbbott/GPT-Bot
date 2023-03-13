from distutils.core import setup
from setuptools import find_packages
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

try:
	with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
		long_description = f.read()
except Exception:
  long_description = ''

setup(
	name = 'GPT-Bot',
	packages = find_packages('.'),
	version = '1.0.0',
	description = long_description,
	author = 'Michael Abbott',
	author_email = 'mikekabbott@gmail.com',
	url = 'https://github.com/MikeKAbbott',
)
