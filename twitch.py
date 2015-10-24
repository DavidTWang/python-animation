import gizeh
import math
import moviepy.editor as mpy
import argparse
from random import randint


W, H = 500, 300  # Width and height
DURATION = 10  # Duration of animation
PI = math.pi  # Pi for some reason
b_coords = (W/2, H/2)  # Global blue circle coords
r_coords = (W/2, H/2)  # Global red square coords


# Generate new coordinates for the square
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


# Create a frame for the animation based on the timing
def make_frame(t):
    global b_coords, r_coords
    # Create template to work on
    surface = gizeh.Surface(W, H)

    # Generate new coordinates
    b_coords = rand_movement(b_coords)
    r_coords = rand_movement(r_coords)

    # Specify and draw circle and square
    b_circle = gizeh.circle(25, xy=b_coords, fill=(0, 0, 1))
    r_square = gizeh.square(l=50, xy=r_coords, fill=(1, 0, 0), angle=PI*t)

    b_circle.draw(surface)
    r_square.draw(surface)
    # Return a numpy array
    return surface.get_npimage()


def main():
    # Create a video clip based on the duration
    clip = mpy.VideoClip(make_frame, duration=DURATION)
    # Write it as a gif
    clip.write_gif("twitch.gif", fps=24, opt="OptimizePlus", fuzz=10)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--width", help="Width of the surface")
    parser.add_argument("-y", "--height", help="Height of the surface")
    args = parser.parse_args()
    if(args.width is not None):
        W = args.width
    if(args.height is not None):
        H = args.height
    main()
