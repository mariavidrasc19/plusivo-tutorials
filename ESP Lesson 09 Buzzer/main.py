import time
from machine import Pin, PWM

#set the mode of the pin and declare as a PWM
buzzer = PWM(Pin(12, Pin.OUT))

#turn on the buzzer and wait 1s
#set the frequency of 1000Hz
buzzer.freq(1000)

#change the sound using duty cycle
buzzer.duty(500)
time.sleep(1)

#deinit() function turn off the buzzer
buzzer.deinit()


buzzer.duty(400)
time.sleep(1)

buzzer.deinit()