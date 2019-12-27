import os
import cv2
import numpy as np

def main():
    coler = cv2.imread("sample.jpg",1)
    dst = cv2.blur(coler, ksize=(3,3))
    cv2.imwrite("output5_1.jpg", dst)

if __name__ == "__main__":
    main()

