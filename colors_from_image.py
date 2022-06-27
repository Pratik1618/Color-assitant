import colorgram


def rgb_to_hex(r, g, b):
    return ('{:X}{:X}{:X}').format(r, g, b)


def getColors(filename):

    rgb_colors = []
    hex_colors = []
    print(filename)

    colors = colorgram.extract(f"/home/jayesh/Desktop/new/{filename}", 10)

    for i in colors:
        rgb_colors.append(i.rgb)

    for i in rgb_colors:
        hex_colors.append(rgb_to_hex(i.r, i.g, i.b))

    print(hex_colors)
    return hex_colors
