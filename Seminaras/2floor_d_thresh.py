import cv2.cv as cv
import cv2

import sys


cv.NamedWindow("camera", 1)
cv.NamedWindow("thr", 1)

#capture = cv.CaptureFromCAM(0)
#img = cv.QueryFrame(capture)

img = cv2.imread("./d.jpg")
img = cv.fromarray(img)

dst = cv.CreateImage((img.width, img.height), cv.IPL_DEPTH_8U, 1)
hsv = cv.CreateImage((img.width, img.height), cv.IPL_DEPTH_8U, 3)

cv.CvtColor(img, hsv, cv.CV_BGR2HSV)

#cv.InRangeS(hsv, cv.Scalar(0,100,0), cv.Scalar(180,255,255), dst)
#cv.InRangeS(hsv, [0,100,0], [180,255,255], dst)
cv.InRangeS(hsv, (0,100,0), (180,255,255), dst)

cv.ShowImage("thr", dst)
cv.ShowImage("camera", hsv)

cv.WaitKey(0)
cv.DestroyAllWindows()
quit()

"""
dst = cv.CreateImage((img.width, img.height), cv.IPL_DEPTH_8U, 1)

cv.CvtColor(img, img, cv.CV_BGR2HSV)

cv.InRangeS(img, (0,100,0), (180,255,255), dst)

cv.ShowImage("thr", dst)
cv.ShowImage("camera", img)
"""
