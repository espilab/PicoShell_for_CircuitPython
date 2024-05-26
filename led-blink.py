# ここにコードを書いてね :-)
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    print("on ",end="")
    time.sleep(0.20)
    led.value = False
    print("off ",end="")
    time.sleep(0.2)
