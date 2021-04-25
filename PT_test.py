# PT_Test.py - Test Pan and Tilt Servo's
#
# 18 February 2017

import RPi.GPIO as GPIO
from RS_Servo import Servo

# create new servo's to be controlled from GPIO pins 5 & 6
pan_servo = Servo(5, 3, 11)    
tilt_servo = Servo(6, 2, 11)

# start PWM for servo's
pan_servo.start()
tilt_servo.start()

print(pan_servo)
print(tilt_servo)
print("Servo instances: ", Servo.count())

try:
    while True:
        print("\nScanning (CTRL c to exit)...")
        pan_servo.scan()
        tilt_servo.scan()
except KeyboardInterrupt:
    print("\n-- CTRL-C: Terminating program --")
finally:
    print("Cleaning up PWM and GPIO...")
    pan_servo.cleanup()
    tilt_servo.cleanup()
    GPIO.cleanup()
    print("Done.")


