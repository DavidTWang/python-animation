import gizeh
import math
import moviepy.editor as mpy
from random import randint


W, H = 500, 300
DURATION = 10
PI = math.pi
b_coords = (W/2, H/2)
r_coords = (W/2, H/2)


def rand_movement(coords):
    x = coords[0] + randint(-5, 5)
    y = coords[1] + randint(-5, 5)
    if(x >= W):
        x -= 10
    elif(x <= 0):
        x += 10
    if(y >= H):
        y -= 10
    elif(y <= 0):
        y += 10
    return (x, y)


def make_frame(t):
    global b_coords, r_coords
    surface = gizeh.Surface(W, H)

    b_coords = rand_movement(b_coords)
    r_coords = rand_movement(r_coords)

    b_circle = gizeh.circle(25, xy=b_coords, fill=(0, 0, 1))
    r_square = gizeh.square(l=50, xy=r_coords, fill=(1, 0, 0), angle=PI*t)

    b_circle.draw(surface)
    r_square.draw(surface)
    return surface.get_npimage()


def main():
    clip = mpy.VideoClip(make_frame, duration=DURATION)
    clip.write_gif("circle.gif", fps=24, opt="OptimizePlus", fuzz=10)

if __name__ == '__main__':
    main()
