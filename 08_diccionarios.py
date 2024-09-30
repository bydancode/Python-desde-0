#Declarar 
mi_diccionario = {
    "daniel" : [1.4, 1.3, 4.0, 5.0],
    "nathaly" : [5.0, 4.1, 4.0, 5.0],
    "karlimar" : [2.4, 1.1, 4.0, 5.0]
}

#dict 
mi_segundo_diccionario = dict(daniel = [1.4, 1.3, 4.0, 5.0],
                              nathaly = [5.0, 4.1, 4.0, 5.0],
                              karlimar = [2.4, 1.1, 4.0, 5.0])

#dict vacio 
# mi_tercer_diccionario = {}
mi_tercer_diccionario = dict()
mi_tercer_diccionario["daniel"] = [1.4, 1.3, 4.0, 5.0]
mi_tercer_diccionario["nathaly"] = [5.0, 4.1, 4.0, 5.0]
mi_tercer_diccionario["karlimar"] = [2.4, 1.1, 4.0, 5.0]

print(mi_diccionario)
print(mi_segundo_diccionario)
print(mi_tercer_diccionario)

mi_diccionario["maria"] = [2.4, 1.1, 4.0, 5.0]
print(mi_diccionario)

#Extrar el valor de una clave en un diccionario 
print(mi_diccionario["maria"])

#del para eliminar una clave/valor de un diccionario 
del mi_diccionario["maria"]
print(mi_diccionario)

#Formas para acceder a los diccionarios
# 1. keys 
print(mi_diccionario.keys())
# 2. values 
print(mi_diccionario.values())
# 3. both 
print(mi_diccionario.items())