"""
 * Credits: www.plusivo.com
 *
 * Lesson 14: DHT11
 *
 * This lesson is created for the lesson "DHT11",
 * where you will learn how to use a DHT11
 * Temperature and Humidity sensor.
 *
 * Do not forget to install the Adafruit_Python_DHT library
 * as shown in the guide!
 *
 * More details can be found in the guide.
 *
 """

#import the libraries
import RPi.GPIO as GPIO
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)

#name the type of sensor used
type = Adafruit_DHT.DHT11

#declare the pin used by the sensor in GPIO form
dht11 = 25

#set the sensor as INPUT
GPIO.setup(dht11, GPIO.IN)

try:
    while True:
        #make the reading
        humidity, temperature = Adafruit_DHT.read_retry(type, dht11)

        #we will display the values only if they are not null
        if humidity is not None and temperature is not None:
            print('Temperature = {:.1f}  Humidity = {:.1f}' .format(temperature, humidity))

except KeyboardInterrupt:
    pass

#clean all the used ports
GPIO.cleanup()