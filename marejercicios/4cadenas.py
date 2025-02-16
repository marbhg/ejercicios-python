#Guardamos la ciudad del usuario 
ciudad = input("Introduce tu ciudad")

#Unimos 2 cadenas 
bienvenida = "Bienvenidos a:" + ciudad;

#Obtenemos el numero de letras de la cadena 
longitud = len(bienvenida);

#Ponemos la cadena en mayuscula
bienvenidaenmayuscula = bienvenida.upper()

#Poner la cadena en miniscula 
bienvenidaenminuscula = bienvenida.lower()

#Imprimimos las variables
print(bienvenida)
print("Longitud ", longitud)
print(bienvenidaenmayuscula)
print(bienvenidaenminuscula)



