from machine import Pin
from time import sleep
import dht

dht_obj = dht.DHT11(Pin(13))

while True:
    
    try:
        dht_obj.measure()
        sleep(0.02)
        temp = dht_obj.temperature()
        hum = dht_obj.humidity()
        print("tempereature is : ",temp)
        print("humidity is : ",hum)
        sleep(1)
    except OSError as e:
        print("Failed to read dht value")