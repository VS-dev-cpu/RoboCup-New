import cv2 as cv
import numpy as np

cap = cv2.VideoCapture(0)

acorn = cv.imread('acorn_red.jpg')

h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges
channels = [0, 1]

while (1):
    ret, frame = cap.read()
    
    if not ret:
        break
        
    hsv_base = cv.cvtColor(base, cv.COLOR_BGR2HSV)
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    hist_acorn = cv.calcHist([hsv_acorn], channels, None, histSize, ranges, accumulate=False)
    cv.normalize(hist_acorn, hist_acorn, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
    
    hist_frame = cv.calcHist([hsv_frame], channels, None, histSize, ranges, accumulate=False)
    cv.normalize(hist_frame, hist_frame, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
    
    frame_acorn = cv.compareHist(hist_acorn, hist_frame, compare_method)
    
    cv2.waitKey(1)
