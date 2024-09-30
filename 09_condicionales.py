#Es importante el espacio identado en python,
# porque es el scope de los condicionales 

edad = 15
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

# Condicionales con multiples comparaciones 

if edad >= 0 and edad <= 12:
    print("Usted es un niño")
elif edad >= 13 and edad <=17:
    print("Usted es un adolecente")
elif edad >= 18 and edad <= 59:
    print("Usted es un adulto")
elif edad >= 60:
    print("Usted es un adulto mayor")
else:
    print("Usted no introdujo un numero valido para una edad")

