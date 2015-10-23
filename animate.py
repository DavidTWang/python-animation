import gizeh


def main():
    surface = gizeh.Surface(width=320, height=320)
    circle = gizeh.circle(r=40, xy=[100, 100], fill=(1, 0, 1))
    circle.draw(surface)
    surface.get_npimage()
    surface.write_to_png("output.png")


if __name__ == '__main__':
    main()
