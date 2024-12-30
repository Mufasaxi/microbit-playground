from microbit import *
import time

# Set temperature thresholds (for alert)
LOW_TEMP_THRESHOLD = 15  # Minimum temperature before alert
HIGH_TEMP_THRESHOLD = 30  # Maximum temperature before alert

# Function to check temperature and give an alert
def check_temperature(temp):
    if temp < LOW_TEMP_THRESHOLD:
        display.scroll("LOW TEMP", delay=100)
        display.show(Image.SAD)
    elif temp > HIGH_TEMP_THRESHOLD:
        display.scroll("HIGH TEMP", delay=100)
        display.show(Image.SURPRISED)
    else:
        display.show(Image.HAPPY)

while True:
    # Read the current temperature (in Celsius)
    current_temp = temperature()

    # Show the temperature on the display
    display.scroll(str(current_temp) + "C", delay=100)
    
    # Check if the temperature is above or below the set thresholds
    check_temperature(current_temp)
    
    # Wait a bit before measuring again
    time.sleep(2000)  # 2-second delay before reading the temperature again
