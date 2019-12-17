import os
import numpy as np
from PIL import Image

def main():
    img = np.array(Image.open("sample.jpg"))
    Image.fromarray(np.flip(img, (0,1))).save("Inversdst.jpg")

if __name__ == "__main__":
    main()

