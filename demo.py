import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("logo.png"))
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("We-Fly", img)
k = cv.waitKey(0)
