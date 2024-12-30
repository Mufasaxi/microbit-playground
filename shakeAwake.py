from microbit import *

while True:
    if accelerometer.was_gesture("shake"):
        display.show(Image.SURPRISED)
        sleep(1000)  # Show the smiley for 1 second
        display.clear()
    else:
        display.show(Image.ASLEEP)
