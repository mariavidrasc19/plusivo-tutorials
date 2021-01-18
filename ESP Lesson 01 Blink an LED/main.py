from time import sleep
from machine import Pin

#the variable "LED" stores the pin used by the LED
#Parameters for Pin:
#first parameter can be one of the 9 available on the board (from D0-D8)
#15 represents GPIO15 as D8 on the board
#second parameter Pin.OUT set variable LED as OUTPUT
LED = Pin(15, Pin.OUT) 

#the int variable "delayTime" stores the time (in this case in seconds) between the blinks
delayTime = 1

#in order to turn on/off the LED, you have to use the value
# 0 for HIGH and 1 for LOW

#the next two instructions are used to turn off the LED and wait for 1 second
LED.value(0)
sleep(1)
 
#the next two instructions are used to turn on the LED and wait for 1 secon
LED.value(1)
sleep(1)