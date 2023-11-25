#%%
import pandas as pd
import numpy as np

#%% Cargar datos de el archivo csv
dataframe_vino = pd.read_csv('winequality-red.csv', sep=';')

# %% desplegar las primeras 10 filas del dataset default son 5
dataframe_vino.head(10)

# %%
dataframe_vino.tail(10)
# %%
dataframe_vino.shape
# %%
dataframe_vino.describe()
# %%
dataframe_vino.isnull().sum()
# %% acceso standard
dataframe_vino['quality']
# %%
dataframe_vino['fixed acidity']
# %%
dataframe_vino['quality'].unique()
# %%
dataframe_vino['fixed acidity'].unique()
# %% imprimir columnas multiples
dataframe_vino[['quality', 'fixed acidity']]
#%% iloc 
dataframe_vino.iloc[0:5] # solo filas
#%%
dataframe_vino.iloc[0:5, 0:3] # filas y columnas
#%%
dataframe_vino.iloc[:, 0:3] # solo columnas

# %% agroupar por calidad, tener promedio de ph y alcohol
dataframe_agrupado = dataframe_vino.groupby('quality')[['pH', 'alcohol']].mean()

# %% usar aggregation para encontrar minimo, camsimo y promedio de alcohol para cada calidad

datagrame_agg = dataframe_vino.groupby('quality')[['alcohol']].agg(['min', 'max', 'mean'])

# %%
datos_de_region = pd.DataFrame({
'quality':  [3, 4, 5, 6, 7, 8],
'region': ['A', 'B', 'C', 'A', 'B', 'C']
})
# %%
vino_y_region = pd.merge(dataframe_vino, datos_de_region, on='quality')
# %%
import matplotlib.pyplot as plt

#%% graficar histograma de calidad y alcohol

calidad_vino_promedio = dataframe_vino.groupby('quality')['alcohol'].mean()
calidad_vino_promedio.plot(kind='bar', color=[0.337,0.333,0.71])
plt.xlabel('Calidad')
plt.ylabel('Contenido de alcohol promedio')
plt.title('Contenido promedio de alcohol por calidad de vino')
plt.show()#%% graficar histograma de calidad y alcohol

#%%
calidad_vino_promedio = dataframe_vino.groupby('quality')['alcohol'].mean()
calidad_vino_promedio.plot(kind='bar', color='blue')
plt.xlabel('Calidad')
plt.ylabel('Contenido de alcohol promedio')
plt.title('Contenido promedio de alcohol por calidad de vino')
plt.show()
# %% calcular matriz de correlacion
correlacion = dataframe_vino.corr()
print(correlacion)

# %% alcohol a arreglo numpy
alcohol = dataframe_vino['alcohol'].values

# %%
alcohol_std =np.std(alcohol)
# %%
