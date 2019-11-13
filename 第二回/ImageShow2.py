from PIL import Image
from matplotlib import pyplot as plt

def ImageShow():
    im = Image.open("sample.jpg")
    plt.imshow(im)
    plt.pause(10)
    plt.clf()
    print("clf()起動しました")
    plt.pause(5)
    ImageShow()

if __name__ == "__main__":
    ImageShow()
