#De acuerdo a una condicion de tu ciclo while o for 
# Va a permitir parar el ciclo asi no se haya cumplido
# la condicion de salida o la cantidad de veces que debe iterar 

#Ejercicio carrera de caracoles 

import turtle 
import random

meta = 400 
caracol1 = 0
caracol2 = 0

ventana = turtle.Screen()
ventana.bgcolor("white")
tortuga1 = turtle.Turtle()
tortuga1.shape("turtle")
tortuga1.color("red") 
tortuga1.penup()
tortuga1.goto(-300, 100)  
tortuga2 = turtle.Turtle()
tortuga2.shape("turtle")
tortuga2.color("blue")
tortuga2.penup()
tortuga2.goto(-300, -100)

#Dibujar la meta 
meta_linea = turtle.Turtle()
meta_linea.penup()
meta_linea.goto(100, 200)
meta_linea.pendown()
meta_linea.goto(100, -200)
meta_linea.hideturtle()

while True:
    random1 = random.randint(1, 20)
    random2 = random.randint(1, 20)
    caracol1 += random1
    print(f"Caracol 1: {caracol1}")
    tortuga1.forward(random1)
    caracol2 += random2
    print(f"Caracol 2: {caracol2}")
    tortuga2.forward(random2)

    if caracol1 >= meta or caracol2 >= meta:
        break

if caracol1 > caracol2:
    print("El ganador es el caracol rojo")
    tortuga1.color("green")
    ventana.exitonclick()
elif caracol2 > caracol1:
    print("El ganador es el caracol azul")
    tortuga2.color("green")
    ventana.exitonclick()
else:
    print("Esto fue un justo empate")
    ventana.exitonclick()






