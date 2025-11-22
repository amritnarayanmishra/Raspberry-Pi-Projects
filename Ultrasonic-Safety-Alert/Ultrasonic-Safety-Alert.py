import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24
LED1 = 17
LED2 = 27
LED3 = 22
BUZZER = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup([LED1, LED2, LED3, BUZZER, TRIG], GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        GPIO.output(TRIG, False)
        time.sleep(0.5)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
        distance = (pulse_end - pulse_start) * 17150
        distance = round(distance,2)
        print(f"Distance: {distance} cm")

        GPIO.output([LED1, LED2, LED3, BUZZER], False)
        if distance < 10:
            GPIO.output([LED1, BUZZER], True)
        elif distance < 20:
            GPIO.output(LED2, True)
        else:
            GPIO.output(LED3, True)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program stopped")
