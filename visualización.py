import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Cargar de datos
file_path = 'detail_300BLK.csv'  # Asegurarse de que esta ruta sea accesible en el entorno local
data = pd.read_csv(file_path)

# Selecciona y renombra las columnas relevantes
data_renamed = data[['Ammo Name', 'Bullet Weight', 'Muzzle', '100 Yards.1', '200 Yards.2']].rename(columns={
    'Bullet Weight': 'Peso de la bala',  # Corregir la coma que faltaba aquí
    'Muzzle': 'Velocidad',
    '100 Yards.1': 'Energía a 100 Yardas',
    '200 Yards.2': 'Energía a 200 Yardas'
})

# Limpia los datos eliminando filas con valores NaN en las columnas seleccionadas
data_clean = data_renamed.dropna()

# Crea el gráfico de coordenadas paralelas
plt.figure(figsize=(12, 8))

# Agrega un título y subtítulo explicativos
plt.suptitle('Gráfico de coordenadas paralelas para tipos de balas y sus características', fontsize=16)
plt.title(
    'Este gráfico muestra las características de diversos tipos de munición, incluyendo peso de la bala, '
    'velocidad al salir del cañón y energía del proyectil a 100 y 200 yardas. '
    'Cada línea representa un tipo diferente de munición, facilitando la comparación entre ellos.',
    fontsize=8, style='italic'
)

# Dibuja el gráfico de coordenadas paralelas
parallel_coordinates(data_clean, 'Ammo Name', colormap=plt.get_cmap("tab10"))

# Configura los ticks del eje y
plt.yticks(range(0, max(data_clean['Velocidad']) + 1, 100))

# Habilita la leyenda con un título
plt.legend(title='Nombre de la Bala', bbox_to_anchor=(1.05, 1), loc='upper left')

# Rota los ticks del eje x para mejor legibilidad
plt.xticks(rotation=20)

plt.annotate('Fuente: https://www.kaggle.com/datasets/jpmiller/external-ballistics (documento: detail_300BLK.csv)',
             xy=(0.1, -0.2),
             xycoords='axes fraction',
             ha='left',
             va='center',
             fontsize=8,
             color='gray')

#Guardar el gráfico
plt.savefig('Carballo_GraficoCoordenadasParalelas.png', bbox_inches='tight')

# Muestra el gráfico
plt.show()
