# -*- coding: utf-8 -*-
 
import RPi.GPIO as gpio
import time

class dht11(self):
    def __init__(self, pinmode, pin):
        self.pin = pin
        gpio.setwarnings(False)
        if pinmode == 'BCM':
            gpio.setmode(gpio.BCM)
        else:
            gpio.setmode(gpio.BOARD)

    def get(self):
        data=[]
        #start work
        gpio.setup(datapin,gpio.OUT)
        #gpio.output(datapin,gpio.HIGH)
        #delay(10)
        gpio.output(datapin,gpio.LOW)
        time.sleep(0.02)
        gpio.output(datapin,gpio.HIGH)
        #wait to response
        gpio.setup(datapin,gpio.IN)
        while gpio.input(datapin)==1:
            continue
        while gpio.input(datapin)==0:
            continue
        while gpio.input(datapin)==1:
                continue
        #get data
        while j<40:
            k=0
            while gpio.input(datapin)==0:
                continue
            while gpio.input(datapin)==1:
                k+=1
                if k>100:break
            if k<6:
                data.append(0)
            else:
                data.append(1)
            j+=1
        #get temperature
        humidity_bit=data[0:8]
        humidity_point_bit=data[8:16]
        temperature_bit=data[16:24]
        temperature_point_bit=data[24:32]
        check_bit=data[32:40]
         
        humidity=0
        humidity_point=0
        temperature=0
        temperature_point=0
        check=0
         
        for i in range(8):
            humidity+=humidity_bit[i]*2**(7-i)
            humidity_point+=humidity_point_bit[i]*2**(7-i)
            temperature+=temperature_bit[i]*2**(7-i)
            temperature_point+=temperature_point_bit[i]*2**(7-i)
            check+=check_bit[i]*2**(7-i)
         
        tmp=humidity+humidity_point+temperature+temperature_point
        if check==tmp:
            return {'t':temperature, 'h':humidity}
        else:
            return None
        

