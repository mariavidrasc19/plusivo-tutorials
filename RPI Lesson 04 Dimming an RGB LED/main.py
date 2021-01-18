from time import sleep #we import the sleep module from the time library
import RPi.GPIO as GPIO #we import the RPi.GPIO library with the name of GPIO

GPIO.setmode(GPIO.BOARD) #we set the pin numbering to the GPIO.BOARD numbering
                         #for more details check the guide attached to this code

GPIO.setup(8, GPIO.OUT) #we set the PIN8 as a output pin
GPIO.setup(10, GPIO.OUT) #we set the PIN10 as a output pin
GPIO.setup(12, GPIO.OUT) #we set the PIN12 as a output pin

redPWM = GPIO.PWM(8, 1000) #we create a PWM instance on the 8th pin that is set as
                           #an output.
greenPWM = GPIO.PWM(10, 1000) #we create a PWM instance on the 10th pin that is set as
                              #an output.
bluePWM = GPIO.PWM(12, 1000) #we create a PWM instance on the 12th pin that is set as
                             #an output.

#we start the pwm pins with a duty cycle of 0. This means that at first the pins
#have an output of a digital 0.
redPWM.start(0)
greenPWM.start(0)
bluePWM.start(0)

def single(ledPin):
        #the next for loop will change the duty cycle
        #of the LED from 0 to 100, with a delay of 10 ms between
        #the increments
        for i in range(100):
                ledPin.ChangeDutyCycle(i)
                sleep(0.01)

        #the next for loop will change the duty cycle
        #of the LED from 100 to 0, with a delay of 10 ms
        #between iterations
        for i in reversed(range(100)):
                ledPin.ChangeDutyCycle(i)
                sleep(0.01)

def duo(firstLed, secondLed):
        for i in range(100):
                firstLed.ChangeDutyCycle(i)
                secondLed.ChangeDutyCycle(i)
                sleep(0.01)

        for i in reversed(range(100)):
                firstLed.ChangeDutyCycle(i)
                secondLed.ChangeDutyCycle(i)
                sleep(0.01)

def all(firstLed, secondLed, thirdLed):
        for i in range(100):
                firstLed.ChangeDutyCycle(i)
                secondLed.ChangeDutyCycle(i)
                thirdLed.ChangeDutyCycle(i)
                sleep(0.01)

        for i in reversed(range(100)):
                firstLed.ChangeDutyCycle(i)
                secondLed.ChangeDutyCycle(i)
                thirdLed.ChangeDutyCycle(i)
                sleep(0.01)

while True:
        single(redPWM)
        single(bluePWM)
        single(greenPWM)
        duo(redPWM, bluePWM)
        duo(redPWM, greenPWM)
        duo(bluePWM, greenPWM)
        all(bluePWM, redPWM, greenPWM)

#for a clean ending of the program we will use the next instruction
#to clean all the used ports
#these ports will go back to input mode
GPIO.cleanup()

#NOTE! The duty cycle in the GPIO library is represented with numbers from 0 to 100. At 0 the PIN
#has no output and at 100 the PIN is a digital 1.
#The GPIO.PWM method requires 2 arguments. The first is the previously set PIN, and the second
#the frequency at which the pin works.