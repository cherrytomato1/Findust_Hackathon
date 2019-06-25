import RPi.GPIO as GPIO
import requests
import time
import threading
from operator import eq
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)

reader = SimpleMFRC522()

def open_close():## onopen requests
    basic_time = time.time()## 기준 시간
    nowtime = round(time.time()-basic_time)
    while 1:
        
        if(nowtime > 9):## 10 초에 한번씩 요청
            response2 = requests.get('http://kyu9341.cafe24.com/TestText.php')
            print(response2.text)
            basic_time = time.time()
        
        if(nowtime != round(time.time()-basic_time)):
            print(round(time.time()-basic_time))
            nowtime = round(time.time()-basic_time)
            
def scan_nfc():
    id,text= reader.read()
    print(id)
    print(text)
    data = {'Test':id}
    response = requests.post('http://kyu9341.cafe24.com/TestText.php',data=data)
    time.sleep(1)
    print("scan end")

        
t1 = threading.Thread(target = open_close)
t1.start()

while 1:
    scan_nfc()


