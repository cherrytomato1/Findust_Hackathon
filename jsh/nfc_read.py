#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


try:
    while 1:
        id,text= reader.read()
        print(id)
        print(text)
        time.sleep(1)
        
finally:
    GPIO.cleanup()