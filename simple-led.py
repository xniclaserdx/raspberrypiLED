import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.OUT) # replace 13 with the designated port

lightLED(3)

def lightLED(e):
    x=0
    while(x<e):
        GPIO.output(13, GPIO.HIGH)  # replace 13 with the designated port
        time.sleep(.1)
        GPIO.output(13, GPIO.LOW)   # replace 13 with the designated port
        time.sleep(.1)
        x=+1

