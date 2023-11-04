#%% 
# -----------------------------------
# INTRODUCCIÓN
# -----------------------------------

# En Python, un tipo de dato es esencialmente una propiedad intrínseca de un valor que determina 
# cómo se representa, cómo se manipula y cómo interactúa con otros valores. Los tipos de datos son 
# cruciales para la programación y la ciencia de datos ya que definen qué operaciones son posibles 
# y cómo los datos se almacenan y se procesan. 

# En ciencia de datos, utilizar el tipo de dato correcto no solo puede simplificar la lógica y mejorar 
# la eficiencia del código, sino también asegurar que nuestros cálculos y análisis sean correctos.

# -----------------------------------
# TIPOS PRIMITIVOS
# -----------------------------------

# Los tipos primitivos son los bloques básicos en la programación. Son la base sobre la que se 
# construyen estructuras más complejas.

#%%

# Enteros (int)
num_entero = 123
print(type(num_entero))

# Punto flotante (float)
num_flotante = 12.3
print(type(num_flotante))

# Booleano (bool)
valor_booleano = True
print(type(valor_booleano))

# Cadena de caracteres (str)
texto = "Hola, mundo!"
print(type(texto))



#%% 
# En ciencia de datos:
# - Los 'int' y 'float' se usan para cálculos numéricos y análisis estadísticos.
# - Los 'bool' son útiles para filtrar datos y realizar comprobaciones lógicas.
# - Las 'str' se utilizan para procesamiento y análisis de texto, etiquetas, etc.

#%% 
# -----------------------------------
# OPERACIONES ENTRE TIPOS PRIMITIVOS
# -----------------------------------

# Python permite realizar operaciones entre diferentes tipos primitivos, pero es importante 
# comprender cómo funcionan estas operaciones y cuáles son los resultados esperados.
#%%
# Operaciones entre 'int' y 'float'
num_entero = 5
num_flotante = 2.5
resultado = num_entero + num_flotante
print(f"Suma de int y float: {resultado} es un {type(resultado)}")
#%%
# Concatenación de 'str'
saludo = "Hola"
nombre = "Juan"
mensaje = saludo + ", " + nombre + "!"
print(mensaje)

#%%
# Conversión de tipos para operación
edad = 30
mensaje_edad = "Mi edad es " + str(edad)
print(mensaje_edad)
# str(edad) convierte el valor de 'edad' a 'str' para poder concatenarlo con el texto
# es decir, str, esta haciendo un CAST

#%%

# Multiplicación de 'str' y 'int'
repetir_texto = "Hola " * 3
print(repetir_texto)

#%%
# Operación con 'bool'
# En operaciones matemáticas, Python considera True como 1 y False como 0
valor_booleano1 = True  # Considerado como 1
valor_booleano2 = False # Considerado como 0
resultado_booleano = valor_booleano1 + valor_booleano2
print(f"Suma de booleanos: {resultado_booleano}")

#%% 
# En ciencia de datos:
# - Es común encontrar diferentes tipos de datos en un conjunto de datos. Por ejemplo, 
#   un DataFrame podría tener columnas numéricas y de texto. Saber cómo operar con 
#   diferentes tipos de datos es crucial para el preprocesamiento y análisis.
# - Las conversiones entre tipos (por ejemplo, de 'int' a 'str' o viceversa) son 
#   operaciones comunes cuando se preparan datos para análisis o visualización.



#%% 
# -----------------------------------
# LISTAS
# -----------------------------------

# Una lista es una colección ordenada de valores. Es mutable, lo que significa que 
# podemos agregar, eliminar y modificar elementos después de su creación.
#%%
mi_lista = [10, 20, 30, "hola", True]
#%%
print(mi_lista)
print(type(mi_lista))

# En ciencia de datos, las listas son útiles para almacenar y manipular colecciones de datos. 
# Sin embargo, para operaciones matemáticas y estadísticas, es más conveniente usar arrays 
# (con bibliotecas como NumPy).

#%% 
# -----------------------------------
# ARREGLOS (Usando NumPy)
# -----------------------------------

# Aunque las listas son geniales, carecen de la capacidad de realizar operaciones matemáticas 
# eficientes en grandes conjuntos de datos. Aquí es donde NumPy (Numerical Python) entra en juego.

import numpy as np

mi_array = np.array([1, 2, 3, 4, 5])
print(mi_array)
print(type(mi_array))

# Operaciones matemáticas
print(mi_array + 10)
print(mi_array * 2)

# En ciencia de datos, NumPy es fundamental para cálculos numéricos, manipulación de datos, 
# y preparación de datos para otros análisis o visualizaciones.

#%% 
# -----------------------------------
# DICCIONARIOS
# -----------------------------------

# Un diccionario es una colección no ordenada de pares clave-valor. Es útil para almacenar 
# datos que pueden ser identificados por una clave única.

mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "es_estudiante": False
}

print(mi_diccionario)
print(type(mi_diccionario))

# En ciencia de datos, los diccionarios son útiles para almacenar metadatos, configuraciones, 
# y cualquier otro conjunto de datos que requiera acceso por nombre o clave en lugar de índice.

#%% 
# -----------------------------------
# SETS (Conjuntos)
# -----------------------------------

# Un conjunto es una colección no ordenada de valores únicos. Es decir, no permite duplicados.
# Los conjuntos son útiles para operaciones como la unión, intersección y diferencia.

mi_set = {1, 2, 3, 4, 4, 5}  # Nota: El valor 4 aparece duplicado
print(mi_set)  # Observa que el valor 4 solo aparece una vez
print(type(mi_set))

# Operaciones con conjuntos
otro_set = {4, 5, 6, 7}
print(mi_set.union(otro_set))  # Unión de conjuntos
print(mi_set.intersection(otro_set))  # Intersección de conjuntos
print(mi_set.difference(otro_set))  # Diferencia de conjuntos

#%% 
# En ciencia de datos:
# - Los sets son útiles para operaciones de conjunto como identificar items únicos, 
#   encontrar elementos comunes entre dos conjuntos de datos, o identificar diferencias.
# - También son eficientes en términos de tiempo para verificar si un elemento existe 
#   dentro del conjunto, gracias a su estructura interna basada en tablas hash.



#%% 
# -----------------------------------
# CONCLUSIÓN
# -----------------------------------

# Conocer y utilizar correctamente los tipos de datos en Python es esencial, especialmente en 
# ciencia de datos. Nos permite escribir código más eficiente, lógico y claro, 
# y asegurarnos de que nuestros análisis y operaciones sean correctos.

#%% 
# -----------------------------------
# F-STRINGS (Cadenas Formateadas)
# -----------------------------------

# A partir de Python 3.6, se introdujeron las f-strings para facilitar la inserción 
# y formateo de valores dentro de cadenas de texto.
#%%
nombre = "Carlos"
edad = 25

# Usando f-string para insertar variables dentro de una cadena
mensaje_fstring = f"Mi nombre es {nombre} y tengo {edad} años."
print(mensaje_fstring)
#%%


# También puedes incluir expresiones directamente dentro de las llaves
mensaje_fstring2 = f"En cinco años, {nombre} tendrá {edad + 5} años."
print(mensaje_fstring2)
#%%

# Formateo de números con f-string
precio = 1234.5678
#%%
mensaje_fstring3 = f"El precio redondeado es {precio:.2f}"
print(mensaje_fstring3)

#%%

#%% 
# En ciencia de datos:
# - Las f-strings son muy útiles para crear mensajes informativos basados en resultados 
#   de análisis, como medias, medianas o cualquier otro valor estadístico.
# - Permiten un código más limpio y legible al generar reportes o al visualizar 
#   información derivada de los datos.

#%% 
# -----------------------------------
# SLICING DE LISTAS (Rebanado)
# -----------------------------------

# El slicing es una característica que permite extraer una parte de una lista (o cualquier otro 
# tipo de dato secuencial como strings o arrays) usando índices. Es extremadamente útil 
# para acceder a segmentos específicos de datos.
# [donde empiezo : donde termino : pasos]

#%%
# Lista de ejemplo
números = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#%%
# Básico: obtener los tres primeros elementos
primeros_tres = números[0:3]
print(primeros_tres)
#%%
# Sin índice inicial (desde el comienzo hasta el índice 3 excluido)
primeros_tres_v2 = números[:3]
print(primeros_tres_v2)
#%%

# Sin índice final (desde el índice 7 hasta el final)
desde_siete = números[7:]
print(desde_siete)
#%%
# Con pasos: obtener números pares
números_pares = números[0::3]
print(números_pares)
#%%
#%%
# Inverso: invertir la lista
invertido = números[::-1]
print(invertido)
#%%
#%% 
# En ciencia de datos:
# - El slicing es esencial cuando trabajamos con conjuntos de datos grandes y 
#   solo necesitamos acceder a segmentos específicos de estos.
# - Es especialmente útil en análisis exploratorios, limpieza de datos, y 
#   preparación de datos para entrenar modelos de aprendizaje automático.
# - Esta técnica también es relevante cuando trabajamos con arrays usando 
#   bibliotecas como NumPy.




