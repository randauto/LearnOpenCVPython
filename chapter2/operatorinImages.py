import cv2 as cv

image1 = cv.imread('res/girl2.jpg')
image2 = cv.imread('res/girl3.jpg')

imgAdd = cv.addWeighted(image1, 0.5, image2, 0.4, 0)
cv.imshow("Add 2 Image", imgAdd)
k = cv.waitKey(0) & 0xFF
if k == 27:
    cv.destroyAllWindows()
elif k == ord("s"):
    cv.imwrite("imageadd.jpg", imgAdd)
    print("Save Image add")
    cv.destroyAllWindows()
