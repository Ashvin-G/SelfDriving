import cv2
import numpy as np
import time

from functions import grab_screen
from functions import crop_bottom_minimap
from functions import roi
from functions import perspective_transform

import matplotlib.pyplot as plt

import pyautogui



def main():
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    
    tracker = cv2.TrackerMOSSE_create()
    game_frame = grab_screen()
    bbox = cv2.selectROI("game_frame", game_frame, False)
    tracker.init(game_frame, bbox)

    while True:
        game_frame = grab_screen()
        lane = perspective_transform(game_frame)
       
        success, bbox = tracker.update(game_frame)

        if success:
            x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
            pt1 = (x + int(w/2), y)
            cv2.circle(game_frame, pt1, 3, (0, 0, 255), -1)
            cv2.rectangle(game_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("game_frame", game_frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    

main()


