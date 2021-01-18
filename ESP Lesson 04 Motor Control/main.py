#use these libraries to declare used pins and PWM
from machine import Pin, PWM
#for delay
from time import sleep

#define the pins used by motror for speed control
motorspeed_pin = Pin(14, Pin.OUT)
#and the pwm for motror speed control
pwm = PWM(motorspeed_pin)

#we define pins used by motror for its direction and also initialise it as OUTPUT
DIRA = Pin(12, Pin.OUT) #D6
DIRB = Pin(13, Pin.OUT) #D7

#waiting time
delayOn = 2
delayOff = 3

def turnOff ():
    #this instruction is used to set the speed of the motor to 0 (off)
    motorspeed_pin.off()
    #in these instructions the state is irrelevant because the motor is off
    DIRA.off()
    DIRB.off()
    #wait 3 seconds
    sleep(delayOff)

#for board execute the instructions continuously we make an infinite loop
while True:
    #this instruction is used to set the maximum speed of the motor
    motorspeed_pin.on()
    #these instructions are used to turn on the motor in one direction
    DIRA.on()
    DIRB.off()
    #wait 2 seconds
    sleep(delayOn)
    
    #turn off the motor
    turnOff()
    
    #this instruction is used to set the maximum speed of the motor
    motorspeed_pin.on()
    #these instructions are used to turn on the motor in the opposite direction
    DIRA.off()
    DIRB.on()
    #wait 2 seconds
    sleep(delayOn)
    
    #turn off the motor
    turnOff()
    
    #this instruction sets the motor speed to about 50%, for this we use the PWM duty cycle
    #you can put any integer from 0 to 1023
    pwm.duty(512)
    #these instructions are used to turn on the motor in one direction
    DIRA.on()
    DIRB.off()
    #wait 2 seconds
    sleep(delayOn)
    
    #turn off the motor
    turnOff()
    
    #this instruction sets the motor speed to about 50%, for this we use the PWM duty cycle
    #you can put any integer from 0 to 1023
    pwm.duty(512)
    #these instructions are used to turn on the motor in the opposite direction
    DIRB.on()
    DIRA.off()
    #wait 2 seconds
    sleep(delayOn)
    
    #turn off the motor
    turnOff()
