import RPi.GPIO as GPIO
import time
from time import sleep
from firebase import firebase

firebase = firebase.FirebaseApplication('https://temphumi69.firebaseio.com/data/')

def controlBoiler():
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(2, GPIO.OUT)
   pwm = GPIO.PWM(2, 50)
   pwm.start(0)
   result = firebase.get('status', None)
   if result == 1:
      pwm.ChangeDutyCycle(7.5)
      time.sleep(1)
      pwm.stop()
      GPIO.cleanup()
   elif result == 0:
      pwm.ChangeDutyCycle(12.5)
      time.sleep(1)
      pwm.stop()
      GPIO.cleanup()
