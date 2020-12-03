import pygame
import csv
import cv2

pygame.joystick.init()
pygame.joystick.Joystick(0).init()

JoyName = pygame.joystick.Joystick(0).get_name()
#print("Joystick Name : ", JoyName)

JoyAx = pygame.joystick.Joystick(0).get_numaxes()
#print("Number of Axis : ", JoyAx)

f = open("log.csv", "w", newline="")
writer = csv.writer(f)

while True:
        val = (pygame.joystick.Joystick(0).get_axis(0))
        print(val)
        if cv2.waitKey(1) == 27:
            break
f.close()