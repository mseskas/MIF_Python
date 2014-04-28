import cv2.cv as cv
import cv2

import sys

cv.NamedWindow("camera", 1)
cv.NamedWindow("thr", 1)

# capture = cv.CaptureFromCAM(0)
# img = cv.QueryFrame(capture)

img = cv2.imread("./d.jpg")
img = cv.fromarray(img)

gray = cv.CreateImage((img.width, img.height), 8, 1)
dst = cv.CreateImage((img.width, img.height), 8, 1)

cv.CvtColor(img, gray, cv.CV_BGR2GRAY)

cv.AdaptiveThreshold(gray, dst, maxValue=255,
    adaptive_method=cv.CV_ADAPTIVE_THRESH_GAUSSIAN_C)

# CV_ADAPTIVE_THRESH_GAUSSIAN_C 
# CV_ADAPTIVE_THRESH_MEAN_C


cv.ShowImage("thr", dst)
cv.ShowImage("camera", img)

cv.WaitKey(0)
cv.DestroyAllWindows()
quit()



