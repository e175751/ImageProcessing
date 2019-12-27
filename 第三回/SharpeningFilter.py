import os
import numpy as np
import cv2

def main():
    image = cv2.imread('sample2.jpg')
    cv2.namedWindow("original")
    cv2.moveWindow("original", 200, 200)
    cv2.imshow('original', image)

    #kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]], np.float32)

    kernel = np.array([[-1,-1,-1], [-1,12,-1], [-1,-1,-1]], np.float32)
    dst = cv2.filter2D(image, -1, kernel)

    cv2.namedWindow("result")
    cv2.moveWindow("result", 200, 400)
    cv2.imshow('result', dst)
    cv2.imwrite('output6_1.jpg', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

