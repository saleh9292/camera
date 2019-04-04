# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 02:47:11 2019

@author: Moutaz

Class for socket using ZMQ

"""

import zmq

class NetworkConnect:
    def __init__(self,connectionString, PUB, SUB, PUSH,PULL,REQ,REP):         
        self.contextZMQ = zmq.Context()#create Context 
        #define node mode
        if PUB == True :
            self.socketConnection = self.contextZMQ.socket(zmq.PUB)
            self.socketConnection.connect(connectionString)
        elif SUB == True :
            self.socketConnection = self.contextZMQ.socket(zmq.SUB)
            self.socketConnection.bind(connectionString)
        elif PUSH == True :
            self.socketConnection = self.contextZMQ.socket(zmq.PUSH)
            self.socketConnection.connect(connectionString)
        elif PULL == True : 
            self.socketConnection = self.contextZMQ.socket(zmq.PULL)
            self.socketConnection.bind(connectionString)
        elif REQ == True :
            self.socketConnection = self.contextZMQ.socket(zmq.REQ)
            self.socketConnection.connect(connectionString)
        elif REP == True :
            self.socketConnection = self.contextZMQ.socket(zmq.REP)
            self.socketConnection.bind(connectionString)
    def send(self, text):
        self.socketConnection.send(text)
     
    def rcv(self):
        return self.socketConnection.recv_string()
  
