import os
import cv2
from time import sleep

def main():
    url = "sample1.png"
    ImageShow(url)

def ImageShow(url):
    img = cv2.imread(url)
    cv2.imshow("img",img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
    sleep(5)
    ImageShow(url)


if __name__ == "__main__":
    main()

