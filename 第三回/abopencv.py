import os
import numpy as np
import cv2

def main():
    src1 = cv2.imread('./sample3.jpg')
    src2 = cv2.imread("./sample4.jpg")
    src2 = cv2.resize(src2,src1.shape[1::-1])

    dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)
    cv2.imwrite("./abdst.jpg",dst)

if __name__ == "__main__":
    main()

