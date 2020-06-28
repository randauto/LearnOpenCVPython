# Image Processing in Python (Scaling, Rotating, Shifting and Edge Detection)
import cv2 as cv

image = cv.imread("res/girl1.jpg")
try:
    # get number of pixel h and vertical
    (height, width) = image.shape[:2]

    res = cv.resize(image, (int(width / 2), int(height / 2)), interpolation=cv.INTER_CUBIC)
    cv.imwrite("result.jpg", res)
    cv.imshow("Result", res)
    cv.imshow("Original", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
except IOError:
    print("Error while reading file!!!!")
