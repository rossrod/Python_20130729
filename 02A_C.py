import turtle

def drawSquare(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

if __name__ == '__main__':
    drawSquare(100)
    turtle.exitonclick()
