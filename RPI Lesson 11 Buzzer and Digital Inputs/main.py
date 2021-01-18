"""
*  Credits: www.plusivo.com
*
*  Lesson 11: Buzzer and Digital Inputs
*
*  The code below is created for the lesson "Buzzer and Digital Inputs"
*  where you will learn how to use a buzzer and a push button.
*
*  Before you run the code, do not forget to start the pigpiod daemon
*  using "sudo pigpiod".
*
*  More information about the connection can be found in the guide.
"""

#import the libraries used
import time
import pigpio

#create an instance of the pigpio library
pi = pigpio.pi()

#define the pin used by the Buzzer
#this pin will be used by the pigpio library
#which takes the pins in GPIO forms
#we will use GPIO18, which is pin 12
buzzer = 18

#set the pin used by the buzzer as OUTPUT
pi.set_mode(buzzer, pigpio.OUTPUT)

#define the pin used by the button
#here we will use the GPIO number
button = 8 #pin 24 in BOARD mode

#set the pins for the buttons as INPUT, and we will
#set the initial value to On, or we can say that will be pulled up
pi.set_pull_up_down(button, pigpio.PUD_UP)

try:
    while True:
        #check if the button was pressed
        while pi.read(button) == 0:
            #turn on the buzzer at a frequency of 500 Hz
            pi.hardware_PWM(buzzer, 500, 500000)

        #check if the button is released
        if pi.read(button) == 1:
            #turn off the buzzer
            pi.hardware_PWM(buzzer, 0, 0)

        #wait 100 ms before next run
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

#stop the PWM signal
pi.write(buzzer, 0)

#stop the connection with the daemon
pi.stop()