#GPIO #18 LED ON/OFF
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
LED = 18
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)

loop = 1
while loop < 10:
    GPIO.output(LED, True)
    sleep(1)
    GPIO.output(LED, False)
    sleep(1)
    loop += 1
