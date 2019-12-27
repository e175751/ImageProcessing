import os
import numpy as np
import cv2

def main():

    coler = cv2.imread("sample.jpg", 1)
    kernel = np.array([[1/16, 1/8, 1/16],
                   [1/8, 1/4, 1/8],
                   [1/16, 1/8, 1/16]])
    dst = cv2.filter2D(coler, -1, kernel)
    cv2.imwrite("output5_3.jpg", dst)

if __name__ == "__main__":
    main()

