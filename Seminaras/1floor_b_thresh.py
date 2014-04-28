import cv2.cv as cv
import cv2

import sys


cv.NamedWindow("img", 1)
cv.NamedWindow("thr", 1)

#capture = cv.CaptureFromCAM(0)
#img = cv.QueryFrame(capture)

img = cv2.imread("./b.jpg")
img = cv.fromarray(img)


# gray = cv.CreateImage((img.width, img.height), cv.IPL_DEPTH_8U, 1)
dst = cv.CreateImage((img.width, img.height), cv.IPL_DEPTH_8U, 1)
hsv = cv.CreateImage((img.width, img.height), cv.IPL_DEPTH_8U, 3)

cv.CvtColor(img, hsv, cv.CV_BGR2HSV)
# cv.CvtColor(img, gray, cv.CV_BGR2GRAY)

cv.InRangeS(hsv, cv.Scalar(80,0,0), cv.Scalar(180,255,255), dst)

cv.ShowImage("thr", dst)
cv.ShowImage("img", img)

cv.WaitKey(0)
cv.DestroyAllWindows()
quit()
