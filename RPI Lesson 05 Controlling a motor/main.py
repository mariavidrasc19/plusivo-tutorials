
#we will import the sleep module from the time library
from time import sleep
#we will import the RPi.GPIO library with the name of GPIO
import RPi.GPIO as GPIO

#we will set the pin numbering to the GPIO.BOARD numbering
#for more details check the guide attached to this code
GPIO.setmode(GPIO.BOARD)

#the next variable stores the pin used to control the speed of the motor
motorspeed_pin = 8

#the next two variables store the pins used to control the direction of the motor
DIRA = 10
DIRB = 22

#the variable "delayOn" stores the time (in seconds) for the motor to remain On
delayOn = 3

#the variable "delayOff" stores the time (in seconds) for the motor to remain Off
delayOff = 1.5
#we will set the pins as output
GPIO.setup(motorspeed_pin, GPIO.OUT)
GPIO.setup(DIRA, GPIO.OUT)
GPIO.setup(DIRB, GPIO.OUT)

#the motorspeed_pin will be used as an enable pin on the motor driver
pwmPIN = GPIO.PWM(motorspeed_pin, 100)

#we start the pwm instance with a duty cycle of 0
pwmPIN.start(0)

#define a function to stop the motor
def turnOff():
        #this instruction is used to set the speed of the motor to 0 (Off)
        pwmPIN.ChangeDutyCycle(0)
        #in these instructions the state is irrelevant because the speed is 0
        GPIO.output(DIRA, GPIO.LOW)
        GPIO.output(DIRB, GPIO.LOW)
        sleep(delayOff)

try:
        while True:
                #this instruction is used to set the maximum speed of the motor
                pwmPIN.ChangeDutyCycle(100)
                #these instructions are used to turn on the motor in one direction
                GPIO.output(DIRA, GPIO.HIGH)
                GPIO.output(DIRB, GPIO.LOW)
                sleep(delayOn)

                #turn off the motor
                turnOff()

                #this instruction is used to set the maximum speed of the motor
                pwmPIN.ChangeDutyCycle(100)
                #these instructions are used to turn on the motor in the opposite direction
                GPIO.output(DIRA, GPIO.LOW)
                GPIO.output(DIRB, GPIO.HIGH)
                sleep(delayOn)

                #turn off the motor
                turnOff()

                #this instruction sets the motor speed to about 50%
                pwmPIN.ChangeDutyCycle(50)
                #these instructions are used to turn on the motor in one direction
                GPIO.output(DIRA, GPIO.HIGH)
                GPIO.output(DIRB, GPIO.LOW)
                sleep(delayOn)

                #turn off the motor
                turnOff()

                #this instruction sets the motor speed to about 50%
                pwmPIN.ChangeDutyCycle(50)
                #these instructions are used to turn on the motor in the opposite direction
                GPIO.output(DIRA, GPIO.LOW)
                GPIO.output(DIRB, GPIO.HIGH)
                sleep(delayOn)

                #turn off the motor
                turnOff()

except KeyboardInterrupt:
        pass

#clean all the used ports
GPIO.cleanup()