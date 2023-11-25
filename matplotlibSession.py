#%%
import matplotlib.pyplot as plt
import numpy as np

#%%
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
# %%
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Mi curva')
plt.xlabel('eje x')
plt.ylabel('y = sin(x)')
plt.title('Mi primer grafico')
plt.legend()
plt.grid(True)
plt.show()
# %% scatter plot
x = np.random.rand(100)
y = np.random.rand(100)
# %%
plt.figure(figsize=(10, 5))
plt.scatter(x, y, c='k', marker='*')
#plt.plot(x, y, c='k', marker='*')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.title('Mi primer scatterplot')
plt.grid(True)
plt.show()
# %% crear un plot de barras
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [2, 5, 8, 9, 6]

plt.figure(figsize=(10, 5))
plt.bar(categorias, valores, width=0.5, color='skyblue')
plt.xlabel('Categoria')
plt.ylabel('Valores')
plt.title('Mi primer grafico de barras')
plt.grid(True)
plt.show()

# %% Histograma
datos = np.random.randn(100000)

plt.figure(figsize=(10, 5))
plt.hist(datos, bins=50, color='green', alpha=0.6)
plt.xlabel('Valores')
plt.ylabel('Frecuencias')
plt.title('Mi primer histograma')
plt.grid(True)
plt.show()

# %% diagrama de pie
etiquetas = ['A', 'B', 'C', 'D', 'E']
valores = [2, 5, 8, 9, 6]
colores = ['red', 'green', 'blue', 'orange', 'yellow']

plt.figure(figsize=(10, 5))
plt.pie(valores, labels=etiquetas, colors=colores, startangle=0, shadow=True, explode=(0.1, 0, 0, 0, 0), autopct='%1.1f%%')
plt.title('Mi primer diagrama de pie')
plt.show()

# %%
