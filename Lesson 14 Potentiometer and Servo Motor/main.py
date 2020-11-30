#use these libraries to declare used pins and PWM
from machine import Pin, ADC, PWM
#for delay
from time import sleep

#use the ADC pin for read values between 0 and 1024 who is generated from potentiometer
pot = ADC(0)

#define the pin as OUTPUT and the PWM of the servo 
servo = PWM(Pin(5, Pin.OUT) , freq = 100)


#for board execute the instructions continuously we make an infinite loop
while True:
  #declare a new variable where we read from ADC pin (A0)
  pot_value = pot.read()
  
  #send the value to servo motor 
  servo.duty(pot_value)