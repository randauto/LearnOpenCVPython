import cv2 as cv

image1 = cv.imread("res/1bit1.png")
image2 = cv.imread("res/2bit2.png")

dest_and = cv.bitwise_and(image2, image1, mask=None)
dest_or = cv.bitwise_or(image2, image1, mask=None)
dest_not = cv.bitwise_not(image2, image1, mask=None)
dest_xor = cv.bitwise_xor(image2, image1, mask=None)

cv.imshow("And", dest_and)
cv.imshow("Or", dest_or)
cv.imshow("Not", dest_not)
cv.imshow("Xor", dest_xor)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
elif cv.waitKey(0) & 0xff == ord("s"):
    print("Save all image")
    cv.imwrite("dest_and.jpg", dest_and)
    cv.imwrite("dest_or.jpg", dest_or)
    cv.imwrite("dest_not.jpg", dest_not)
    cv.imwrite("dest_xor.jpg", dest_xor)
    cv.destroyAllWindows()
