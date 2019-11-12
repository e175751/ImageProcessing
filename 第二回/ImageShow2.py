import os
import cv2
from matplotlib import pyplot as plt

def main():
    url = "sample.jpg"
    ImageShow(url)
    print("finish")

def ImageShow(url):
    img = cv2.imread(url)
    plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    main()

