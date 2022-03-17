# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:48:50 2022

@author: BENEJAH MAYELE
"""

import socket
from cesar_code import cryptage, decryptage

host= '192.168.43.65'
port= 12006
s=socket.socket()
s.connect((host,port))
message=cryptage(12,"jonathan").encode()
s.send(message)