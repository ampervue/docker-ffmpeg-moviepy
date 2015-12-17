__author__ = 'David Karchmer'

import moviepy.editor as mpy

hello_world = mpy.TextClip('Hello, World!', fontsize=78, color='white', size=(1280,720))
hello_world = hello_world.set_duration(10)
hello_world.write_videofile('hello_world.mp4', fps=24)