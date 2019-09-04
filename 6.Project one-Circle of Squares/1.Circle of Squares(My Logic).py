import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)

def fun(length,angle,angle2):
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle2)

for square in range(100): #360/11 = ... # we choose a prime number so the circle is dense 
    fun(100,90, 101)

