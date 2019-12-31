import RPi.GPIO as GPIO
import dht11
import time
import datetime
import pyrebase

config = {
  "apiKey": "AIzaSyC3pzCqiD9fovRiPX2PEoWAOfsuhaaiYPc",
  "authDomain": "temphumi69.firebaseapp.com",
  "databaseURL": "https://temphumi69.firebaseio.com/",
  "storageBucket": "temphumi69.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
instance = dht11.DHT11(pin=4)

while True:
    result = instance.read()
    if result.is_valid():      
        data = {"temp": result.temperature,
                "humi": result.humidity
        }
        db.child("data").update(data)

GPIO.cleanup()
