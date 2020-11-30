import time
from machine import Pin, PWM

#set the 3 variables for each color
blue = PWM(Pin(14))
green = PWM(Pin(12))
red = PWM(Pin(13))

#create an function for one color with one parameter
#we will use the PWM from the previous example for setting the brightness 
def single(led):
    for fade in range(0,1024):
        #set the brightness of the LED using duty()
        led.duty(fade)
        time.sleep_ms(3) #wait for 3 milliseconds
        
    for fade in range(1023,-1, -1):
        led.duty(fade)
        time.sleep_ms(3)

#create an function for two colours with two parameters
def duo(led1, led2):
    for fade in range(0,1024):
        #set the brightness of the LED using duty()
        led1.duty(fade)
        led2.duty(fade)
        time.sleep_ms(3) #wait for 3 milliseconds
        
    for fade in range(1023,-1, -1):
        led1.duty(fade)
        led2.duty(fade)
        time.sleep_ms(3)

#create an function for two colours with two parameters 
def all(led1, led2, led3):
    for fade in range(0,1024):
        #set the brightness of the LED using duty()
        led1.duty(fade)
        led2.duty(fade)
        led3.duty(fade)
        time.sleep_ms(3)#wait for 3 milliseconds
        
    for fade in range(1023,-1, -1):
        led1.duty(fade)
        led2.duty(fade)
        led3.duty(fade)
        time.sleep_ms(3)
        
#turn on the LEDs one by one        
single(red)
single(blue)
single(green)

#turn on LEDs two by two
duo(red, blue)
duo(red, green)
duo(green, blue)

#turn on all 3 LEDs
all(red, blue, green)