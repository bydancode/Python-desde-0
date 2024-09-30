#Parametros en las funciones

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


sumar(5, 10)
resta(10, 5)
multiplicacion(5, 10)
dividir(10, 5)