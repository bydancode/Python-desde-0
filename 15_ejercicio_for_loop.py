import turtle

ventana = turtle.Screen()
ventana.bgcolor("white")
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.speed(1)

# Dibujar un rombo
tortuga.left(120)
for i in range(2):
    tortuga.forward(100)
    tortuga.right(60)
    tortuga.forward(100)
    tortuga.right(120)


#Dibujar un cuadrado 

for i in range(4):
    tortuga.forward(100)
    tortuga.right(90)
    
ventana.exitonclick()