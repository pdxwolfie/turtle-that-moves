import turtle

turtle.title("Jeremy the turtle that moves")
turtle.bgcolor("aqua")
turtle.setup(500,500)
turtle.shape("turtle") 

screen=turtle.Screen() 
Bob=turtle.Turtle() 

def goUp():
  if Bob.heading() != 270:
    Bob.left(90)
  Bob.forward(20)

def goRight():
  if Bob.heading() != 0:
    Bob.left(90)
  Bob.forward(20)

def goLeft():
  if Bob.heading() != 180:
    Bob.left(90)
  Bob.forward(20)


screen.onkey(goUp,"Up")
screen.onkey(goLeft,"Left")
screen.onkey(goRight,"Right")
screen.listen()
