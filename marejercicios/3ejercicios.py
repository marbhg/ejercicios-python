#Le pedimos al usuario que introduzca 2 numeros 
#Convertmimos a umero in (sin decimales) float(puede tener decimales)
numero1 = float(input("Introduzca el numero"))
numero2 = float(input("Introduzca el numero"))

#Hacemos las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

media = (numero1 + numero2) / 2

#Reflejamos el resultado de las operaciones
print("Suma, ",  suma)
print("Resta ,",  resta)
print("Multiplicacion, ",  multiplicacion)
print("Division, ",  division)
print("Media, ",  media)

