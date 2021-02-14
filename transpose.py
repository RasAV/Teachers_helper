import sys
from PIL import Image


if __name__ == '__main__':
    params = sys.argv
    try:
        im = Image.open(params[1])
        im2 = im.transpose(Image.TRANSPOSE)
        im2.save(params[2])
    except:
        print("Something is wrong in the arguments in your query")
