import pdb
from PIL import Image
import argparse




def image_info(input_file):
    # Opening Image as an object
    Img = Image.open(input_file)
    # Getting the filename of image
    print("Filename : ",Img.filename)
    # Getting the format of image
    print("Format : ",Img.format)
    # Getting the mode of image
    print("Mode : ",Img.mode)
    # Getting the size of image
    print("Size : ",Img.size)
    # Getting only the width of image
    print("Width : ",Img.width)
    # Getting only the height of image
    print("Height : ",Img.height)
    # Getting the color palette of image
    print("Image Palette : ",Img.palette)
    # Getting the info about image
    #print("Image Info : ",Img.info)
    # Closing Image object
    Img.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image info',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', action="store", dest="input",required=True,help='Input image file name')
    results = parser.parse_args()
    image_info(results.input)

