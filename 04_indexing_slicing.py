cadena = "Hola, mundo!"

#El indexing es la capacidad de acceder a los caracteres de un string 

print(cadena[0])

#El slicing permite extraer cadenas más grandes de la cadena principal, listas-tuplas-secuencias
#el primer caracter es inclusivo y el segundo exclusivo 
# DEESDE / HASTA / SALTOS

print(cadena[0:4]) #Hola
print(cadena[6:11]) #mundo
print(cadena[6:]) #mundo!
print(cadena[:7]) #Hola, m

#slicing NEGATIVO, cuando el slicing es negativo se empiezan las posiciones desde el numero -1
print(cadena[-5:-1]) #mundo


#El tercer argumento sería de cuanto en cuanto se saltaría 
print(cadena[::2]) #Hl,mno

#Ejercicio, telefono sin guiones 
telefono = "4-5-6-3-2-4-7-9"
print(telefono[::2])

telefono2 = "-4-5-6-3-2-4-7-9"
print(telefono2[1::2])

#Saltos negativos
print(cadena[::-1]) #La cadena al reves 

