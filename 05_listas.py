lista_numeros = [1,2,3]
print(lista_numeros)

#append, agregar al final de la lista 
lista_numeros.append(4)
print(lista_numeros)

#count, para contar cuantos elementos iguales hay en la lista
print(lista_numeros.count(2))

#extend, para extender la lista con otros elementos 
lista_extendida = [100, 101]
lista_numeros.extend(lista_extendida)
print(lista_numeros)

#index, para encontrar en que posicion esta un elemento 
print(lista_numeros.index(100))

#insert, permite agregar elementos en cualquier posición POSICION / VALOR
lista_numeros.insert(0, 5000)
print(lista_numeros)

#pop, para extraer/eliminar elementos de la lista y retornarlos por posicion 
#si no se especifica la ubicacion va a extraer el ultimo valor 
print(lista_numeros.pop(2))
print(lista_numeros)

#remove, para eliminar elementos de la lista por valor 
lista_numeros.remove(101)
print(lista_numeros)

#reverse, devuelve la lista a reves 
lista_numeros.reverse()
print(lista_numeros)

#clear, para limpiar totalmente la lista 
lista_numeros1 = lista_numeros[:]
lista_numeros1.clear()
print(lista_numeros1)

#sort, para ordenar la lista 
lista_numeros.sort()
print(lista_numeros)