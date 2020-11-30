#use these libraries to declare used pins and PWM
from machine import Pin, PWM
#for delay
from time import sleep

#define the pine used by the button
#also initialise the button as INPUT, PULL_UP 
button = Pin(5, Pin.IN, Pin.PULL_UP) #D1
#define the pin as OUTPUT and the PWM of the buzzer 
buzzer = PWM(Pin(12, Pin.OUT) , freq = 500)

#for board execute the instructions continuously we make an infinite loop
while True:
    # read the current state of the button
    #if the button is pressed, turn on the buzzer
    if button.value() == 0:
        #we use a frequency of 1kHz(1000Hz)
        #you can change this frequency so the sound can be
        #more pleasant
        buzzer.duty(1000)
    #if the button is pushed down, we need something
    #to keep the loop() function from running
    elif button.value():
        #if we leave the while with no instructions to do
        #the board will crash, because it will stay too long
        #in a while loop and other processes will not be able to run
        buzzer.deinit()