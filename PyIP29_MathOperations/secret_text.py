# Find the secret text

import cv2
import numpy as np

image_a = cv2.imread("input/a.png")
image_b = cv2.imread("input/b.png")

image_a = 255 - image_a
image_b = 255 - image_b

secret_result = image_a - image_b
secret_result = 255 - secret_result

cv2.imshow("", secret_result)

cv2.imwrite("output/secret_text.jpg", secret_result)
cv2.waitKey()