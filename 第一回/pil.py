import os
from PIL import Image, ImageFilter
import numpy as np

def main():
    image_url = "./img_89.png"
    img = Image.open(image_url)
    #width, height = img.size
    #img2 = Image.new('RGB', (width, height))
    img.show()

if __name__ == "__main__":
    main()

