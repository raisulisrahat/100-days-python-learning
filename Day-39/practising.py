# Here I am showing turtle Clock

import turtle
import datetime

# Initialize Turtle settings
myPen = turtle.Turtle()
myPen.shape("arrow")
myPen.speed(0)
myPen.penup()

# Get current time
current_time = datetime.datetime.now()
current_hour = current_time.hour
current_minute = current_time.minute

# Draw clock face
myPen.goto(0, -180)
myPen.color("blue")
myPen.pendown()
myPen.circle(180)

# Draw hour hand
myPen.color("red")
myPen.goto(0, 0)
myPen.setheading(90)  # Point to the top - 12 o'clock
myPen.right(current_hour * 360 / 12)
myPen.pendown()
myPen.forward(100)

# Draw minute hand
myPen.penup()
myPen.goto(0, 0)
myPen.setheading(90)  # Point to the top - 0 minute
myPen.right(current_minute * 360 / 60)
myPen.pendown()
myPen.forward(150)

# Hide the turtle and display the clock
myPen.hideturtle()
turtle.done()
