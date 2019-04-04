# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 04:55:22 2019

@author: Moutaz
"""

import cv2
import zmq
import numpy as np
import pyautogui
import imutils

class GetFrames:
    def __init__(self,screenCapture): 
        self.screenCapture = screenCapture
    def CaptureFrame(self):
        if self.screenCapture == True:
            image = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            encoded, buffer = cv2.imencode('.jpg', image)
            return encoded, buffer
    def GetFrameFromText (self, frameBuffer):
        npFrame = np.fromstring(frameBuffer, dtype=np.uint8)
        frame = cv2.imdecode(npFrame, 1)
        return frame
    def showCameraFeed (self, frame):
        cv2.imshow("Tank01 Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows() 
            
            