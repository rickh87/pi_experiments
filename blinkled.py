import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
counter = 1

while True:
    print (counter)
    GPIO.output(17, True)
    sleep(1)
    GPIO.output(17, False)
    sleep(1)
    counter = counter + 1