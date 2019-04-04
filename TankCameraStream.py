# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 05:14:28 2019

@author: Moutaz
"""
from NetworkConnect import NetworkConnect
from GetFrames import GetFrames
from EncodingFrame import EncodingFrame

class TankCameraStream:
    def __init__(self,isServer):
        
        self.isServer = isServer
        if self.isServer == True :
            self.NetworkConnect = NetworkConnect('tcp://192.168.56.1:5556' , False, False, True,False,False,False) #'tcp://192.168.56.1:5555' , False, False, True,False,False,False)
        else:
            self.NetworkConnect = NetworkConnect('tcp://*:5556', False, False, False,True,False,False) #'tcp://192.168.56.1:5555' , False, False, True,False,False,False)
        
        self.GetFrames = GetFrames(True)
        self.EncodingFrame = EncodingFrame(True)
        
    def run(self):
        while True:
            if self.isServer == True :
                encoded, buffer = self.GetFrames.CaptureFrame()
                frameTextCoded = self.EncodingFrame.FrameEncoder(buffer) 
                self.NetworkConnect.send(frameTextCoded)
            else:
                frameTextCoded = self.NetworkConnect.rcv()
                buffer = self.EncodingFrame.FrameDecoder(frameTextCoded)
                frame = self.GetFrames.GetFrameFromText(buffer)
                self.GetFrames.showCameraFeed(frame)        
        
if __name__ == '__main__':
    Tank01 = TankCameraStream(False)
    Tank01.run()
        
        
