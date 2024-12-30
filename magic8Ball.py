from microbit import *
import random

responses = [
    "Yes", "No", "Maybe", "Try again", 
    "Definitely", "Unlikely", "Ask later", "Sure!"
]

while True:
    display.show("?")  # Show a question mark when idle
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(500)  # Pause before showing the answer
        display.scroll(random.choice(responses))
