import cv2
import numpy as np

color = cv2.imread("sample.jpg", 1)

kernel = np.array([[1/256, 1/64, 3/128, 1/64, 1/256],
                   [1/64, 1/16, 3/32, 1/16, 1/64],
                   [3/128, 3/32, 9/64, 3/32, 3/128],
                   [1/64, 1/16, 3/32, 1/16, 1/64],
                   [1/256, 1/64, 3/128, 1/64, 1/256]])

dst = cv2.filter2D(color, -1, kernel)

cv2.imwrite("output5_4.jpg", dst)
