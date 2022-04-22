import cv2
import numpy as np

cap = cv2.VideoCapture(0)

acorn = cv2.imread('acorn_red.jpg')
wall = cv2.imread('wall.jpg')

def cross (frame, x, y, r, g, b, s):
    frame = cv2.line(frame, (int(x), 0), (int(x), 2000), (b, g, r), s)
    frame = cv2.line(frame, (0, int(y)), (2000, int(y)), (b, g, r), s)

while (1):
    ret, frame = cap.read()
    
    acorn_res = cv2.matchTemplate(frame, acorn, cv2.TM_CCOEFF_NORMED)
    wall_res = cv2.matchTemplate(frame, wall, cv2.TM_CCOEFF_NORMED)
    
    threshold = .8
    
    acorn_loc = np.where(acorn_res >= threshold)
    wall_loc = np.where(wall_res >= threshold)
    
    for pt in zip(*acorn_loc[::-1]):
        cross(frame, pt[0], pt[1], 255, 0, 0, 2)
        
    for pt in zip(*wall_loc[::-1]):
        cross(frame, pt[0], pt[1], 100, 100, 100, 2)

    cv2.imshow('frame', frame)
    
    cv2.waitKey(1)
