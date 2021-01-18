from time import sleep #we import the sleep module from the time library
import RPi.GPIO as GPIO #we import the RPi.GPIO library with the name of GPIO

GPIO.setmode(GPIO.BOARD) #we set the pin numbering to the GPIO.BOARD numbering
                         #for more details check the guide atached to this code

GPIO.setup(8, GPIO.OUT) #we set the PIN8 as a output pin

pwmPIN = GPIO.PWM(8, 1000)  #we create a PWM instance on the 8th pin that is set as
                            #an output

pwmPIN.start(0) #we start the pwm pin with a duty cycle of 0. This means that at first the pin
                #has an output of a digital 0

while True: #we start a loop that never ends in which we modify the duty cycle from 0 to 100
            #and back. This will make the LED change it's light intensity
        for i in range(1000): #for an index i which gets the values from 0 to 100 we change the
                             #duty cycle.
                pwmPIN.ChangeDutyCycle(i)
                sleep(0.2) #We wait 1 seconds(10 milliseconds) between the cycle changes
                            #to make the light intensity change visible.
        for i in reversed(range(1000)): #we do the same thing but going from 100 to 0.
                pwmPIN.ChangeDutyCycle(i)
                sleep(0.2)

#NOTE! The duty cycle in the GPIO library is represented with numbers from 0 to 100. At 0 the PIN
#has no output and at 100 the PIN is a digital 1.
#The GPIO.PWM method requires 2 arguments. The first is the previously set PIN, and the second
#the frequency at which the pin works.