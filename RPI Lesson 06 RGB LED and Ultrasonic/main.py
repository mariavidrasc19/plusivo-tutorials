"""
 * Credits: www.plusivo.com
 *
 * Lesson 6: Ultrasonic HC-SR04+
 *
 * The code below uses an ultrasonic module to measure
 * the distance.
 *
 * This module can work with voltages as low as 3V and up to 5.5V,
 * so we do not need an additional power supply and
 * neither a shift level.
 *
 * The module is powered by the development board.
 *
 * For further information, check the guide.
 *
 """
#import the libraries used
import time
import RPi.GPIO as GPIO

#we will set the pin numbering to the GPIO.BOARD numbering
GPIO.setmode(GPIO.BOARD)
trig = 16
echo = 18

#set the trigger pin as OUTPUT and the echo as INPUT
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
#set the trigger to HIGH
GPIO.output(trig, GPIO.HIGH)

#sleep 0.00001 s and the set the trigger to LOW
time.sleep(0.00001)
GPIO.output(trig, GPIO.LOW)

#save the start and stop times
start = time.time()
stop = time.time()

#modify the start time to be the last time until
#the echo becomes HIGH
while GPIO.input(echo) == 0:
       start = time.time()

#modify the stop time to be the last time until
#the echo becomes LOW
while  GPIO.input(echo) == 1:
       stop = time.time()

#get the duration of the echo pin as HIGH
duration = stop - start

#calculate the distance
distance = 34300/2 * duration

#the reading can be erroneous, and we will print
#the distance only if it is lower than the specified value
if distance < 3400:
       #display the distance in console
       print ("Distance = %.2f" % distance)