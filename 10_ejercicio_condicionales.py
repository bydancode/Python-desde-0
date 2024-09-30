# Ejercicio de admisiones a un equipo por altura y edad 

print("Bienvenido a las admisiones del equipo!")
edad = int(input("Introduzca su edad: "))
altura = float(input("Introduzca su estatura: "))

if edad >= 18:
    if altura > 1.70:
        print("Usted puede participar")
    else:
        if edad > 25 and altura > 1.65:
            print("Usted puede participar")
        else: 
            print("Usted no puede participar")
else:
    print("Usted no puede participar")