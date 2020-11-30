#use these libraries to declare used pins and PWM
from machine import Pin, PWM
#for delay
from time import sleep

#define the pins used by the buttons and led
#also initialise it as INPUT, PULL_UP and led as OUTPUT
button_down = Pin(5, Pin.IN, Pin.PULL_UP)
button_up = Pin(4,  Pin.IN, Pin.PULL_UP)
led = Pin(13, Pin.OUT)

#declare the pwm for led 
pwm = PWM(led)

#the frequency controls how fast the PWM signal is turned on and off
pwm.freq(1000)
pwm.duty(0)

container = 0

#for board execute the instructions continuously we make an infinite loop
while True:
    #while the down button is pressed
    while button_down.value() == 0:
        #the minimum value for container is 0, so if the
        #value is greater than 50, we can substract 50
        #else, the value will be set to 0
        print('Button down pressed')
        if container > 50:
            #change the value
            container = container - 50
        else:
            #set the value to 0
            container = 0
        
        #turn on the LED
        pwm.duty(container)
        #wait 50 ms before the next run
        sleep(0.1)
        
    #while the up button is pressed
    while button_up.value() == 0: 
        #the maximum value for container is 1023
        #if the value is less than 972, we can add 50
        #otherwise, the container will be set to 1023
        print('Button up pressed')
        if container < 972:
            container = container + 50
        else:
            container = 1023
        
        #turn on the LED
        pwm.duty(container)  # =analogWrite (din arduino)
        #wait 50 ms before the next run
        sleep(0.1)

