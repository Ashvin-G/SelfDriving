import cv2
import numpy as np
import time
import pygame
import csv

from functions import grab_screen


pygame.joystick.init()
pygame.joystick.Joystick(0).init()




DATADIR = "./Dataset/"

f = open("log.csv", "w", newline="")
writer = csv.writer(f)

def main():

    image_counter = 0

    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    
    while True:
        game_frame = grab_screen()
        game_frame = cv2.resize(game_frame, (320, 160))
        game_frame = cv2.cvtColor(game_frame, cv2.COLOR_BGR2GRAY)




        val = (pygame.joystick.Joystick(0).get_axis(0))

        image_path = DATADIR+str(image_counter)+".jpg"

        cv2.imwrite(image_path, game_frame)
        writer.writerow([image_path, val])
        image_counter = image_counter + 1


        cv2.imshow('game_frame', game_frame)
        if cv2.waitKey(1) == 27:
            break
    
    f.close()
    cv2.destroyAllWindows()


main()