from microbit import Image, display, sleep

# Get all attributes of the Image class
all_images = [attr for attr in dir(Image) if not callable(getattr(Image, attr)) and not attr.startswith("__")]

# Display each image sequentially
for img_name in all_images:
    # Get the actual Image object using getattr
    img = getattr(Image, img_name)
    if isinstance(img, Image):  # Check if it's an Image object
        display.show(img)
        sleep(500)  # Display for 500 milliseconds

# Clear the display after showing all images
display.clear()
