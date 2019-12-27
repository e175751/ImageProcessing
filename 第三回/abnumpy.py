import numpy as np
from PIL import Image

def main():
    src1 = np.array(Image.open("./sample2.jpg"))
    src2 = np.array(Image.open("./sample.jpg").resize(src1.shape[1::-1], Image.BILINEAR))

    dst = src1 * 0.5 + src2 * 0.5

    Image.fromarray(dst.astype(np.uint8)).save("./abdst.jpg")

if __name__ == "__main__":
    main()
