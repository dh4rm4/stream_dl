#/usr/bin/env python

__VERSION = '1.0'

from distutils.core import setup
setup(
    name = 'stream_dl',
    version = __VERSION,
    description = 'little soft to DL/convert flux from streaming platform',
    url = 'https://github.com/dh4rm4/stream_dl',
    py_modules=['youtube_dl'],
)
