from turtle import *

bgcolor('#9fa')
color('red')
shape('turtle')
title('Love Drawing using Turtle')

#Turtle shrink animation
shapesize(10,10)
fd(0)
shapesize(9,9)
fd(0)
shapesize(8,8)
fd(0)
shapesize(7,7)
fd(0)
shapesize(6,6)
fd(0)
shapesize(5,5)
fd(0)
shapesize(4,4)
fd(0)
shapesize(3,3)
fd(0)
shapesize(2,2)
fd(0)
shapesize(1,1)

#Draw Love shape 
begin_fill()
left(50)
forward(150)
circle(80,180)
right(100)
circle(80,180)
forward(150)
forward(41)
end_fill()

#Write Love text
up()
left(140)
forward (180)
left(90)
forward(80)
right(90)
down()


bgcolor('orange')
pencolor('white')
width(4)
backward(50)
right(90)
forward(30)
up()
forward(25)
down()
circle(20)
up()
forward(50)
down()


left(60)
forward(30)
left(120)
up()
forward (30)
left(100)
down()

forward(30)
up()
left(80)
forward(60)

down()
bgcolor('#222')


circle(13,-270)
left(90)
forward(26)
up()
right(90)
forward(200)

bgcolor('pink')
done() # exit program
