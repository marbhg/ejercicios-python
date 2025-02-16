# Pedimos al usuario que introduzca los detalles del producto

nombre_producto = input("Introduce el nombre del producto: ")

# Convertimos las entradas a números decimales (float)
precio_unidad = float(input("Introduce el precio por unidad del producto: "))
cantidad_producto = int(input("Introduce la cantidad de productos que deseas comprar: ")) # Cantidad es un entero
descuento_porcentaje = float(input("Introduce el descuento en porcentaje: "))
iva_porcentaje = float(input("Introduce el IVA en porcentaje: "))

# Calculamos el precio total

# Calculamos el subtotal (precio por unidad * cantidad)
subtotal = precio_unidad * cantidad_producto

# Calculamos el descuento en valor
descuento_valor = subtotal * (descuento_porcentaje / 100)

# Calculamos el subtotal con descuento
subtotal_con_descuento = subtotal - descuento_valor

# Calculamos el IVA en valor
iva_valor = subtotal_con_descuento * (iva_porcentaje / 100)

# Calculamos el precio total (subtotal con descuento + IVA)
precio_total = subtotal_con_descuento + iva_valor

# Mostramos la información al usuario

print("\nDetalles del producto:")
print(f"Nombre del producto: {nombre_producto}")
print(f"Precio por unidad: {precio_unidad:.2f}") # Formateamos a 2 decimales
print(f"Cantidad: {cantidad_producto}")
print(f"Descuento: {descuento_porcentaje:.2f}%") # Formateamos a 2 decimales
print(f"IVA: {iva_porcentaje:.2f}%") # Formateamos a 2 decimales
print(f"Subtotal: {subtotal:.2f}") # Formateamos a 2 decimales
print(f"Descuento aplicado: {descuento_valor:.2f}") # Formateamos a 2 decimales
print(f"Subtotal con descuento: {subtotal_con_descuento:.2f}") # Formateamos a 2 decimales
print(f"IVA aplicado: {iva_valor:.2f}") # Formateamos a 2 decimales
print(f"Precio total: {precio_total:.2f}") # Formateamos a 2 decimales



