from microbit import *
import time

# Set light level thresholds
LOW_LIGHT_THRESHOLD = 30  # Below this level, consider the environment dark
HIGH_LIGHT_THRESHOLD = 200  # Above this level, consider the environment bright

# Function to check light level and give an alert
def check_light_level(light_level):
    if light_level < LOW_LIGHT_THRESHOLD:
        display.scroll("It's Dark", delay=100)
        display.show(Image.SAD)
    elif light_level > HIGH_LIGHT_THRESHOLD:
        display.scroll("It's Bright", delay=100)
        display.show(Image.HAPPY)
    else:
        display.show(Image.ASLEEP)

while True:
    # Read the current light level (0-255)
    light_level = display.read_light_level()

    # Show the light level on the display
    display.scroll(str(light_level), delay=100)
    
    # Check the light level and give an alert if it crosses a threshold
    check_light_level(light_level)
    
    # Small delay before the next light reading
    time.sleep(2000)  # Wait for 2 seconds before taking the next reading
