import cv2

image = cv2.imread("girl1.jpg")
(b, g, r) = image[0, 0]

print("Pixels at (0,0) - Red: {}, Green:{}, Blue:{}".format(r, g, b))
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixels at (0,0) - Red: {}, Green:{}, Blue:{}".format(r, g, b))
