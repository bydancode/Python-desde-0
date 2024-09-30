#Parametros en las funciones

operar = "si"

def sumar(a, b): # a y b son parametros
    resultado = a + b
    print(f"La suma entre {a} y {b} da como resultado: {resultado}")

def resta(a, b):
    resultado = a - b 
    print(f"El resultado de la resta de {a} y {b} es: {resultado}")

def multiplicacion(a, b):
    resultado = a * b
    print(f"El resultado de la multiplicacion de {a} y {b} es: {resultado}")

def dividir(a, b):
    resultado = a / b
    print(f"El resultado de la division entre {a} y {b} es: {resultado}")

while operar == "si":
    print("Bienvenido a la calculadora de Daniel")
    operacion = input("Que operacion deseas realizar? (sumar, restar, multiplicar, dividir): ")
    numero1 = input("Ingresa el primer numero: ")
    numero2 = input("Ingresa el segundo numero: ")

    if operacion == "sumar":
        sumar(int(numero1), int(numero2))
    elif operacion == "restar":
        resta(int(numero1), int(numero2))
    elif operacion == "multiplicar":
        multiplicacion(int(numero1), int(numero2))
    elif operacion == "dividir":
        dividir(int(numero1), int(numero2))
    else:
        print("Tiene que insertar una operacion valida")

    operar = (input("Deseas realizar otra operacion? (si, no): ")).lower()


    