# moveshape.py
import gizeh as gz
import numpy as np
import moviepy.editor as mpy 


# global variables
max_w = 640
max_h = 480
w = 0
h = 480
UP = True
RADIUS = 30


def make_frame(time):
	global w, h, max_w, max_h, UP
	# set the surface of size 640 * 480 
	surface = gz.Surface(max_w, max_h)

	# UP is checking if the circle is going up
	if UP == True:
		# circle is going up
		w = w + 6.4 	# increase the width  
		h = h - 4.8 	# decrease the height
		# check if the circle go over than the upper right boarder
		if w + RADIUS > max_w or h - RADIUS < 0:
			UP = False	# change UP value to False (going down)
	else: 
		# circle is going down		
		w = w - 6.4 	# decrease the width
		h = h + 4.8 	# increase the height
		# check if the circle go under the bottom left boundary
		if w - RADIUS < 0 or h + RADIUS > max_h:
			UP = True	# change UP value to True (going up)

	# 
	circle = gz.circle(r=RADIUS, xy=(w, h), fill=(1,0,0))
	# draw a circle in a surface
	circle.draw(surface)
	
	return surface.get_npimage()


def main():
	# calls make_frame function for 10 seconds
	clip = mpy.VideoClip(make_frame, duration=10)
	# saving the clips
	clip.write_gif('move_shape.gif', fps=30)



if __name__ == '__main__':
	main()