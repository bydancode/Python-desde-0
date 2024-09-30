mi_tupla = 1, False, 'Edward', 0.145
print(type(mi_tupla))

def retornar_estudiante():
    return 1, False, 'Edward', 0.145

tupla_estudiante = retornar_estudiante()
print(tupla_estudiante)

var1, var2, var3, var4 = retornar_estudiante()
print(var1, var2, var3, var4)

#one-line swapping    Intercambio de variables gracias a las tuplas 
var1, var2 = var2, var1
print(var1, var2)
