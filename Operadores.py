#%% 
# ----------------------------------------------
# Introducción a Operadores en Python
# ----------------------------------------------

# Los operadores son símbolos especiales en Python que realizan operaciones específicas en una o más variables o valores.
# En la ciencia de datos, a menudo estamos manipulando y analizando datos, y para hacerlo necesitamos realizar cálculos 
# y comparaciones. Los operadores nos permiten realizar estos cálculos y comparaciones de manera eficiente.

#%% 
# ----------------------------------------------
# Operadores Aritméticos
# ----------------------------------------------

# Estos operadores son esenciales para realizar cálculos numéricos.

# +   : Adición
# -   : Sustracción
# *   : Multiplicación
# /   : División
# %   : Módulo (resto de la división)
# **  : Exponenciación
# //  : División de piso (redondea hacia abajo)

# Ejemplo:

a = 10
b = 3

print(a + b)  # Resultado: 13
print(a - b)  # Resultado: 7
print(a * b)  # Resultado: 30
print(a / b)  # Resultado: 3.333...
print(a % b)  # Resultado: 1 (porque 10 dividido entre 3 tiene un resto de 1)
print(a ** b) # Resultado: 1000 (10 al cubo)
print(a // b) # Resultado: 3 (redondeo hacia abajo)

#%% 
# ----------------------------------------------
# Operadores de Comparación
# ----------------------------------------------

# Estos operadores son esenciales para comparar valores.

# ==  : Igual que
# !=  : No igual que
# >   : Mayor que
# <   : Menor que
# >=  : Mayor o igual que
# <=  : Menor o igual que

# Ejemplo:
#%%
x = 5
y = 8

#%%
print(x == y)  # Resultado: False
print(x != y)  # Resultado: True
print(x < y)   # Resultado: True
print(x > y)   # Resultado: False
print(x >= y)  # Resultado: False
print(x <= y)  # Resultado: True

#%% 
# ----------------------------------------------
# Operadores Lógicos
# ----------------------------------------------

# Son esenciales para construir condiciones complejas a partir de condiciones simples.

# and : Y lógico
# or  : O lógico
# not : NO lógico

# Ejemplo:

condition1 = True
condition2 = False

print(condition1 and condition2) # Resultado: False
print(condition1 or condition2)  # Resultado: True
print(not condition1)            # Resultado: False

#%% 
# ----------------------------------------------
# Importancia en la Ciencia de Datos
# ----------------------------------------------

# En la ciencia de datos, frecuentemente queremos filtrar, transformar y analizar grandes conjuntos de datos.
# Los operadores nos permiten hacer comparaciones y cálculos que pueden ayudarnos a obtener insights 
# de nuestros datos, crear nuevos features o filtrar datos no deseados.

# Por ejemplo, si estamos trabajando con un dataset de ventas, podemos querer calcular la ganancia total,
# filtrar ventas mayores a un cierto valor, o identificar cuántas ventas se realizaron en un rango de tiempo particular.

# Los operadores son herramientas fundamentales en este proceso.

