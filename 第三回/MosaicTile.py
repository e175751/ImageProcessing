from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

def main():
    img = cv2.imread("sample.jpg")
    height, width, channels = img.shape
    out_img=[]

    img = mosaic(img)
    height_split = 3
    width_split = 3
    new_img_height = int(height / height_split)
    new_img_width = int(width / width_split)

    for h in range(height_split):
        height_start = h * new_img_height
        height_end = height_start + new_img_height

        for w in range(width_split):
            width_start = w * new_img_width
            width_end = width_start + new_img_width
            file_name = "test_" + str(h) + "_" + str(w) + ".png"
            clp = img[height_start:height_end, width_start:width_end]
            out_img.append(clp)
            #cv2.imwrite(file_name, clp)
    print(len(out_img))
    out_img = np.array(out_img)
    shuffle = np.random.permutation(range(len(out_img)))
    img = np.vstack((
        np.hstack(out_img[shuffle[0:2]]),
        np.hstack(out_img[shuffle[3:5]]),
        np.hstack(out_img[shuffle[6:8]]),
    ))
    cv2.imwrite("mosaic_result.jpg", img)

def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)




if __name__ == "__main__":
    main()
