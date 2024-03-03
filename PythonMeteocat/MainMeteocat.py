import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------------------------------------------------------------------------------------

# TO DO: 
# No es 'TM'.. Revisar bien las columnas!!

# -------------------------------------------------------------------------------------------------------------

# Carregar dades

file_path = 'nzvn-apee.csv'
data = pd.read_csv(file_path)
print(data.columns)
print(data.head())

data['data_lectura'] = pd.to_datetime(data['data_lectura'])
data = data[data['data_lectura'].dt.year > 2006]
numpy_array = data.to_numpy()
print(numpy_array)

# -------------------------------------------------------------------------------------------------------------

# Visualitza temperatura mitjana del mes de Febrer

data['data_lectura'] = pd.to_datetime(data['data_lectura'])

february_data = data[(data['data_lectura'].dt.month == 2) &
                     (data['data_lectura'].dt.year >= 2014) &
                     (data['data_lectura'].dt.year <= 2019)]

# No es 'TM'.. Revisar bien las columnas!!
daily_means = february_data.groupby(february_data['data_lectura'].dt.date)['TM'].mean()

plt.figure(figsize=(15, 7))
for year in range(2014, 2020):
    yearly_data = daily_means[daily_means.index.year == year]
    plt.plot(yearly_data.index, yearly_data.values, label=str(year))

plt.xlabel('Fecha')
plt.ylabel('Temperatura Media (°C)')
plt.title('Temperatura Media Diaria en Febrero (2014 - 2019)')
plt.legend()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

fig, axs = plt.subplots(6, 1, figsize=(15, 15), sharex=True)
for i, year in enumerate(range(2014, 2020)):
    yearly_data = daily_means[daily_means.index.year == year]
    axs[i].plot(yearly_data.index, yearly_data.values, label=str(year), color=f'C{i}')
    axs[i].set_title(f'Febrero {year}')
    axs[i].xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
    axs[i].legend()

fig.suptitle('Temperatura Media Diaria en Febrero por Año (2014 - 2019)')
plt.xticks(rotation=45)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# -------------------------------------------------------------------------------------------------------------

# Predicció temperatura mes de Febrer

historical_february = data[(data['data_lectura'].dt.month == 2) &
                           (data['data_lectura'].dt.year >= 2011) &
                           (data['data_lectura'].dt.year <= 2020)]

# No es 'TM'.. Revisar bien las columnas!!
historical_daily_means = historical_february.groupby(historical_february['data_lectura'].dt.day)['TM'].mean()

plt.figure(figsize=(10, 5))
plt.hist(historical_daily_means, bins=15, color='blue', edgecolor='black')
plt.title('Distribución de la Temperatura Media Histórica de Febrero (2011-2020)')
plt.xlabel('Temperatura Media (°C)')
plt.ylabel('Frecuencia')
plt.show()

# -------------------------------------------------------------------------------------------------------------

# 5 - Predicció temperatura mes de Febrer (extra)

data['lluvia'] = data['PPT24H'] > 0
prob_lluvia = data[(data['data_lectura'].dt.year < 2020) & (data['data_lectura'].dt.month == 2)]['lluvia'].mean()
predicciones = np.random.rand(29) < prob_lluvia  # 2020 es bisiesto

dias_con_lluvia = np.sum(predicciones)
dias_sin_lluvia = 29 - dias_con_lluvia

plt.figure(figsize=(8, 8))
plt.pie([dias_con_lluvia, dias_sin_lluvia], labels=['Lluvia', 'No Lluvia'], autopct='%1.1f%%')
plt.title('Proporción de días con y sin lluvia - Predicciones para Febrero 2020')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(['Lluvia', 'No Lluvia'], [dias_con_lluvia, dias_sin_lluvia], color=['blue', 'grey'])
plt.ylabel('Número de días')
plt.title('Días con y sin lluvia - Predicciones para Febrero 2020')
plt.show()
