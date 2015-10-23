import gizeh
import moviepy.editor as mpy
import imageio

D = 7.5 #duration in seconds
letter = "Liger"
fsize = 10 #font size

def make_frame(t):
	global fsize
	im = imageio.imread("Liger.png")
	surface = gizeh.Surface.from_image(im)
	#grab width and height
	x = im.shape[1]
	y = im.shape[0]
	xmid = x/2
	#have the text move up
	y = y - t*130
	#increase font size
	fsize = fsize + 1 
	txt = gizeh.text(letter, fontfamily="Impact", fontsize=fsize, fontweight='bold', fill=(0,0,1), xy=(xmid, y))
	txt.draw(surface)
	return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif("animation.gif", fps=20, opt="OptimizePlus")