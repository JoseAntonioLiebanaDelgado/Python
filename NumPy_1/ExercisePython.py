import csv
import numpy as np

nombres_archivos = ['2020_MeteoCat_Estacions.csv', '2022_MeteoCat_Detall_Estacions.csv', 'MeteoCat_Metadades.csv']

for nombre_archivo in nombres_archivos:
    print(f"\nContenido del archivo: {nombre_archivo}\n")

    with open(nombre_archivo, 'r') as file:
        lines = file.readlines()

    lines_array = np.array(lines)

    for line in lines_array:
        print(line.strip())