import cv2
import numpy as np


video = cv2.VideoCapture('/Users/itaegyeong/Desktop/good.mov')
knn = cv2.createBackgroundSubtractorKNN()


ret, frame = video.read()
point = []
frame_count = 0


# Morphology의 opening, closing을 통해서 노이즈제거
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel, iterations=1)

# 붉은색 mask 씌우기
opening_hsv = cv2.cvtColor(opening,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(opening_hsv, np.array((150., 150., 50.)), np.array((190., 255., 255.)))

# 붉은색 mask에 Morpholgy로 잡음 제거
opening2 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

_, contours, _ = cv2.findContours(opening2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for c in contours:
    x, y, w, h = cv2.boundingRect(c)

    area = w * h
    if area < 200 or y < 40:
        continue

    point.append([x,y,w,h])
    print(x, y, area)



while True:
    ret, frame = video.read()
    cv2.imshow('frame',frame)

    # Morphology의 opening, closing을 통해서 노이즈제거
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel, iterations=1)
    cv2.imshow('opening',opening)

    # 붉은색 mask 씌우기
    opening_hsv = cv2.cvtColor(opening,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(opening_hsv, np.array((150., 150., 50.)), np.array((190., 255., 255.)))
    cv2.imshow('masks', mask)

    # 붉은색 mask에 Morpholgy로 잡음 제거
    opening2 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    cv2.imshow('opening2 mask',opening2)


    _, contours, _ = cv2.findContours(opening2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)

        area = w * h
        if area < 200 or y < 40:
            continue

        point.append([x,y,w,h])
        print(x, y, area)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    frame_count = frame_count + 1


    cv2.imshow('frame',frame)
    cv2.waitKey(0)
