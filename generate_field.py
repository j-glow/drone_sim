import cv2
import numpy as np
import random

blank = np.zeros((3700,3700,4), np.uint8)

##RECTANGLES
for x in range(10):
    for y in range(10):
        cv2.rectangle(blank, (400*x,400*y), (100+400*x,100+400*y),(255,255,255,255),-1)

## GOLD CIRCLES
circle_gold =[]
for i in range(12):
    place=(random.randint(0,9),random.randint(0,9))
    if circle_gold.count(place) == 0:
        circle_gold.append(place)

for (x,y) in circle_gold:
    cv2.circle(blank, (50+400*x,50+400*y), 50, (65,159,212,255), -1)


## ECRU CIRCLES
circle_ecru =[]
for i in range(8):
    place=(random.randint(0,9),random.randint(0,9))
    if circle_ecru.count(place) == 0:
        circle_ecru.append(place)

for (x,y) in circle_ecru:
    cv2.circle(blank, (50+400*x,50+400*y), 50, (227,246,249,255), -1)

## BROWN CIRCLES
circle_brown =[]
for i in range(9):
    place=(random.randint(0,9),random.randint(0,9))
    if circle_brown.count(place) == 0:
        circle_brown.append(place)

for (x,y) in circle_brown:
    cv2.circle(blank, (50+400*x,50+400*y), 50, (76,107,147,255), -1)

# cv2.imshow("field",blank)
cv2.imwrite("field.png",blank)

cv2.waitKey(0)
cv2.destroyAllWindows()