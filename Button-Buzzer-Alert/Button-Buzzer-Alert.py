import RPi.GPIO as GPIO
import time

BUZZER = 17
BUTTON = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(BUTTON) == GPIO.HIGH:
            GPIO.output(BUZZER, True)
        else:
            GPIO.output(BUZZER, False)
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program stopped, GPIO cleaned up")
