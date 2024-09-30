# Esta es la manera de imprimir el indice y el elemento en python

lista_nombres = ["Daniel", "Franco", "Gonzalez"]

for i in range(3):
    print(i, lista_nombres[i])

# ESTA ES LA MANERA OPTIMA CON ENUM 
# La funcion enumerate devuelve una tupla con el indice y el valor

for indice, valor in enumerate(lista_nombres):
    print(indice, valor)