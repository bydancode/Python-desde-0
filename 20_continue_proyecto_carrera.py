#La declaracion continue evita que el codigo dentro del ciclo de ahi en adelante se ejecute

#Ejercicio carrera de caracoles pero solo avanza si los dos
# numeros random son impares 

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

    if random1 % 2 == 0 or random2 % 2 == 0:
        print(f"Los numeros random son {random1} y {random2} y no avanzan porque no son impares los dos")
        continue

    print(" ")
    caracol1 += random1
    print(f"El caracol 1 avanza {random1} para un total de: {caracol1}")
    tortuga1.forward(random1)
    caracol2 += random2
    print(f"El caracol 2 avanza {random2} para un total de: {caracol2}")
    tortuga2.forward(random2)
    print(" ")

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






