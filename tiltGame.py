from microbit import *
import random

# Initialize player position
player_x = 2
player_y = 2

# Generate random target position
target_x = random.randint(0, 4)
target_y = random.randint(0, 4)

while True:
    # Clear the display and render the player and target
    display.clear()
    display.set_pixel(player_x, player_y, 9)  # Player at full brightness
    display.set_pixel(target_x, target_y, 5)  # Target at medium brightness

    # Read accelerometer values and adjust player position
    x = accelerometer.get_x()
    y = accelerometer.get_y()

    # Map accelerometer tilt to movement
    if x < -200 and player_x > 0:
        player_x -= 1
    if x > 200 and player_x < 4:
        player_x += 1
    if y < -200 and player_y > 0:
        player_y -= 1
    if y > 200 and player_y < 4:
        player_y += 1

    # Check if the player catches the target
    if player_x == target_x and player_y == target_y:
        display.show(Image.HAPPY)
        sleep(1000)

        # Reset the game with a new target position
        target_x = random.randint(0, 4)
        target_y = random.randint(0, 4)
        player_x = 2
        player_y = 2

    sleep(200)  # Small delay for smoother movement
