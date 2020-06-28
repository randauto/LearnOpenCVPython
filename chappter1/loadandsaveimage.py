import cv2

image = cv2.imread("girl1.jpg")
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

cv2.imshow("Load Image", image)
cv2.waitKey(0)
cv2.imwrite("girl1copy.jpg", image)