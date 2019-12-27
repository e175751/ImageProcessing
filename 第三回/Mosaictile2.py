from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
im = Image.open('sample.jpg')

fig = plt.figure()

#im_list = np.asarray(im_mirror)#画像を配列にして保存
height = im.height/3
#height =420/3
#width = 598/3
width = im.width/3
buff = []
print(im.height,im.width,height,width)
dst = Image.new('RGB', (im.width, im.height))

# 縦の分割枚数
for h1 in range(3):
    # 横の分割枚数
    for w1 in range(3):
        w2 = w1 * width
        h2 = h1 *  height
        print(w2, h2, width + w2, height + h2)
        c = im.crop((w2, h2, width + w2, height + h2))
        buff.append(c)
        dst.paste(c, (int(w2), int(h2)))


plt.imshow(dst)#画像を貼り付け
plt.show()#画像表示
count=0
for h3 in range(1,4):
    for w3 in range(1,4):
        w4 = (w3-1) * width
        h4 = (h3-1) *  height
        im_mirror = ImageOps.mirror(buff[count])
        dst.paste(im_mirror, (int(w4),int(h4)))
        plt.imshow(dst)#画像を貼り付け
        plt.show()#画像表示
        plt.close()
        plt.pause(5)#五秒維持
        dst.paste(buff[count], (int(w4),int(h4)))
        plt.clf()#図をクリアする
        count+=1
