import turtle


l = turtle.Turtle()
turtle.bgcolor("black")
l.speed(0)
colors = ["red", "blue", "yellow", "green", "orange", "violet"]


l.penup()
l.goto(-200, 100)  


for i in range(10):
    l.pencolor(colors[i % 6])
    l.write("Thank You", font=("Arial", 24, "normal"))
    l.penup()
    l.forward(10)  
    l.right(36)    
    l.forward(50)  
    l.pendown()


turtle.done()
