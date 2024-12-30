from microbit import *
import random

# Initialize snake and food
snake = [(2, 2)]  # Snake starts at the center
direction = (0, 1)  # Initial direction (moving down)
food = (random.randint(0, 4), random.randint(0, 4))

def generate_food():
    while True:
        new_food = (random.randint(0, 4), random.randint(0, 4))
        if new_food not in snake:
            return new_food

while True:
    # Clear the display
    display.clear()
    
    # Display the snake
    for segment in snake:
        display.set_pixel(segment[0], segment[1], 9)
    
    # Display the food
    display.set_pixel(food[0], food[1], 5)
    
    # Read accelerometer values to determine direction
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    
    if x < -300:
        direction = (-1, 0)  # Move left
    elif x > 300:
        direction = (1, 0)  # Move right
    elif y < -300:
        direction = (0, -1)  # Move up
    elif y > 300:
        direction = (0, 1)  # Move down
    
    # Calculate new head position with wrapping
    head_x, head_y = snake[0]
    new_head = (
        (head_x + direction[0]) % 5,  # Wrap horizontally
        (head_y + direction[1]) % 5   # Wrap vertically
    )
    
    # Check for collisions with itself
    if new_head in snake:
        display.show(Image.SAD)
        sleep(2000)
        snake = [(2, 2)]  # Reset snake
        direction = (0, 1)  # Reset direction
        food = generate_food()
        continue
    
    # Add new head to the snake
    snake.insert(0, new_head)
    
    # Check if the snake eats food
    if new_head == food:
        food = generate_food()  # Generate new food
    else:
        snake.pop()  # Remove the tail to maintain snake length
    
    # Small delay to control game speed
    sleep(300)

