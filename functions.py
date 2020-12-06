import cv2
import win32gui, win32ui, win32con, win32api
import numpy as np
import pyautogui as pg


def grab_screen(region=(0, 50, 794, 610)):
    #Function created by Frannecklp
    
    hwin = win32gui.GetDesktopWindow()

    if region:
            left,top,x2,y2 = region
            width = x2 - left + 1
            height = y2 - top + 1
    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
    
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height,width,4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

    return img


def crop_bottom_minimap(game_frame):
    return game_frame[:400, :]

def roi(game_frame):
    points = np.array([[0, 400], [0, 300], [250, 260], [450, 260], [795, 340], [795, 400]], np.int32)
    
    mask = np.zeros_like(game_frame)

    cv2.fillPoly(mask, [points], (255, 255, 255))

    masked = cv2.bitwise_and(game_frame, mask)

    return masked

def perspective_transform(game_frame):
    pts1 = np.float32([[310, 280], [510, 280], [0, 385], [795, 561]])
    pts2 = np.float32([[0, 0], [800, 0], [0, 800], [800, 800]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    transformed_frame = cv2.warpPerspective(game_frame, matrix, (600, 400))

    return transformed_frame
    
