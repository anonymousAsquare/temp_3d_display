import serial
from vpython import * 
import time
import numpy as np
import math
from datetime import datetime

mBox_size = (.1,.1,.01)
color_black = vector(.2,.2,.2)
color_white = vector(.9,.9,.9)
mBox = box(size = vector(mBox_size[0],mBox_size[1],mBox_size[2]), pos = vector(0,0,0), axis = vector(0,0,0),color = color_white)
mBox1 = box(size = vector(mBox_size[0],mBox_size[1]*.25,mBox_size[2]), pos = vector(0,-(mBox_size[1]/2)+mBox_size[1]*.25/2,mBox_size[2]), axis = vector(0,0,0), color = color_white)
mBox2 = box(size = vector(mBox_size[0],mBox_size[1]*.25*0.25,mBox_size[2]), pos = vector(0,(-(mBox_size[1]/2)+((mBox_size[1]*.25*0.25)/2)+(mBox_size[1]*.25)),mBox_size[2]), axis = vector(0,0,0), color = color_black)
mBox3 = box(size = vector(mBox_size[0]*.25*0.25,mBox_size[1]-(mBox_size[1]*.25)-(mBox_size[1]*.25*0.25),mBox_size[2]), pos = vector((mBox_size[0]/2)-((mBox_size[0]*.25*0.25)/2),(mBox_size[1]/2)-(mBox_size[1]-(mBox_size[1]*.25)-(mBox_size[1]*.25*0.25))+((mBox_size[1]-(mBox_size[1]*.25)-(mBox_size[1]*.25*0.25))/2),mBox_size[2]), axis = vector(0,0,0), color = color_black)
mBox4 = box(size = vector(mBox_size[0]*.25*0.25,mBox_size[1]-(mBox_size[1]*.25)-(mBox_size[1]*.25*0.25),mBox_size[2]), pos = vector((-mBox_size[0]/2)+((mBox_size[0]*.25*0.25)/2),(mBox_size[1]/2)-(mBox_size[1]-(mBox_size[1]*.25)-(mBox_size[1]*.25*0.25))+((mBox_size[1]-(mBox_size[1]*.25)-(mBox_size[1]*.25*0.25))/2),mBox_size[2]), axis = vector(0,0,0), color = color_black)
mBox5 = box(size = vector(mBox_size[0],mBox_size[1]*.25*0.25,mBox_size[2]), pos = vector(0,((mBox_size[1]/2)-((mBox_size[1]*.25*0.25)/2)),mBox_size[2]), axis = vector(0,0,0), color = color_black)
mBox6 = box(size = vector(mBox_size[0]-(mBox_size[0]*.25*0.25)*2,mBox_size[1]-(mBox_size[1]*.25)-(mBox_size[1]*.25*0.25)-(mBox_size[1]*.25*0.25),mBox_size[2]*0.1), pos = vector(0,(mBox_size[1]/2)-(mBox_size[1]-(mBox_size[1]*.25)-(mBox_size[1]*.25*0.25))+((mBox_size[1]-(mBox_size[1]*.25)-(mBox_size[1]*.25*0.25))/2)-((mBox_size[1]*.25*0.25)/2),(mBox_size[2])+(mBox_size[2]/2)-(mBox_size[2]*0.1/2)), axis = vector(0,0,0), color = vector(1,1,1) ,opacity = .1)
mBox7 = box(size = vector(mBox_size[0]-(mBox_size[0]*.25*0.25)*2,mBox_size[1]-(mBox_size[1]*.25)-(mBox_size[1]*.25*0.25)-(mBox_size[1]*.25*0.25),mBox_size[2]*0.1), pos = vector(0,(mBox_size[1]/2)-(mBox_size[1]-(mBox_size[1]*.25)-(mBox_size[1]*.25*0.25))+((mBox_size[1]-(mBox_size[1]*.25)-(mBox_size[1]*.25*0.25))/2)-((mBox_size[1]*.25*0.25)/2),(mBox_size[2])+(mBox_size[2]/2)-(mBox_size[2]*0.1/2)-(mBox_size[2]*0.9)), axis = vector(0,0,0), color = vector(.8,.85,.8))
mBox8 = box(size = vector(mBox_size[0]-(mBox_size[0]*.25*0.25)*2,mBox_size[1]*0.01,mBox_size[2]*0.1), pos = vector(0,(mBox_size[1]/2)-(mBox_size[1]-(mBox_size[1]*.25)-(mBox_size[1]*.25*0.25))+((mBox_size[1]-(mBox_size[1]*.25)-(mBox_size[1]*.25*0.25))/2)-((mBox_size[1]*.25*0.25)/2)-mBox_size[1]*0.08,(mBox_size[2])+(mBox_size[2]/2)-(mBox_size[2]*0.1/2)-(mBox_size[2]*0.89)), axis = vector(0,0,0), color = vector(0,0,0))
mBox9 = box(size = vector(mBox_size[0]*.01,mBox_size[1]*0.28,mBox_size[2]*0.1), pos = vector(0,(-mBox_size[1]/2)+((mBox_size[1]*0.28)/2)+(mBox_size[1]*0.28)-(mBox_size[1]*0.01),(mBox_size[2])+(mBox_size[2]/2)-(mBox_size[2]*0.1/2)-(mBox_size[2]*0.89)), axis = vector(0,0,0), color = vector(0,0,0))
mText = text(text = 'o', align = 'center', height = mBox_size[1]*.03, pos = vector(mBox_size[0]*0.3,mBox_size[1]*0.38,(mBox_size[2])+(mBox_size[2]/2)-(mBox_size[2]*0.1/2)-(mBox_size[2]*0.88)),color = vector(0,0,0))
mText1 = text(text = 'C', align = 'center', height = mBox_size[1]*.1, pos = vector(mBox_size[0]*0.35,mBox_size[1]*0.3,(mBox_size[2])+(mBox_size[2]/2)-(mBox_size[2]*0.1/2)-(mBox_size[2])),color = vector(0,0,0))
mText2 = text(text = '00.00',opacity = 1, align = 'center', height = mBox_size[1]*.22, pos = vector(-mBox_size[0]*.04,mBox_size[1]*.11,(mBox_size[2])+(mBox_size[2]/2)-(mBox_size[2]*0.1/2)-(mBox_size[2]*1.28)),color = vector(0,0,0))
mText3 = text(text = '%', align = 'center', height = mBox_size[1]*.06, pos = vector(mBox_size[0]*.38,-mBox_size[1]*.1,(mBox_size[2])+(mBox_size[2]/2)-(mBox_size[2]*0.1/2)-(mBox_size[2]*0.95)),color = vector(0,0,0))
mText4 = text(text = '00.00',opacity = 1, align = 'center', height = mBox_size[1]*.09, pos = vector(mBox_size[0]*.18,-mBox_size[1]*.12,(mBox_size[2])+(mBox_size[2]/2)-(mBox_size[2]*0.1/2)-(mBox_size[2])),color = vector(0,0,0))
mText5 = text(text = '00:00:00', align = 'center', height = mBox_size[1]*.07, pos = vector(-mBox_size[0]*.23,-mBox_size[1]*.11,(mBox_size[2])+(mBox_size[2]/2)-(mBox_size[2]*0.1/2)-(mBox_size[2]*0.98)),color = vector(0,0,0), opacity = 1)

oldtempC = 0.00
oldhumidity = 0.00
oldtime = datetime.now()
oldtime = oldtime.strftime("%H:%M:%S")
arduinoData = serial.Serial('com5', 115200)
time.sleep(3)

while True:
    while(arduinoData.inWaiting()==0):
        pass
    dataPack = arduinoData.readline()
    dataPack = str(dataPack, 'utf-8')
    dataPack = dataPack.strip("\r\n")
    dataSplit = dataPack.split(',')
    tempFr = dataSplit[0]
    tempCr = dataSplit[1]
    humidityr = dataSplit[2]
    tempF = float(tempFr.split(' ')[0])
    tempC = float(tempCr.split(' ')[0])
    humidity = float(humidityr.split(' ')[0])
    if oldtempC != tempC:
        mText2.opacity = 0
        mText2 = text(text = str(tempC), align = 'center', height = mBox_size[1]*.22, pos = vector(-mBox_size[0]*.04,mBox_size[1]*.11,(mBox_size[2])+(mBox_size[2]/2)-(mBox_size[2]*0.1/2)-(mBox_size[2]*1.28)),color = vector(0,0,0), opacity = 1)
    
    if oldhumidity != humidity:
        mText4.opacity = 0
        mText4 = text(text = str(humidity), align = 'center', height = mBox_size[1]*.09, pos = vector(mBox_size[0]*.18,-mBox_size[1]*.12,(mBox_size[2])+(mBox_size[2]/2)-(mBox_size[2]*0.1/2)-(mBox_size[2])),color = vector(0,0,0), opacity = 1)
    
    now = datetime.now()
    now = now.strftime("%H:%M:%S")

    if oldtime != now:
        mText5.opacity = 0
        mText5 = text(text = str(now), align = 'center', height = mBox_size[1]*.07, pos = vector(-mBox_size[0]*.23,-mBox_size[1]*.11,(mBox_size[2])+(mBox_size[2]/2)-(mBox_size[2]*0.1/2)-(mBox_size[2]*0.98)),color = vector(0,0,0), opacity =1)
    
    oldtempC = tempC
    oldhumidity = humidity
    oldtime = datetime.now()
    oldtime = oldtime.strftime("%H:%M:%S")
    #print((tempF,tempC,humidity))