"""Library"""
from Phygital_v0 import Phygital_v0 as pyro
import time

"""Pin Initialization"""
pyro.pinMode('A0','dOutput')
pyro.pinMode('A1','dOutput')
pyro.pinMode('A2','dOutput')
pyro.pinMode('A3','dOutput')
pyro.pinMode('A4','dOutput')
"""Init"""
pyro.init("COM5")

"""LED ON"""

while True:
    try:
        pyro.dWrite('A0',1)
        pyro.dWrite('A1',1)
        pyro.dWrite('A2',1)
        pyro.dWrite('A3',1)
        pyro.dWrite('A4',1)
        time.sleep(0.5)
        
         #LED Off
        pyro.dWrite('A0',0)
        pyro.dWrite('A1',1)
        pyro.dWrite('A2',2)
        pyro.dWrite('A3',3)
        pyro.dWrite('A4',4)
        time.sleep(0.5) #Wait for 1 Sec
        
        
        
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
        
print("Closed the Connection!!")

"""Closing"""