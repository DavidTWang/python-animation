import gizeh
import moviepy.editor as mpy
import imageio

D = 7.5 #duration in seconds
letter = "Liger" #Word to be moved
fsize = 10 #font size

def make_frame(t):
	global fsize
	#create image on the surface
	im = imageio.imread("Liger.png")
	surface = gizeh.Surface.from_image(im)
	#grab width and height
	x = im.shape[1]
	y = im.shape[0]
	#start in the middle
	xmid = x/2
	#have the text move up
	y = y - t*130
	#increase font size by 1
	fsize = fsize + 1
	#set the text font, font size, font weight, color, and starting x and y position
	txt = gizeh.text(letter, fontfamily="Impact", fontsize=fsize, fontweight='bold', fill=(0,0,1), xy=(xmid, y))
	#draw the text on the surface
	txt.draw(surface)
	return surface.get_npimage()

#call make_frame method with duration
clip = mpy.VideoClip(make_frame, duration=D)
#create the clip
clip.write_gif("animation.gif", fps=20, opt="OptimizePlus")