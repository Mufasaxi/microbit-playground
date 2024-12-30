from microbit import *
import time

# Initialize step count
step_count = 0

# Sensitivity threshold for detecting a step
threshold = 200

# Store the last accelerometer reading
last_accel = 0

while True:
    # Get the current acceleration (magnitude) from the accelerometer
    current_accel = accelerometer.get_x()

    # Check if the change in acceleration is above the threshold
    if abs(current_accel - last_accel) > threshold:
        step_count += 1  # Increase step count
        display.show(str(step_count))  # Display the step count

    # Update the last accelerometer reading
    last_accel = current_accel

    # Reset step count when Button A is pressed
    if button_a.is_pressed():
        step_count = 0
        display.show("0")  # Display "0" to indicate reset

    # Wait a little bit before checking again
    time.sleep(200)
