from time import sleep #we import the sleep module from the time library
import RPi.GPIO as GPIO #we import the RPi.GPIO library with the name of GPIO

GPIO.setmode(GPIO.BOARD) #we set the pin numbering to the GPIO.BOARD numbering
                         #for more details check the guide atached to this code

GPIO.setup(8, GPIO.OUT) #we set the PIN8 as an output pin
GPIO.setup(10, GPIO.OUT) #we set the PIN10 as an output pin
GPIO.setup(12, GPIO.OUT) #we set the PIN12 as an output pin

while True: #we start a loop that never ends
        GPIO.output(8, GPIO.HIGH) #we change the digital output on the 8th pin to a high voltage
                                  #the RED LED starts
        sleep(1) #wait one second
        #GPIO.output(8, GPIO.LOW) #we change the digital output on the 8th pin to a low voltage
                                 #the RED LED stops

        GPIO.output(10, GPIO.HIGH) #we change the digital output on the 10th pin to a high voltage
                                   #the GREEN LED starts
        sleep(1) #wait one second
        #GPIO.output(10, GPIO.LOW) #we change the digital output on the 10th pin to a low voltage
                                  #the GREEN LED stops

        GPIO.output(12, GPIO.HIGH) #we change the digital output on the 12th pin to a high voltage
                                   #the BLUE LED starts
        sleep(1) #wait one second
        #GPIO.output(12, GPIO.LOW) #we change the digital output on the 12th pin to a low voltage
                                  #the BLUE LED stops