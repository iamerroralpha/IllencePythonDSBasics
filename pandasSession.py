#%%
import pandas as pd
import numpy as np

#%%
datos_libros = {
    'Title': ['To Kill a Mockingbird', '1984', 'The Great Gatsby', 'The Catcher in the Rye', 'Lord of the Flies'],
    'Author': ['Harper Lee', 'George Orwell', 'F. Scott Fitzgerald', 'J.D. Salinger', 'William Golding'],
    'Publication Year': [1960, 1949, 1925, 1951, 1954],
    'Pages': [281, 328, 180, 214, 224]
}
# %%
dataframe_libros = pd.DataFrame(datos_libros)

#%% Imprimir el dataframe
print("Dataframe de libros:")
print(dataframe_libros)
# %% Crear un summary (resumen) del dataframe
print("Summary del dataframe:")
print(dataframe_libros.describe())

# %% Imprimir information del dataframe
print("Information del dataframe:")
print(dataframe_libros.info())

# %% Imprimir los nombres  de las columnas del dataframe
print("Nombres de las columnas del dataframe:")
print(dataframe_libros.columns)
# %% Acceder a una columna del dataframe utilizando el indice
indice = 1
print("Acceder a una columna del dataframe utilizando el indice:")
print("El titulo para el indice que elegimos es ")
titulo = dataframe_libros.columns[indice]
print(titulo)
print("Los valores para el indice que elegimos son ")
print(dataframe_libros[titulo])

# %% Forma estandar de acerder al dataframe
print("Forma estandar de acerder al dataframe:")
print("Informacion del titulo: ")
print(dataframe_libros['Title'])
print("Informacion del autor: ")
print(dataframe_libros['Author'])
print("Informacion del año de publicacion: ")
print(dataframe_libros['Publication Year'])
print("Informacion de las paginas: ")
print(dataframe_libros['Pages'])

# %% que tipo de data es cada columna
type(dataframe_libros['Title'])

# %% delimitar el dataframe a la infomacion que me interesa
print("Delimitar el dataframe a la infomacion que me interesa:")
print("Acceder al titulo y al autor: ")
sub_dataframe_libros = dataframe_libros[['Title', 'Author']]
print(sub_dataframe_libros)

# %%
type(sub_dataframe_libros)
# %% Accesar filas del dataframe utilizando iloc
print("Accesar filas del dataframe utilizando iloc:")
print(dataframe_libros.iloc[4])
# %% Acceder a varias filas del dataframe utilizando iloc
print("Acceder a varias filas del dataframe utilizando iloc:")
print(dataframe_libros.iloc[[0, 2, 4]])

# %% Acceder a varias filas del dataframe utilizando iloc
print("Acceder a varias filas del dataframe utilizando iloc:")
print(dataframe_libros.iloc[::-2]) # el slashing sirve como lo vimos en numpy
# %% Agregar una nueva colmna al dataframe
print("Agregar una nueva colmna al dataframe:")
dataframe_libros['Price'] = [10.99, 12.99, 9.99, 7.99, 11.99]
print("Dataframe con la nueva columna Precio:")
print(dataframe_libros)

# %% Orderar el dataframe basandonos en una columna
print("Orderar el dataframe basandonos en una columna:")
print("Ordenar el dataframe por el an;o de publicacion: ")
print(dataframe_libros.sort_values('Publication Year', ascending = True))
# %% Orderar el dataframe basandonos en una columna
print("Orderar el dataframe basandonos en una columna:")
print("Ordenar el dataframe por el an;o de publicacion: ")
print(dataframe_libros.sort_values('Publication Year'))
# %% Ordenar el dataframe basandonos en una columa de forma descendente
print("Ordenar el dataframe basandonos en una columa de forma descendente:")
print(dataframe_libros.sort_values('Publication Year', ascending=False))

#%% Filtrando elementos del dataframe
print("Filtrando elementos del dataframe:")
print("Filtrando elementos por el n'umero de paginas")
libros_grandes = dataframe_libros[dataframe_libros['Pages'] > 220]
print(libros_grandes)
# %% Filtrando datos de acuerdo a una regla de lista booleana
print("Filtrando datos de acuerdo a una regla de lista booleana:")
lista_booleana = [True, False, True, False, True]
dataframe_filrado = dataframe_libros[lista_booleana]
print(dataframe_filrado)
# %% Agrupar y calcular estadiscica para cada autor
print("Agrupar y calcular minimos para cada autor:")
precio_promedio_autor = dataframe_libros.groupby('Author').min()
print(precio_promedio_autor)
# %% Refrescar valores utilizando iloc
print("Refrescar valores utilizando iloc:")
dataframe_libros.loc[dataframe_libros['Title'] == 'The Great Gatsby', 'Pages'] = 203
print(dataframe_libros)
# %% borrar alguna columna del dataframe
print("Borrar alguna columna del dataframe:")
dataframe_libros_backup = dataframe_libros.copy(deep = True)
print("Dataframe backup: ")
print(dataframe_libros_backup)
del dataframe_libros_backup['Price']
print("Dataframe sin la columna precio: ")
print(dataframe_libros_backup)

# %% Seleccion avanzada de datos
print("Seleccionar libros publicados despues de 1950 y con menos de 300 paginas")
lista_booleana_seleccion_avanzada = (dataframe_libros['Publication Year'] > 1950) & (dataframe_libros['Pages'] < 300)
seleccion_avanzada = dataframe_libros[lista_booleana_seleccion_avanzada]
print(seleccion_avanzada)
# %% Agregar una variable categ'orica a un dataframe utilizando una funcion

def categoria_precios(precio: int):
    if precio < 8:
        return 'Barato'
    elif precio < 11:
        return 'Medio'
    else:
        return 'Premium'
# %%
dataframe_libros["Price Category"] = dataframe_libros['Price'].apply(categoria_precios)

# %% Busquda de caracteres en el dataframe
print("Busqueda de The en el dataframe:")
dataframe_libros_contieneThe = dataframe_libros[dataframe_libros['Title'].str.contains('The')]
print(dataframe_libros_contieneThe)
print("Dataframe original:")
print(dataframe_libros)


# %% Ahora que la busqueda sea case insensitive
print("para todos los casos que tengan The o the")
dataframe_libros_contiene_Thethe = dataframe_libros[dataframe_libros['Title'].str.contains('The|the', case = False)]
print(dataframe_libros_contiene_Thethe)
print("Dataframe original:")
print(dataframe_libros)

# %% Ahora que la busqueda sea case insensitive
print("para todos los casos que tengan The o the")
dataframe_libros_contiene_Thethe = dataframe_libros[dataframe_libros['Title'].str.contains('the', case = False)]
print(dataframe_libros_contiene_Thethe)
print("Dataframe original:")
print(dataframe_libros)
# %% Cosas avanzadas que no abordamso en la sesion en vivo...
