import csv
import json

# Ejercicio 1 - ETL from csv

# Abrimos el archivo CSV en la misma ubicación que el script
with open('basket_players.csv', mode='r', encoding='ASCII') as csv_file:
    # Creamos el objeto reader, que leerá del archivo csv
    dades = csv.reader(csv_file, delimiter=';')

    # Iteramos sobre el objeto reader con un for loop y enumerate para obtener el índice y la fila
    for i, fila in enumerate(dades):
        # Mostramos por pantalla el índice y la fila
        print(f"Fila {i}: {fila}")

# -------------------------------------------------------------------------

# Este código realiza lo siguiente:
# Define un diccionario que mapea los nombres de las columnas de inglés a catalán.
# Abre el archivo CSV original.
# Lee el archivo fila por fila.
# Si es la primera fila (la cabecera), usa el diccionario para cambiar los nombres de las columnas.
# Añade la fila transformada a la lista transformed_data.
# Luego, imprime la lista transformed_data que contiene todas las filas con la cabecera ya en catalán.

# A continuación, el nuevo código para transformar la cabecera
column_names = {
    'Name': 'Nom',
    'Team': 'Equip',
    'Position': 'Posicio',
    'Height': 'Altura',
    'Weight': 'Pes',
    'Age': 'Edat'
}

# Ruta al archivo CSV
file_path = 'basket_players.csv'

# Lista para guardar las filas transformadas
transformed_data = []

# Abrimos el archivo CSV en la misma ubicación que el script
with open(file_path, mode='r', encoding='ASCII') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    # Iteramos sobre cada fila del archivo
    for i, row in enumerate(csv_reader):
        if i == 0:  # Si es la primera fila, cambiamos los nombres de las columnas
            header = [column_names[column] if column in column_names else column for column in row]
            transformed_data.append(header)
        else:
            transformed_data.append(row)

# Ahora 'transformed_data' contiene todas las filas con la cabecera en catalán
# Puedes imprimir para verificar
for row in transformed_data:
    print(row)

# -------------------------------------------------------------------------

# Este código hace lo siguiente:
# Crea un diccionario que mapea las posiciones de inglés a catalán.
# Itera sobre cada fila de la lista transformed_data, que ya debería tener la cabecera traducida al catalán.
# Para todas las filas que no son la cabecera, actualiza la columna de la posición utilizando el diccionario de mapeo.
# Añade cada fila actualizada a la nueva lista translated_positions_data.

# Diccionario para mapear las posiciones de los jugadores de inglés a catalán
positions_map = {
    'Point Guard': 'Base',
    'Shooting Guard': 'Escorta',
    'Small Forward': 'Aler',
    'Power Forward': 'Ala-pivot',
    'Center': 'Pivot'
}

# Asumimos que la columna de posiciones es la tercera columna (índice 2)
# y que 'transformed_data' ya contiene todas las filas con la cabecera en catalán

# Lista para guardar las filas con las posiciones traducidas
translated_positions_data = []

# Iteramos sobre cada fila de 'transformed_data'
for row in transformed_data:
    # Creamos una copia de la fila para modificarla
    new_row = row.copy()
    if row != transformed_data[0]:  # Si no es la cabecera
        # Traducimos la posición usando el diccionario 'positions_map'
        new_row[2] = positions_map.get(row[2], row[2])  # Usamos 'get' para evitar errores si la clave no existe
    # Añadimos la fila modificada a la nueva lista
    translated_positions_data.append(new_row)

# Ahora 'translated_positions_data' contiene todas las filas con las posiciones traducidas
# Puedes imprimir para verificar
for row in translated_positions_data:
    print(row)

# -------------------------------------------------------------------------

# Para la tercera transformación, convertiremos las unidades de altura y peso del sistema imperial al métrico. Vamos a definir dos constantes para las conversiones y aplicaremos estas transformaciones a cada fila de datos (excepto la cabecera). Aquí están los pasos y el código correspondiente:
# Definir las constantes de conversión para polzadas a centímetros y libras a kilogramos.
# terar sobre cada fila y convertir los valores de altura y peso.
# onvertir los valores de string a float, aplicar la conversión y redondearlos a dos decimales.
# ctualizar la fila con los nuevos valores convertidos.

# Constantes de conversión
INCH_TO_CM = 2.54
POUND_TO_KG = 0.45359237

# Asumimos que 'translated_positions_data' contiene todas las filas con las posiciones traducidas
# y que la altura es la cuarta columna (índice 3) y el peso es la quinta columna (índice 4)

# Lista para guardar las filas con la altura y el peso convertidos
converted_data = []

# Iteramos sobre cada fila de 'translated_positions_data'
for row in translated_positions_data:
    # Creamos una copia de la fila para modificarla
    new_row = row.copy()
    if row != translated_positions_data[0]:  # Si no es la cabecera
        # Convertimos la altura y el peso a float y aplicamos las conversiones
        height_in_cm = round(float(new_row[3]) * INCH_TO_CM, 2)
        weight_in_kg = round(float(new_row[4]) * POUND_TO_KG, 2)
        new_row[3] = height_in_cm
        new_row[4] = weight_in_kg
    # Añadimos la fila modificada a la nueva lista
    converted_data.append(new_row)

# Ahora 'converted_data' contiene todas las filas con la altura y el peso convertidos
# Puedes imprimir para verificar
for row in converted_data:
    print(row)

# -------------------------------------------------------------------------

# Para la cuarta transformación, redondearemos los valores de edad, que actualmente están en formato decimal, a enteros.
# Esto es bastante directo usando la función round().
# Suponiendo que ya hemos realizado las transformaciones anteriores y tenemos una lista converted_data con la altura y el peso ya convertidos,
# el siguiente paso es iterar sobre esta lista y redondear los valores de edad. La edad se asume que es la sexta columna (índice 5).

# Asumimos que 'converted_data' contiene todas las filas con la altura y el peso convertidos

# Lista para guardar las filas con la edad redondeada
rounded_age_data = []

# Iteramos sobre cada fila de 'converted_data'
for row in converted_data:
    # Creamos una copia de la fila para modificarla
    new_row = row.copy()
    if row != converted_data[0]:  # Si no es la cabecera
        # Redondeamos la edad al entero más cercano
        rounded_age = round(float(new_row[5]))
        new_row[5] = rounded_age
    # Añadimos la fila modificada a la nueva lista
    rounded_age_data.append(new_row)

# Ahora 'rounded_age_data' contiene todas las filas con la edad redondeada
# Puedes imprimir para verificar
for row in rounded_age_data:
    print(row)

# Este código itera sobre cada fila de la lista converted_data y redondea el valor de la edad a un entero.
# Luego, añade cada fila actualizada a la nueva lista rounded_age_data.

# -------------------------------------------------------------------------

# Define la ruta del nuevo archivo de salida.
# Abre este archivo para escritura.
# Crea un objeto csv.writer, especificando el nuevo delimitador ^.
# Escribe cada fila de la lista rounded_age_data en el nuevo archivo.
# Cierra el archivo una vez que todas las filas se han escrito.

# Ruta al nuevo archivo CSV con el delimitador cambiado
output_file_path = 'jugadors_basket.csv'

# Abrimos el nuevo archivo para escritura
with open(output_file_path, mode='w', newline='', encoding='ASCII') as new_file:
    # Creamos el objeto writer, especificando el nuevo delimitador '^'
    csv_writer = csv.writer(new_file, delimiter='^')

    # Escribimos las filas en el nuevo archivo
    for row in rounded_age_data:
        csv_writer.writerow(row)

# El archivo 'jugadors_basket.csv' ahora contiene los datos transformados con el delimitador '^'
print(f"Datos transformados guardados en {output_file_path}")

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# Ejercicio 2 - Estadísticas

# Inicializamos las variables necesarias para las estadísticas
max_weight = 0
min_height = float('inf')
players_by_team = {}
players_by_position = {}
age_distribution = {}
player_max_weight = ''
player_min_height = ''

# Iteramos sobre los datos (excluyendo la cabecera)
for row in rounded_age_data[1:]:
    name, team, position, height, weight, age = row
    height = float(height)
    weight = float(weight)

    # a) Jugador con el peso más alto
    if weight > max_weight:
        max_weight = weight
        player_max_weight = name

    # b) Jugador con la altura más baja
    if height < min_height:
        min_height = height
        player_min_height = name

    # c) Media de peso y altura por equipo
    if team not in players_by_team:
        players_by_team[team] = {'total_height': 0, 'total_weight': 0, 'count': 0}
    players_by_team[team]['total_height'] += height
    players_by_team[team]['total_weight'] += weight
    players_by_team[team]['count'] += 1

    # d) Recuento de jugadores por posición
    players_by_position[position] = players_by_position.get(position, 0) + 1

    # e) Distribución de jugadores por edad
    age_distribution[age] = age_distribution.get(age, 0) + 1

# Mostramos las estadísticas
print(f"a) Jugador con el peso más alto: {player_max_weight} con {max_weight} kg")
print(f"b) Jugador con la altura más baja: {player_min_height} con {min_height} cm")

print("c) Media de peso y altura por equipo:")
for team, stats in players_by_team.items():
    avg_height = round(stats['total_height'] / stats['count'], 2)
    avg_weight = round(stats['total_weight'] / stats['count'], 2)
    print(f"   {team}: {avg_height} cm, {avg_weight} kg")

print("d) Recuento de jugadores por posición:")
for position, count in players_by_position.items():
    print(f"   {position}: {count}")

print("e) Distribución de jugadores por edad:")
for age, count in sorted(age_distribution.items()):
    print(f"   Edad {age}: {count} jugadores")

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# Ejercicio 3 - Canviar el formato de los datos (Extra)

# Abre el archivo CSV (jugadors_basket.csv) y utiliza csv.DictReader para leer el archivo. DictReader convierte cada fila del CSV en un diccionario,
# donde las claves son los nombres de las columnas y los valores son los datos de cada fila. Estos diccionarios se añaden a la lista data.
# Abre un nuevo archivo JSON (jugadors_basket.json) para escritura y utiliza json.dump para escribir la lista de diccionarios al archivo en formato JSON.
# El argumento indent=4 se utiliza para formatear el JSON con una indentación de 4 espacios, lo que hace que el archivo sea más fácil de leer.
# Imprime un mensaje indicando que la conversión se ha completado y dónde se ha guardado el archivo JSON.
# Una vez ejecutes este código, tendrás un archivo jugadors_basket.json en el mismo directorio que contiene los datos del CSV en formato JSON.


# Ruta al archivo CSV de entrada
input_csv_file = 'jugadors_basket.csv'
# Ruta al archivo JSON de salida
output_json_file = 'jugadors_basket.json'

# Lista para almacenar los datos del CSV
data = []

# Leer el archivo CSV y almacenar los datos en una lista de diccionarios
with open(input_csv_file, mode='r', encoding='ASCII') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='^')
    for row in csv_reader:
        data.append(row)

# Escribir los datos a un archivo JSON
with open(output_json_file, mode='w', encoding='UTF-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f"Datos convertidos a JSON y guardados en {output_json_file}")
