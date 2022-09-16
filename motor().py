
import board
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
servo1 = GPIO.PWM(17, 60)
GPIO.setup(27, GPIO.OUT)
servo2 = GPIO.PWM(27, 60)

class motor:
    def open(self):  #lock-unlock motor
        servo1.ChangeDutyCycle(7)
        print("unlocked")
        time.sleep(1)
        servo2.ChangeDutyCycle(5)
        print("door opened")
        

    def close(self):
        servo2.ChangeDutyCycle(12)
        print("door closed")
        time.sleep(2)
        servo1.ChangeDutyCycle(12)
        print("locked")
        

while True:
    motor.open()
    time.sleep(2)
    motor.close()
    time.sleep(2)
    break;







