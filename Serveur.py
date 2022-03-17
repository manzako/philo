# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:38:32 2022

@author: MANZAKO MANGOMBE
"""

import socket
import os
import sys
from cesar_code import cryptage, decryptage

host= '192.168.137.787'
port= 12006
s=socket.socket()
s.bind((host,port))
s.listen(10)
while True:
    c,adresse=s.accept()
    print("client",adresse)
    message=s.recv(100).decode()
    print("message decrypté",message)
    print("message decrypté", decryptage(12,message))