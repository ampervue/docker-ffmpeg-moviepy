"""
Configuration of MoviePy


Overwriting to make sure it uses the local versions 
of convert and ffmpeg

"""

import os

FFMPEG_BINARY = os.getenv('FFMPEG_BINARY', 'auto-detect')
IMAGEMAGICK_BINARY = os.getenv('FFMPEG_BINARY', 'auto-detect')