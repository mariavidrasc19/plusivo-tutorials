"""
*   Credits: www.plusivo.com
*
*   Lesson 17: Control an LED from web
*
*   The code below is created for the lesson "Control an LED from web"
*   where you will host a simple website.
*
*   Also we defined a new function to control the led.
*
"""

#import the necessary modules from the bottle library
from bottle import route, run, template, request
#we will import the RPi.GPIO library with the name of GPIO
import RPi.GPIO as GPIO

#we will set the pin numbering to the GPIO.BOARD numbering
GPIO.setmode(GPIO.BOARD)

#define the pin used by the Led
led_pin = 8

#set the pin used by the Led as OUTPUT
GPIO.setup(led_pin, GPIO.OUT)

#define the route for the main page
@route('/')
def index():
    #at the '/' route we will return the index.html
    #template that is in the views folder
    return template('index.html')

@route('/led', method = 'POST')
def func():
    #request data from web page
    state = request.POST.get('state')

    #if the value returned is "On", we will turn On the LED
    #else, we will turn Off the LED
    if state == 'On':
        #turn On the Led
        GPIO.output(led_pin, GPIO.HIGH)
    else:
        #turn off the Led
        GPIO.output(led_pin, GPIO.LOW)

    #send a message to the user
    return 'ok'

#we will run the app on port 5000
run(host = '0.0.0.0', port = '5000')
