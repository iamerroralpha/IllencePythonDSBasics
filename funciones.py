#%%
# ----------------------------------------------
# Introducción a las Funciones en Python
# ----------------------------------------------

'''
Las funciones son uno de los bloques de construcción básicos en programación. 
Una función es un conjunto reutilizable de instrucciones que realizan una acción o devuelven un valor. 

¿Por qué usar funciones?

1. **Reutilización de código**: Puedes escribir una función una vez y usarla en múltiples lugares.
2. **Organización**: Las funciones ayudan a estructurar tu código y lo hacen más legible.
3. **Modularidad**: Facilitan la actualización, corrección y comprensión del código al dividirlo en bloques lógicos.
4. **Abstracción**: Ocultan la complejidad y permiten centrarse en la tarea de alto nivel.

En el ámbito de la ciencia de datos, las funciones son esenciales por las siguientes razones:

1. **Procesamiento de datos**: Puedes crear funciones para limpiar y transformar datos de manera consistente.
2. **Análisis repetitivo**: Realizar tareas como simulaciones estocásticas donde el mismo proceso necesita repetirse muchas veces.
3. **Encapsulamiento de algoritmos**: Implementar y probar algoritmos específicos de manera aislada.
4. **Facilita la replicabilidad**: Si compartes tu código con otros científicos de datos, las funciones facilitan que otros repliquen y entiendan tu análisis.

Veamos un ejemplo básico de una función:
'''

#%%
# Definición de una función simple

def saludar(nombre):
    '''
    Esta función recibe un nombre y devuelve un saludo.
    '''
    return f"Hola, {nombre}!"

#%%
# Uso de la función

resultado = saludar("Juan")
print(resultado)

#%%
'''
Ahora, en un contexto de ciencia de datos, supongamos que a menudo necesitamos calcular el promedio de una lista de números.
Podemos crear una función para esto:
'''

#%%
# Función para calcular el promedio de una lista de números

def calcular_promedio(lista_numeros):
    '''
    Esta función recibe una lista de números y devuelve su promedio.
    '''
    if len(lista_numeros) == 0:
        return 0
    suma = sum(lista_numeros)
    return suma / len(lista_numeros)

#%%
# Uso de la función

datos = [23, 45, 67, 89, 12, 34, 56]
promedio = calcular_promedio(datos)
print(f"El promedio de los datos es: {promedio}")

#%%
'''
Como se puede observar, encapsulamos la lógica de calcular un promedio dentro de una función. 
Este es solo un ejemplo simple, pero en proyectos reales de ciencia de datos, las funciones pueden ser más complejas y vitales para mantener un código organizado y eficiente.
'''

