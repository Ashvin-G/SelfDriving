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
    
    while True:
        game_frame = grab_screen()       

        cv2.imshow("game_frame", game_frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    

main()


