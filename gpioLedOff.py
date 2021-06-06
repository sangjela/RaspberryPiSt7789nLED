#GPIO #18 LED ON/OFF
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
LED = 12
#GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, False)
