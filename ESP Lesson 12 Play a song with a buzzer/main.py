#use these libraries to declare used pins and PWM
from machine import Pin, PWM
#for delay
from time import sleep

#define the pins used by the buttons
#also initialise the buttons as INPUT, PULL_UP 
button1 = Pin(5, Pin.IN, Pin.PULL_UP) #D1
button2 = Pin(4, Pin.IN, Pin.PULL_UP) #D2
#define the pin as OUTPUT and the PWM of the buzzer 
buzzer = PWM(Pin(12, Pin.OUT) , freq = 500)

#define the frequencies of the notes
#for all the 7 octaves
#these notes have an error because we 
#declared them as integers and not floats
c8 = 4187
b7 = 3951
a7 = 3520
g7 = 3136
f7 = 2794
e7 = 2637
d7 = 2349
c7 = 2093
b6 = 1975
a6 = 1760
g6 = 1568
f6 = 1397
e6 = 1318
d6 = 1174
c6 = 1046
b5 = 988
a5 = 880
g5 = 784
f5 = 698
e5 = 659
d5 = 587
c5 = 523
b4 = 494
a4 = 440
g4 = 392
f4 = 349
e4 = 330
d4 = 293
c4 = 261
b3 = 247
a3 = 220
g3 = 196
f3 = 174
e3 = 165
d3 = 146
c3 = 130
b2 = 123
a2 = 110
g2 = 97
f2 = 87
e2 = 82
d2 = 73
c2 = 65
b1 = 61
a1 = 55
g1 = 49
f1 = 43
e1 = 41
d1 = 37
c1 = 33

#when calling this function, the buzzer will
#play the ABC Alphabet song
def abc_song():
    #define the waiting times
    sleep1 = 0.7
    sleep2 = 0.01
    sleep3 = 0.3
    sleep4 = 0.1
    
    #play every note indicated for delay1 (or delay2, or delay3)
    #milliseconds, then turn off the buzzer for delay4 milliseconds
    #then play the next note
    
    #first sequence
    #play: C C G G A A G
    buzzer.freq(c7)
    sleep(sleep1)
    buzzer.deinit()
    sleep(sleep4)
    
    buzzer.freq(c7)
    sleep(sleep1)
    buzzer.deinit()
    sleep(sleep4)
    
    buzzer.duty(g7)
    sleep(sleep1)
    buzzer.deinit()
    sleep(sleep4)
    
    buzzer.duty(g7)
    sleep(sleep1)
    buzzer.deinit()
    sleep(sleep4)
    
    buzzer.duty(a7)
    sleep(sleep1)
    buzzer.deinit()
    sleep(sleep4)
    
    buzzer.duty(a7)
    sleep(sleep1)
    buzzer.deinit()
    sleep(sleep4)
    
    buzzer.duty(g7)
    sleep(sleep1)
    buzzer.deinit()
    sleep(sleep4)
    
#when calling this function, the buzzer will
#play the Old Mcdonald had a farm song
def old_mcdonald():
    #play every note indicated for time1 (or time2, 
    #or time3, or time4, or time5) milliseconds, 
    #then turn off the buzzer for time0 milliseconds
    #then play the next note
    time0 = 0.1
    time1 = 0.3
    time2 = 0.6
    time3 = 0.9
    time4 = 0.55
    time5 = 0.2

    #first part
    #play: C C C G A A G
    buzzer.freq(c4)
    sleep(time1)
    buzzer.deinit()
    sleep(time0)
    
    buzzer.freq(c4)
    sleep(time1)
    buzzer.deinit()
    sleep(time0)
    
    buzzer.duty(c4)
    sleep(time1)
    buzzer.deinit()
    sleep(time0)
    
    buzzer.duty(g3)
    sleep(time1)
    buzzer.deinit()
    sleep(time0)
    
    buzzer.duty(a4)
    sleep(time1)
    buzzer.deinit()
    sleep(time0)
    
    buzzer.duty(a4)
    sleep(time1)
    buzzer.deinit()
    sleep(time0)
    
    buzzer.duty(g3)
    sleep(time1)
    buzzer.deinit()
    sleep(time0)
    
    
#for board execute the instructions continuously we make an infinite loop
while True:
    # read the current state of the button
    #if the first button is pressed, turn on first song
    if button1.value() == 0:
        #play ABC Alphabet song
        abc_song()
    #if the second button was pressed, play the second song
    elif button2.value() == 0:
        #play the second song
        old_mcdonald()