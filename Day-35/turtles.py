# Here i am showing Turtle modules in python

# Turtle
from turtle import *

for x in range(50):
    for i in ('red', 'blue'):
        color(i)
        forward(x)
        right(30)

# Turtle and Random
from turtle import Turtle
from random import *

t = Turtle()
for i in range(100):
    step = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(step)

t.screen.mainloop()