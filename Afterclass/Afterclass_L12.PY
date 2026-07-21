import turtle

# Set up the screen
window = turtle.Screen()
window.title("Turtle Square Example")

# Create a turtle object
pen = turtle.Turtle()

# Draw a square using a loop
for _ in range(4):
    pen.forward(100)  # Move forward by 100 pixels
    pen.left(90)      # Turn left by 90 degrees

# Keep the window open until you click it
window.exitonclick()
