# Image Processing in Python (Scaling, Rotating, Shifting and Edge Detection)
import cv2 as cv

image = cv.imread("res/girl1.jpg")
try:
    # get number of pixel h and vertical
    (rows, cols) = image.shape[:2]

    M = cv.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)  # lay diem giua cua hinh anh de xoay
    res = cv.warpAffine(image, M, (cols, rows))
    cv.imwrite("rotate_result.jpg", res)
    cv.imshow("Result", res)
    cv.imshow("Original", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
except IOError:
    print("Error while reading file!!!!")
