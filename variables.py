#%%
# -----------------------------------------------------------------------------
# Introducción a las Variables en Python
# -----------------------------------------------------------------------------

# En programación, una variable es un espacio reservado en memoria que tiene un 
# nombre asociado, y que nos permite almacenar valores temporales que pueden cambiar
# a lo largo de la ejecución de un programa. En otras palabras, es como una caja 
# en la que podemos guardar cosas (valores).

# En el contexto de la ciencia de datos, las variables son esenciales porque:

# 1. **Organización de Datos**: Nos permiten guardar y manipular datos fácilmente. 
#    Por ejemplo, podemos tener una variable llamada 'edad' que guarda la edad de un usuario.

# 2. **Reusabilidad**: Una vez que se asigna un valor a una variable, podemos usar 
#    esa variable en múltiples lugares en nuestro código, sin tener que repetir el valor.

# 3. **Legibilidad**: Las variables con nombres descriptivos hacen que nuestro 
#    código sea más fácil de entender. Por ejemplo, es más claro tener una variable 
#    llamada 'precio_total' en lugar de simplemente tener un número flotante sin contexto.

# 4. **Flexibilidad**: Las variables nos permiten realizar operaciones, transformaciones
#    y análisis de manera dinámica, esencial en ciencia de datos para manipular grandes 
#    conjuntos de datos.

# Vamos a ver cómo declaramos y usamos variables en Python.

#%%
# Declaración de Variables

nombre = "Juan"       # Una variable de tipo cadena (string)
edad = 25             # Una variable de tipo entero (int)
altura = 1.75         # Una variable de tipo flotante (float)
tiene_mascota = True  # Una variable de tipo booleano (bool)

# Ahora, podemos imprimir los valores de estas variables para ver su contenido.
#%%
print(nombre)
print(edad)
print(altura)
print(tiene_mascota)

#%%
# Operaciones con Variables

# Las variables no sólo sirven para almacenar datos, sino que también podemos realizar
# operaciones con ellas. Por ejemplo, si queremos actualizar la edad de Juan:

#%%
edad = edad + 1

#%%
print("La nueva edad de Juan es:", edad)

# En ciencia de datos, a menudo realizamos muchas transformaciones y cálculos en 
# nuestros datos, por lo que la capacidad de manipular variables es esencial.

#%%
# Conclusión

# Las variables son uno de los conceptos más fundamentales en programación. Sirven 
# como la base para almacenar, manipular y organizar datos en nuestros programas.
# En el campo de la ciencia de datos, donde el manejo y análisis de datos es central,
# el entendimiento y buen uso de las variables es crucial.

