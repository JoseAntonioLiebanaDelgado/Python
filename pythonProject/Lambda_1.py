# Definición de la función lambda llamada "pvp".
# Toma un parámetro de entrada llamado "precio".
pvp = lambda precio: precio * 1.21

# Ejemplo de uso:
# Definimos un precio inicial de 100.
precio_inicial = 100

# Llamamos a la función lambda "pvp" con el precio inicial como argumento.
# Esto calcula el precio con el 21% de IVA aplicado.
precio_con_iva = pvp(precio_inicial)

# Imprimimos el resultado.
print("Precio con IVA:", precio_con_iva)
