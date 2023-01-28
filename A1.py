from vpython import *
import math
import numpy as np
import serial
import time


cylR1 = .5
cylR2 = .5

hndL = cylR1*0.7
cyl2 = cylinder(pos = vector(0,0,-cylR1*0.01), axis = vector(math.cos(math.pi/2),0,sin(math.pi/2)), radius = cylR2, size = vector(.2,0,0), color = vector(0,1,0))
cyl1 = cylinder(pos = vector(0,0,0), axis = vector(math.cos(math.pi/2),0,sin(math.pi/2)), radius = cylR1, size = vector(.2,0,0))
cyl0 = cylinder(pos = vector(0,0,.024), axis = vector(math.cos(math.pi/2),0,sin(math.pi/2)), radius = cylR1, size = vector(.2,0,0), opacity = .2)
bx1 = box(size = vector(cylR2*2.5,.7,.5), pos = vector(0,-(.7/2)-(cylR2*0.1)-(cylR2*0.1/2),.01), color = vector(0,0,0))
bx2 = box(size = vector(cylR2*2,cylR2*0.1,.5), pos = vector(0,-cylR2*0.1,-.02), color = vector(0,1,0))
frm = ring(radius = cylR1, pos = vector(0,0,.15),axis = vector(math.cos(math.pi/2),0,sin(math.pi/2)), thickness = .1 , color = vector(0,1,0))
hnd = arrow(pos = vector(0,0,.2), axis = vector(hndL*math.cos(0),hndL*math.sin(0),0), length = cylR1*0.7, shaftwidth = .01, color = vector(1,0,0), headwidth = .015)
sph = sphere(pos = vector(0,0,.2),radius = .02, color = vector(1,0,0))
labH = 0.05
x = 0
#lab = text(text = 'A',align='center',pos = vector((cylR1-.15)*math.cos(0), (cylR1-.15)*math.sin(0),.2),height = .05,color = vector(0,255,0))

for i in np.linspace(0,math.pi,51):
    box(pos = vector((cylR1-.1)*math.cos(i), (cylR1-.1)*math.sin(i),.18), size = vector(cylR1 * 0.04,cylR1 * 0.01,cylR1 * 0.1), axis = vector(cylR1*math.cos(i), cylR1*math.sin(i),0), color = vector(0,0,0))

for i in np.linspace(0,math.pi,6):
    box(pos = vector((cylR1-.1)*math.cos(i), (cylR1-.1)*math.sin(i),.18), size = vector(cylR1 * 0.09,cylR1 * 0.04,cylR1 * 0.1), axis = vector(cylR1*math.cos(i), cylR1*math.sin(i),0), color = vector(1,0,0))
    
    lab = text(text = str(x),align='center',pos = vector((cylR1-(cylR1 * 0.09)-(labH*2))*math.cos(i), ((cylR1-(cylR1 * 0.09)-(labH*2))*math.sin(i))-labH/2,.2),height = labH,color = vector(0,0,0))
    x += 1


arduinoData = serial.Serial('com5', 115200)
time.sleep(3)

while True:
    while(arduinoData.inWaiting()==0):
        pass
    dataPack = arduinoData.readline()
    dataPack = str(dataPack, 'utf-8')
    dataPack = dataPack.strip('\r\n')
    splitd = dataPack.split("V")
    voltage = float(splitd[0])
    #print(voltage)
    vpVolt = (math.pi/5) * voltage
    #print(vpVolt)

    hnd.axis = vector(hndL*math.cos(vpVolt),hndL*math.sin(vpVolt),0)