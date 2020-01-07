import os
import cv2
import numpy as np

def main(img):
    # エッジ検出後にネガポジ反転
    edge= cv2.Canny(img,80,120)
    nega = cv2.bitwise_not(edge)
    # sizeを取得
    width = img.shape[0] 
    height = img.shape[1]
    # 3値化を行う(ただし灰色の場合はスクリーントーンに置き換える)
    temp = np.zeros_like(img)
    for i in range(width):
        for j in range(height):
            if img[i,j]<80:
                temp[i,j] = 0
            elif img[i,j]>=80 and img[i,j]<160:
                temp[i,j] = 160
            else:
                temp[i,j] = 255
    # 3値化とエッジの画像を合成
    cv2.imwrite("result_nega1.jpg",nega)
    cv2.imwrite("result_sample1.jpg",temp)
    alpha = 0.5
    result = cv2.addWeighted(nega,alpha,temp,1-alpha,0.0)
    (thresh,result)=cv2.threshold(result,200,255,cv2.THRESH_BINARY)
    cv2.imwrite("result4.jpg",result)

if __name__ == "__main__":
    #画像取得
    img = cv2.imread("ギアス.jpg")
    # グレースケール変換
    img = cv2.resize(img,(600,800))
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    main(gray)


