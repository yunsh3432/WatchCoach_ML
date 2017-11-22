import numpy as np
import cv2

# @brief : 팀을 구별해주는 함수 (메인)
# @param : 이미지
# @return : 1 (아군) ,-1 (적군), 0 (기타)
def team_division(image):

    # HSV color
    boundaries = [
        ([110, 51, 51],[130, 255, 255])


    ]

    # image load
    image_path = "/Users/itaegyeong/Desktop/testblue.png"
    img = cv2.imread(image_path) # or image
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype='uint8')
        upper = np.array(upper, dtype='uint8')
        mask = cv2.inRange(img_hsv, lower, upper)

        count = 0
        for i in range(0, len(mask)):
            for j in mask[i]:
                if j == 255:
                    count = count + 1

    if count > 10000:



