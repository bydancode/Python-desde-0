#El ciclo while siempre se va a utilizar cuando no 
# sepamos que cantidad de veces tengamos que iterar 

#Ciclo while para repetir una cantidad n veces dependiendo de una condición
#Es importante verificar que en el while siempre haya una condicion que sea falsa para el ciclo 

#Ejemplo funcionalidad de correos 

nombre = ""
correo = ""
mensaje = ""

condicion_salida = "CONTINUE"

while condicion_salida == "CONTINUE":
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")
    mensaje = input("Ingrese su mensaje: ")

    print(f""" 
        Mensaje enviado por {nombre}.

        destinatario: {correo}

        mensaje: {mensaje}
    """)

    condicion_salida = input("Desea enviar otro mensaje? (CONTINUE/EXIT): ")

