import cv2 as cv

image1 = cv.imread('res/input3.jpg')
image2 = cv.imread('res/input4.jpg')

imgAdd = cv.subtract(image1, image2)
cv.imshow("Subtract 2 Image", imgAdd)
k = cv.waitKey(0) & 0xFF
if k == 27:
    cv.destroyAllWindows()
elif k == ord("s"):
    cv.imwrite("imagesubtract.jpg", imgAdd)
    print("Save Image add")
    cv.destroyAllWindows()
