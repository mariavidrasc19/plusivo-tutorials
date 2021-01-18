#we import the sleep module from the time library
from time import sleep
#we import the RPi.GPIO library with the name of GPIO
import RPi.GPIO as GPIO

#we set the pin numbering to the GPIO.BOARD numbering
#for more details check the guide attached to this code
GPIO.setmode(GPIO.BOARD)

#we set the PIN8 as an output pin
GPIO.setup(8, GPIO.OUT)

#we start a loop that never ends
while True:
        #we change the digital output on the 8th pin to a high voltage
        #the LED starts
        GPIO.output(8, GPIO.HIGH)

        #wait one second
        sleep(1)

        #we change the digital output on the 8th pin to a low voltage
        #the LED stops
        GPIO.output(8, GPIO.LOW)

        #wait one second
        sleep(1)
#NOTE! In place of the GPIO.HIGH and GPIO.LOW we can use 1 and respectivelly 0, but we will keep
#the GPIO.HIGH notation for the purpose of this tutorial to be easier to understand.