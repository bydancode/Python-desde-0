#Como dibujar una estrella de 5 puntas con turtle

import turtle

ventana = turtle.Screen()
ventana.bgcolor("red")
tortuga = turtle.Turtle()
tortuga.shape("turtle")

for _ in range(5):
    tortuga.forward(100)
    tortuga.right(144)

turtle.done()
