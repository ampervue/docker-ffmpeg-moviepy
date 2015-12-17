"""
Configuration of MoviePy


Overwriting to make sure it uses the local versions 
of convert and ffmpeg

"""

import os

FFMPEG_BINARY = os.getenv('FFMPEG_BINARY', 'ffmpeg')
IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'convert')