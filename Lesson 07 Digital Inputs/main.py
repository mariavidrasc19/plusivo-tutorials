from machine import Pin
import time

#set the pin for LED
led = Pin(13, Pin.OUT)

#create the digital input pin with an internal pull-up resistor
#Pin.IN means the pin will be set as an input that can read high or low levels
#Pin.PULL_UP to enable an internal pull-up resistor on the pin
button_on = Pin(5, Pin.IN, Pin.PULL_UP)
button_off = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    # 0 => pressed
    # 1 => release
    
    #check if the button off is pressed
    if button_on.value() and not button_off.value():
        #turn off the LED
        led.off()
        
    #check if the button on is pressed
    elif button_off.value() and not button_on.value():
        #turn on the LED
        led.on()
        
    #wait for 0.1s (100 ms)
    time.sleep(0.01)