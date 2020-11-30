import time
import machine
import utime

#set the mode of the pin used by the buzzer as OUTPUT in PWM structure
buzzer = machine.PWM(machine.Pin(12, machine.Pin.OUT))

# the trigger pin (transmitter) must be set as OUTPUT 
trigg_pin = machine.Pin(0, machine.Pin.OUT)#D3

#the echo pin (receiver) must be set as INPUT
echo_pin = machine.Pin(14, machine.Pin.IN)#D5

while True:
    #set the trigPin to LOW (0) in order to prepare for the next reading
    trigg_pin.value(0)
    utime.sleep_us(2)

    #generate an ultrasound for 10 microseconds then turn off the transmitter
    trigg_pin.value(1)
    utime.sleep_us(10)
    trigg_pin.value(0)

    #the formula for distance d = t*v/2
    #v represents the speed of sound in air (about 0.034 cm/μs)
    #t is the time, the duration of the pulse
    time = machine.time_pulse_us(echo_pin, 1, 29000)
    distance=(time*0.034)/2
    
    print("The distance is {} cm".format(distance))
    if distance < 25.0:
        #creating the beeping effect
        #turn on the buzzer using duty() and wait 50 ms
        buzzer.duty(500)
        utime.sleep(0.05)
        
        #turn off the buzzer and wait 50 m
        buzzer.deinit()
        utime.sleep(0.5)
        
    else:
        #turn off the buzzer
        buzzer.deinit()
    
    #wait for 0.1s
    utime.sleep_us(1)