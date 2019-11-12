import os
import cv2

def main():
    url = "sample.jpg"
    im = cv2.imread(url)
    print(im.shape)

if __name__ == "__main__":
    main()

