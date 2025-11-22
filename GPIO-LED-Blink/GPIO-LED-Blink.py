import RPi.GPIO as GPIO
import time

LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, True)
        time.sleep(1)
        GPIO.output(LED_PIN, False)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program stopped, GPIO cleaned up")
