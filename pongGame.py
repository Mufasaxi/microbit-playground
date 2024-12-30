from microbit import *
import random

# Initialize paddle and ball positions
paddle_left = 2
paddle_right = 2
ball_x = 2
ball_y = 2
ball_dir_x = 1  # Ball's horizontal direction
ball_dir_y = 1  # Ball's vertical direction

# Game speed
game_speed = 300

# Ball speed (can be adjusted)
ball_speed = 1

while True:
    display.clear()
    
    # Display paddles
    display.set_pixel(0, paddle_left, 9)
    display.set_pixel(4, paddle_right, 9)
    
    # Display ball
    display.set_pixel(ball_x, ball_y, 5)
    
    # Read accelerometer values to control paddles
    x = accelerometer.get_x()
    y = accelerometer.get_y()

    # Control left paddle (Player 1) with tilt on the X axis
    if x < -300 and paddle_left > 0:
        paddle_left -= 1
    elif x > 300 and paddle_left < 4:
        paddle_left += 1

    # Control right paddle (Player 2) with tilt on the Y axis
    if y < -300 and paddle_right > 0:
        paddle_right -= 1
    elif y > 300 and paddle_right < 4:
        paddle_right += 1

    # Move the ball
    ball_x += ball_dir_x * ball_speed
    ball_y += ball_dir_y * ball_speed

    # Ball collision with top and bottom walls
    if ball_y == 0 or ball_y == 4:
        ball_dir_y *= -1  # Reverse vertical direction

    # Ball collision with paddles
    if (ball_x == 0 and ball_y == paddle_left) or (ball_x == 4 and ball_y == paddle_right):
        ball_dir_x *= -1  # Reverse horizontal direction

    # Ball goes out of bounds (either left or right side)
    if ball_x == 0 or ball_x == 4:
        # Reset the ball and paddles after a score
        ball_x = 2
        ball_y = 2
        ball_dir_x = random.choice([-1, 1])  # Random horizontal direction
        ball_dir_y = random.choice([-1, 1])  # Random vertical direction
        paddle_left = 2
        paddle_right = 2
        display.show(Image.SAD)
        sleep(1000)
    
    # Small delay to control game speed
    sleep(game_speed)
