import cv2
import numpy as np
import time

from functions import grab_screen
from getKeys import key_check


DATADIR = "../SelfDriving_Dataset/"



def main():

    A_counter = 0
    W_counter = 0
    D_counter = 0

    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    
    while True:
        game_frame = grab_screen()
        
        key_pressed = key_check()

        if key_pressed == 'A':
            cv2.imwrite(DATADIR+"A/"+str(A_counter)+".jpg", game_frame)
            A_counter = A_counter + 1
        elif key_pressed == 'W':
            cv2.imwrite(DATADIR+"W/"+str(W_counter)+".jpg", game_frame)
            W_counter = W_counter + 1
        if key_pressed == 'D':
            cv2.imwrite(DATADIR+"D/"+str(D_counter)+".jpg", game_frame)
            D_counter = D_counter + 1
        else:
            pass

        cv2.imshow('game_frame', game_frame)
        if cv2.waitKey(1) == 27:
            break
    
    
    cv2.destroyAllWindows()


main()