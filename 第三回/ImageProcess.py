import os
from PIL import Image
import task1

def main():
    im = Image.open("sample2.png")
    #RGBに変換
    rgb_im = im.convert('RGB')
    #画像のサイズを取得
    size = rgb_im.size
    
    for x in range(size[0]):
        for y in range(size[1]):
            r,g,b = rgb_im.getpixel((x,y))
            r = task1.ToneCurve(r,2)
            g = task1.ToneCurve(r,2)
            b = task1.ToneCurve(r,2)
            print(r,g,b)


if __name__ == "__main__":
    main()

