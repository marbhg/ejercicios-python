#Creamos la direccion de correo 
correo = input("Introduce la direccion de correo:")
#creamos la longitud del correo 
longitud = len(correo)
#Creamos la vaiable para mostrarlo en mayuscula y minuscula 
correoMayuscula = correo.upper()
correoMinuscula = correo.lower()

#Pintamos el resultado´
print("Longitud del correo es: ", longitud)
print("Mostramos la direccion del correo en mayusculas: ", correoMayuscula)
print("Mostramos la direccion de correo en minuscula: ", correoMinuscula)