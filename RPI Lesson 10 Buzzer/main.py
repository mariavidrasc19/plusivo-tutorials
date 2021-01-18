"""
*   Credits: www.plusivo.com
*
*   Lesson 10: Buzzer
*
*   The code below is created for the lesson "Buzzer"
*   where you will learn how to use a buzzer.
*
*   Make sure you connected the buzzer correctly, as shown in the guide.
*
*   In this code we will turn on the buzzer, at a frequency of 1000Hz,
*   for one second, and then turn it off for one second, then turn it back on,
*   at a frequency of 500Hz, for one second, and then turn it off for
*   one second, and the code will do these instructions over and over again.
*
*   Before you run the code, do not forget to start the pigpiod daemon
*   using "sudo pigpiod".
*
*   More information about the connections can be found in the guide.
*
"""

#import the libraries used
import time
import pigpio

#create an instance of the pigpio library
pi = pigpio.pi()

#define the pin used by the Buzzer
#this is GPIO18, which is pin 12
buzzer = 18

try:
    while True:
        #start for 2 seconds the pwm on the specified pin with a frequency of
        #500 Hz and with 50% duty cycle
        pi.hardware_PWM(buzzer, 50, 5000)
        time.sleep(2)

        #stop the pwm wave for 2 seconds
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(2)

        #start for 2 seconds the pwm on the specified pin with a frequency of
        #1000Hz and with 50% duty cycle
        pi.hardware_PWM(buzzer, 1000, 50000)
        time.sleep(2)

        #stop the pwm wave for 2 seconds
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(2)

except KeyboardInterrupt:
    pass

#stop the pwm signal
pi.hardware_PWM(buzzer, 0, 0)