# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 05:01:09 2019

@author: Moutaz
"""

import base64

class EncodingFrame:
    def __init__(self,base64Enable): 
        self.base64Enable = base64Enable
        
        
    def FrameEncoder (self, frameBuffer):            
        frameText = base64.b64encode(frameBuffer)
        return frameText
    
    
    def FrameDecoder(self, frameText): 
        frameBuffer = base64.b64decode(frameText)
        return frameBuffer
            
        