import os
import cv2
import time

def main():
    #print(os.sys.path)
    VideoTime = 25
    img = cv2.imread("sample.jpg")
    width = img.shape[1]
    height = img.shape[0]
    fourcc = cv2.VideoWriter_fourcc('m','p','4', 'v')
    video = cv2.VideoWriter('out.mp4', fourcc, 20.0, (width, height))
    FrameCount = VideoTime * 20
    for num in range(FrameCount):
        video.write(img)
    video.release()


if __name__ == "__main__":
    main()

