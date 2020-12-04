import cv2
import numpy as np
import time

from functions import grab_screen
from functions import crop_bottom_minimap
from functions import roi
from functions import perspective_transform

import matplotlib.pyplot as plt



def main():
    # for i in range(3, 0, -1):
    #     print(i)
    #     time.sleep(1)
    
    while True:
        game_frame = grab_screen()
        game_frame = crop_bottom_minimap(game_frame)
        roi_game_frame = roi(game_frame)
        lane = perspective_transform(roi_game_frame)
       

        cv2.imshow('roi', roi_game_frame)
        cv2.imshow('lane', lane)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()

    


main()


