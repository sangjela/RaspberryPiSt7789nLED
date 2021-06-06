#GPIO #12 (PWM0) LED ON/OFF
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
LED = 12
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)

#Param Ch, Frequency
PwmObj = GPIO.PWM(LED, 1000)
PwmObj.ChangeDutyCycle(0) # %on of 1 clock

try:
    while True:
        power = 0
        while power < 100:
            PwmObj.start(power) #power is duty cycle
            sleep(0.01)
            power += 1
        while power > 0:
            PwmObj.start(power)
            sleep(0.01)
            power -= 1
except :
    pass
PwmObj.stop()
GPIO.cleanup()
