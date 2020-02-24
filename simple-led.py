import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.OUT)

lightLED(3)

def lightLED(e):
    x=0
    while(x<e):
        GPIO.output(13, GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(13, GPIO.LOW)
        time.sleep(.1)
        x=+1

