import os
import cv2
import matplotlib.pyplot as plt

def main():
    imageurl1 = "./sample2.jpg"

    im = cv2.imread(imageurl1)
    im2= cv2.imread(imageurl1)

    #グレースケール
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    #ガウスフィルタ
    im_gray_smooth=cv2.GaussianBlur(im_gray,(11,11),0)

    #2値化
    ret,th1 = cv2.threshold(im_gray_smooth,130,255,cv2.THRESH_BINARY)

    #輪郭検出
    contours, hierarchy = cv2.findContours(th1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #輪郭描画
    cv2.drawContours(im,contours,-1,(0,255,0),3)

    #描画
    plt.subplot(2,2,1),plt.imshow(im2,'gray')
    plt.title('input image')
    plt.subplot(2,2,2),plt.imshow(im,'gray')
    plt.title('output image')
    plt.subplot(2,2,3),plt.imshow(im_gray_smooth,'gray')
    plt.title('GrayScale+Gaussianfilter')
    plt.subplot(2,2,4),plt.imshow(th1,'gray')
    plt.title('Binarization')
 
    plt.show()


if __name__ == "__main__":
    main()

