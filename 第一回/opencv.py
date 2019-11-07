import os
import cv2

def main():
    image_url = "./img_89.png"
    img = cv2.imread(image_url)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

