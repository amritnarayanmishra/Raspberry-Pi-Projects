import RPi.GPIO as GPIO
import time

RED = 17
YELLOW = 27
GREEN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

try:
    while True:
        GPIO.output(RED, True)
        time.sleep(3)
        GPIO.output(RED, False)

        GPIO.output(GREEN, True)
        time.sleep(3)
        GPIO.output(GREEN, False)

        GPIO.output(YELLOW, True)
        time.sleep(1)
        GPIO.output(YELLOW, False)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program stopped, GPIO cleaned up")
