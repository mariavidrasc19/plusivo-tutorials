"""
 * Credits: www.plusivo.com
 *
 * Lesson 7: RGB LED and Ultrasonic
 *
 * The code below is created for the lesson RGB LED and Ultrasonic and
 * combines two lessons: lesson RGB LED and lesson Ultrasonic HC-SR04+.
 *
 * The code below uses an ultrasonic module to measure the distance
 * and when the distance is less than 25 cm, the red LED will
 * flash quickly, otherwise, the green LED will slowly flash.
 *
 * More information about the connections can be found in the guide.
 *
 """

#import the libraries used
import time
import RPi.GPIO as GPIO

#we will set the pin numbering to the GPIO.BOARD numbering
GPIO.setmode(GPIO.BOARD)

#define the pins used by the ultrasonic module and the RGB Led
trig = 16
echo = 18
redled = 8
greenled = 10
blueled = 12

#set the trigger pin as OUTPUT and the echo as INPUT
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

#set the pins for the led as OUTPUT
GPIO.setup(redled, GPIO.OUT)
GPIO.setup(greenled, GPIO.OUT)
GPIO.setup(blueled, GPIO.OUT)

def calculate_distance():
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

    #return the distance
    return distance

try:
    while True:
        if calculate_distance() < 25:

            #the next 4 instructions are used
            #to crea the flashing effect
            #turn on the red Led and wait 35 ms
            GPIO.output(redled, GPIO.HIGH)
            time.sleep(0.035)

            #turn off the red Led and wait 35 ms
            GPIO.output(redled, GPIO.LOW)
            time.sleep(0.025)

        else:
            #turn on the green Led and wait 300 ms
            GPIO.output(greenled, GPIO.HIGH)
            time.sleep(0.3)

            #turn off the green Led and wait 200 ms
            GPIO.output(greenled, GPIO.LOW)
            time.sleep(0.2)

except KeyboardInterrupt:
    pass

#clean all the used ports
GPIO.cleanup()