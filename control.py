# Control de Flujo en Python

# El control de flujo se refiere a la decisión sobre el orden en que se ejecutan las instrucciones en un programa.

# En ciencia de datos, el control de flujo es esencial. Al analizar y procesar datos, a menudo se necesita realizar diferentes 
# acciones según las condiciones de los datos.

#%%
datos = [10, 25, 30, 30.1, 45, 50, 60, 70, 80]

#%% 
# Explicación: Bucles FOR
# Un bucle `for` en Python se utiliza para iterar sobre una secuencia. Es una herramienta esencial en Python y se utiliza
# ampliamente en tareas de ciencia de datos para procesar y analizar datos.

# Por ejemplo, la siguiente estructura itera sobre cada elemento de una lista:
#%%
for dato in datos:
    print("Esto se va a imprimir en cada iteración")
    print(dato)
    for i in range(5):
        print("Esto se va a imprimir en cada sub-iteración")
        print(i)
print("Esto se va a imprimir solo una vez")

#%%
print(datos[0])
print(datos[1])
print(datos[2])
print(datos[3])
print(datos[4])

#%%
# Si también quieres acceder al índice del elemento mientras iteras, puedes usar `enumerate`.
# `enumerate` devuelve tanto el índice como el valor en cada iteración:
for indice, dato in enumerate(datos):
    print(f"Índice: {indice}, Valor: {dato}")

#%%
# Explicación: Condicional IF
# El condicional `if` permite que un programa ejecute ciertas instrucciones solo si se cumple una condición.

#%%
umbral = 30

for dato in datos:
    if dato > umbral:
        print(f"{dato} es mayor que {umbral}")
        print(dato)


#%% 
# Explicación: Bucles WHILE
# Un bucle `while` permite ejecutar un conjunto de instrucciones siempre que se cumpla una condición.

datos = [10, 15, 20, 25, 30, 35]
umbral = 28
indice = 0

while datos[indice] <= umbral:
    print(f" Lo que estamos comparando ahora es el dato {datos[indice]}")
    indice += 1

print(f"El primer dato mayor que {umbral} es {datos[indice]}")

#%% 
# Explicación: Condicional ELIF y ELSE
# `elif` y `else` se usan junto con `if` para manejar situaciones donde hay múltiples condiciones a considerar.

dato = 25

#%%
if dato < 20:
    print("Bajo")
elif dato < 40:
    print("Medio")
else:
    print("Alto")
# %%
