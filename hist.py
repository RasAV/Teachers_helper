import sys
from PIL import Image

if __name__ == '__main__':
    params = sys.argv
    colors = {}
    try:
        im = Image.open(params[1])
        obj = im.load()
        for i in range(im.size[0]):
            for j in range(im.size[1]):
                currColor = obj[i, j]
                if currColor not in colors:
                    colors[currColor] = 1
                else:
                    colors[currColor] += 1

        for rgb in sorted(colors, key=colors.get, reverse=True):
            # print(type(rgb))
            print(rgb[0], ", ", rgb[1], ", ", rgb[2], ": ", colors[rgb], sep="")
    except():
        print("Something is wrong in the arguments in your query")
