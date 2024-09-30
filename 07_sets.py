#declaración de sets 
#los sets no permiten datos repetidos porque son hasheables
# Es una estructura de datos no ordenada porque son hasheables 
# Es principalmente utilizada para saber si hay un elemento o no 
# Es mas rapido que las listas porque la busqueda no es lineal como en una lista 

#Declaracion 

#1 forma 
mi_set = {1, 2, 3, 4}

#2 forma
mi_segundo_set = set()
mi_segundo_set.add(1)
mi_segundo_set.add(2)
mi_segundo_set.add(3)
mi_segundo_set.add(4)

print(mi_set, mi_segundo_set)

#Convertir una lista en un set para eliminar elementos repetidos 
mi_lista = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4]
mi_lista_a_set = set(mi_lista)
print(mi_lista_a_set)

#Los FROZEN SET
#   son sets inmutables, que no cambian y puden ser utilizados para optimizar espacio en memoria 
lista = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4]
mi_frozen_set = frozenset(lista)
print(mi_frozen_set)



