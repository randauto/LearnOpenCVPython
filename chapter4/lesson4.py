import cv2 as cv
import matplotlib.pyplot as plt

image1 = cv.imread("res/girl1.jpg")

half = cv.resize(image1, (0, 0), fx=0.1, fy=0.1)
bigger = cv.resize(image1, (1050, 1610))
stretch_near = cv.resize(image1, (780, 540), interpolation=cv.INTER_NEAREST)

Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
images = [image1, half, bigger, stretch_near]
count = 4
for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])
plt.show()
