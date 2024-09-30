nombre = "Daniel"
apellido = 'Franco'
frase = """Hola soy Daniel, un gusto
Espero que en el dia de hoy se encuentren bien """

print(type(nombre))
print(frase)
print(len(nombre))


producto1 = "001 - Manzana"
producto2 = "Manzana - 0001"

print(producto1.removeprefix("001 - "))
print(producto2.removesuffix(" - 0001"))