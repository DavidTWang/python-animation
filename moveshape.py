# moveshape.py
import moviepy
import gizeh
import numpy as np


clip = VideoClip(make_frame, duration=4) # for custom animations (see below)
clip = VideoFileClip("my_video_file.mp4") # or .avi, .webm, .gif ...
clip = ImageSequenceClip(['moving1.png', 'moving2.png', 'moving3.png', 'moving4.png', 'moving5.png', ], fps=24)
#clip = ImageClip("my_picture.png") # or .jpeg, .tiff, ...
#clip = TextClip("Hello !", font="Amiri-Bold", fontsize=70, color="black")
clip = ColorClip(size=(640,480), color=[R,G,B])