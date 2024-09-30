#De una lista de numeros solo imprimir los numeros impares 

lista_numeros = [34, 10, 23, 57, 19, 2, 8, 3]

for numero in lista_numeros:
    if numero % 2 != 0:
        continue
    else:
        print(f"El numero {numero} es impar")
