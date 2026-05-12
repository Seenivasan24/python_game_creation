from turtle import *
import colorsys

# Set drawing speed to maximum
speed(10000)

# Set black background
bgcolor("green")

# Initial hue value for rainbow colors
h = 0

# Outer loop controls overall rotation
for i in range(16):
    # Inner loop draws repeated arc patterns
    for j in range(18):
        # Convert HSV color to RGB
        c = colorsys.hsv_to_rgb(h, 1, 1)

        # Set pen color
        color(c)

        # Increment hue for smooth rainbow effect
        h += 0.005

        # Draw the pattern
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)

    # Draw a small circle after each outer loop iteration
    circle(40, 24)

# Keep the window open
done()