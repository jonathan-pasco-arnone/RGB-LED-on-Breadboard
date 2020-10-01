# Creator: Jonathan P-A
# Date: September 30
# This program makes an RGB LED turn on for 1 second and then off for 1 second repetedly
import time
import board
from digitalio import DigitalInOut, Direction

ledi = DigitalInOut(board.D1)
ledii = DigitalInOut(board.D2)
lediii = DigitalInOut(board.D3)
ledi.direction = Direction.OUTPUT
ledii.direction = Direction.OUTPUT
lediii.direction = Direction.OUTPUT

while True:
    ledi.value = True
    ledii.value = True
    lediii.value = True
    time.sleep(1)#wait 1 second
    ledi.value = False
    ledii.value = False
    lediii.value = False
    time.sleep(1)#wait 1 second