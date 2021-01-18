"""
*   Credits: www.plusivo.com
*
*   The code below is created for the lesson "Play songs with a buzzer"
*   where you will learn how to create simple songs and play them
*   using a buzzer.
*
*   If you know the frequencies of the notes and have a good musical ear,
*   you can compose more complicated songs.
*
*   Make sure you connected the buzzer correctly, as shown in the guide.
*
*   More information about the connection can be found in the guide.
"""
#import the libraries used
import pigpio
import time
import RPi.GPIO as GPIO
import array

#create an instance of the pigpio library
pi = pigpio.pi()

#define the frequencies of the notes
#for all the 7 octaves
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

#define the pin used by the buzzer
#this is GPIO18, which is pin 12
buzzer = 18

#set the pin used by the buzzer as OUTPUT
pi.set_mode(buzzer, pigpio.OUTPUT)

#define the pins used by the buttons
#these are pin numbers
button1 = 24 #pin 18 in BOARD mode
button2 = 8 #pin 24 in BOARD mode

#set the pins for the buttons as INPUT, and we will
#set the initial value to On, or we can say that will be pulled up
pi.set_pull_up_down(button1, pigpio.PUD_UP)
pi.set_pull_up_down(button2, pigpio.PUD_UP)

#when calling this function, the buzzer will
#play the ABC Alphabet song
def abc_song():
    #define the waiting times
    delay1 = 0.7
    delay2 = 1
    delay3 = 0.3
    delay4 = 0.1

    #play every note indicated for delay1 (or delay2, or delay3)
    #seconds, then turn off the buzzer for delay4 seconds
    #then play the next note

    #first sequence
    #play: C C G G A A G
    #create two arrays: one that stores the notes in order and
    #another that stores the playing time for each note
    sequence_1_notes = array.array('i', [c7, c7, g7, g7, a7, a7, g7])
    sequence_1_delays = array.array('f', [delay1, delay1, delay1, delay1, delay1, delay1, delay2])

    #using the for loop we will play all the notes in the correct
    #order
    for i in range(0,7):
        #play "i" note
        pi.hardware_PWM(buzzer, sequence_1_notes[i], 500000)
        #time for playing the "i" note
        time.sleep(sequence_1_delays[i])
        #turn off the buzzer
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(delay4)

    #second sequence
    #play: F F E E D D D D C
    sequence_2_notes = array.array('i', [f7, f7, e7, e7, d7, d7, d7, d7, c7])
    sequence_2_delays = array.array('f', [delay1, delay1, delay1, delay1, delay3, delay3, delay3, delay3, delay2])

    for i in range(0,9):
        pi.hardware_PWM(buzzer, sequence_2_notes[i], 500000)
        time.sleep(sequence_2_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(delay4)

    #third sequence
    #play: G G F E E D
    sequence_3_notes = array.array('i', [g7, g7, f7, e7, e7, d7])
    sequence_3_delays = array.array('f', [delay1, delay1, delay2, delay1, delay1, delay2])

    for i in range(0,6):
        pi.hardware_PWM(buzzer, sequence_3_notes[i], 500000)
        time.sleep(sequence_3_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(delay4)

    #fourth sequence
    #play: G G G F E E D
    sequence_4_notes = array.array('i', [g7, g7, g7, f7, e7, e7, d7])
    sequence_4_delays = array.array('f', [delay3, delay3, delay3, delay2, delay1, delay1, delay2])

    for i in range(0,7):
        pi.hardware_PWM(buzzer, sequence_4_notes[i], 500000)
        time.sleep(sequence_4_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(delay4)

    #fifth sequence
    #play: C C G G A A G
    sequence_5_notes = array.array('i', [c7, c7, g7, g7, a7, a7, g7])
    sequence_5_delays = array.array('f', [delay1, delay1, delay1, delay1, delay1, delay1, delay2])

    for i in range(0,7):
        pi.hardware_PWM(buzzer, sequence_5_notes[i], 500000)
        time.sleep(sequence_5_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(delay4)

    #sixth sequence
    #play: F F E E D D C
    sequence_6_notes = array.array('i', [f7, f7, e7, e7, d7, d7, c7])
    sequence_6_delays = array.array('f', [delay1, delay1, delay1, delay1, delay1, delay1, delay2])

    for i in range(0,7):
        pi.hardware_PWM(buzzer, sequence_6_notes[i], 500000)
        time.sleep(sequence_6_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(delay4)

#when calling this function, the buzzer will
#play the Old Mcdonald had a farm song
def old_mcdonald():
    #play every note indicated for time1 (or time2,
    #or time3, or time4, or time5) seconds,
    #then turn off the buzzer for time0 seconds
    #then play the next note
    time0 = 0.1
    time1 = 0.3
    time2 = 0.6
    time3 = 0.9
    time4 = 0.55
    time5 = 0.2

    #first part
    #play: C C C G A A G
    sequence_1_notes = array.array('i', [c4, c4, c4, g3, a4, a4, g3])
    sequence_1_delays = array.array('f', [time1, time1, time1, time1, time1, time1, time2])

    for i in range(0,7):
        pi.hardware_PWM(buzzer, sequence_1_notes[i], 500000)
        time.sleep(sequence_1_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(time0)

    #second part
    #play: E E D D C
    sequence_2_notes = array.array('i', [e4, e4, d4, d4, c4])
    sequence_2_delays = array.array('f', [time1, time1, time1, time1, time3])

    for i in range(0,5):
        pi.hardware_PWM(buzzer, sequence_2_notes[i], 500000)
        time.sleep(sequence_2_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(time0)

    #third part
    #play: G C C C G A A G
    sequence_3_notes = array.array('i', [g3, c4, c4, c4, g3, a4, a4, g3])
    sequence_3_delays = array.array('f', [time4, time1, time1, time1, time4, time1, time1, time2])

    for i in range(0,8):
        pi.hardware_PWM(buzzer, sequence_3_notes[i], 500000)
        time.sleep(sequence_3_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(time0)

    #fourth part
    #play: E E D D C
    sequence_4_notes = array.array('i', [e4, e4, d4, d4, c4])
    sequence_4_delays = array.array('f', [time1, time1, time1, time1, time3])

    for i in range(0,5):
        pi.hardware_PWM(buzzer, sequence_4_notes[i], 500000)
        time.sleep(sequence_4_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(time0)

    #fifth part
    #play: G G C C C G G C C C
    sequence_5_notes = array.array('i', [g3, g3, c4, c4, c4, g3, g3, c4, c4, c4])
    sequence_5_delays = array.array('f', [time5, time5, time1, time1, time1, time5, time5, time1, time1, time2])

    for i in range(0,10):
        pi.hardware_PWM(buzzer, sequence_5_notes[i], 500000)
        time.sleep(sequence_5_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(time0)

    #sixth part
    #play: C C C C C C C C C C C C
    sequence_6_notes = array.array('i', [c4])
    sequence_6_delays = array.array('f', [time5, time5, time1, time5, time5, time1, time5, time5, time5, time5, time1, time1])

    for i in range(0,12):
        pi.hardware_PWM(buzzer, sequence_6_notes[0], 500000)
        time.sleep(sequence_6_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(time0)

    #seventh part
    #play: C C C G A A G
    sequence_7_notes = array.array('i', [c4, c4, c4, g3, a4, a4, g3])
    sequence_7_delays = array.array('f', [time1, time1, time1, time1, time1, time1, time2])

    for i in range(0,7):
        pi.hardware_PWM(buzzer, sequence_7_notes[i], 500000)
        time.sleep(sequence_7_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(time0)

    #eight part
    #play: E E D D C
    sequence_8_notes = array.array('i', [e4, e4, d4, d4, c4])
    sequence_8_delays = array.array('f', [time1, time1, time1, time1, time3])

    for i in range(0,5):
        pi.hardware_PWM(buzzer, sequence_8_notes[i], 500000)
        time.sleep(sequence_8_delays[i])
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(time0)


try:
    while True:
        #if the first button was pressed, play the first song
        if pi.read(button1) == 0:
            #play ABC Alphabet song
            abc_song()

        #if the second button was pressed, play the second song
        if pi.read(button2) == 0:
            #play the second song
            old_mcdonald()

except KeyboardInterrupt:
    pass

#turn off the buzzer
pi.write(buzzer, 0)
#stop the connection with the daemon
pi.stop()