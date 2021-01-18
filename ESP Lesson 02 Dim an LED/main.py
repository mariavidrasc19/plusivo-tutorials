#use these libraries to declare used pins and PWM
from machine import Pin, PWM
#for delay
from time import sleep

#first, define the pins used by the led
LED = Pin(12, Pin.OUTPUT) #D6
#and the pwm for led
pwm = PWM(LED)

#for board execute the instructions continuously we make an infinite loop
while True:
    #PWM is generated using 10 bits, so it ranges between
    #0 and 1023 (2^10 = 1024)
    for fade in range(0, 1024):
        #set the brightness of the LED using duty cycle
        pwm.duty(fade)
        #wait 0.005 seconds
        sleep(0.005)
    #keep the LED at the maximum brightness for 500 ms  
    sleep(0.05)
    
    #we reduce the intensity of the led
    for fade in range(1024, -1, -1):
        #set the brightness of the LED using duty cycle
        pwm.duty(fade)
        #wait 0.005 seconds
        sleep(0.005)