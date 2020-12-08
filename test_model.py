import cv2
import numpy as np
import time
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from functions import grab_screen
from tensorflow.keras.models import load_model



import pyautogui




print("Loading Model!!!!")
model = load_model("model.h5")
print("Model Loaded!!!")

def main():
    try:
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
    
        while True:
            game_frame = grab_screen()
            game_frame = cv2.cvtColor(game_frame, cv2.COLOR_BGR2GRAY)
            game_frame = cv2.resize(game_frame, (100, 100))

            prediction = model.predict(game_frame.reshape(-1, 100, 100, 1))
            print(np.argmax(prediction[0]))
            
            
            if cv2.waitKey(1) == 27:
                break

        
    except KeyboardInterrupt:
        pass
        

main()


