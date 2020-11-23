"""
Code to Control LED State On-Off
LED connected at A0
"""

"""Library"""
from Phygital_v0 import Phygital_v0 as pyro
import time

"""Pin Initialization"""
pyro.pinMode('A0','dOutput')
pyro.pinMode('A1','dOutput')
pyro.pinMode('A2','dOutput')

"""Init"""
pyro.init("COM5")

"""LED ON"""

while True:
    try:
        pyro.dWrite('A0',0)
        pyro.dWrite('A2',0)
        pyro.dWrite('A1',1)#LED ON
        time.sleep(0.5) #Wait for 1 Sec
        
        pyro.dWrite('A0',1)
        pyro.dWrite('A2',1)
        pyro.dWrite('A1',0) #LED Off
        time.sleep(0.5) #Wait for 1 Sec
        
        
        
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
        
print("Closed the Connection!!")

"""Closing"""
