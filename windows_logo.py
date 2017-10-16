import turtle
import random

for i in range(4):
  
  if (i == 0):
    turtle.fillcolor(255, 210, 10)
  elif (i == 1):
    turtle.fillcolor(0, 250, 0)
  elif (i == 2):
    turtle.fillcolor("red")
  elif (i == 3):
    turtle.fillcolor("blue")
  turtle.begin_fill()
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.end_fill()


