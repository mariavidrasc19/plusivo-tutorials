#use these libraries to declare used pins
from machine import Pin, PWM
import machine
#for delay
from time import sleep
import time
#utime is an library used for getting the current time and date
#measuring time intervals, and for delays
import utime

#set the mode of the pins used by the RGB LED as OUTPUT
red = Pin(12, Pin.OUT)
green = Pin(13, Pin.OUT)
blue = Pin(15, Pin.OUT)

#set the input to trigger module to send ultrasonic waves
#the trigger pin (transmitter) must be set as OUTPUT
trig_pin = Pin(0, Pin.OUT) #D3

#set he output received representing the reflection of waves
#the echo pin (receiver) must be set as INPUT
echo_pin = Pin(14,  Pin.IN) #D5

#for board execute the instructions continuously we make an infinite loop
while True:
    #set the trigPin to LOW(0) in order to prepare for the next reading
    trig_pin.value(0)
    #delay for 2 microseconds
    utime.sleep_us(2)
    
    #generate an ultrasound for 10 microseconds then turn off the transmitter
    trig_pin.value(1)
    utime.sleep_us(10)
    trig_pin.value(0)

    #find the time using machine.time_pulse_us(pin, pulse_level, timeout_us=1000000)
    #Time a pulse on the given pin, and return the duration of the pulse in microsecond
    # 29000 timeout optional => nr milisecunds witch the pulse have to wait for begin

    time = machine.time_pulse_us(echo_pin, 1)
    
    #the formula for distance d = t*v/2
    #v represents the speed of sound in air (about 0.034 cm/μs)
    #t is the time, the duration of the pulse
    distance=(time*0.034)/2
    
    #display the distance
    print("The distance is {} cm".format(distance))
    
    if distance < 25.0:
        #the next 4 instructions are used
        #to create the flashing effect
        #turn on the LED and wait 35 ms
        red.on()
        sleep(0.035)
        
        red.off()
        sleep(0.035)
    else:
        #turn on the green LED and wait 300 ms
        green.on()
        sleep(0.3)
        
        #turn off the green LED and wait 200 ms
        green.off()
        sleep(0.2)