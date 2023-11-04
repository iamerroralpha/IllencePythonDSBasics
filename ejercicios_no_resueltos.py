# 1. Imprime la versión de Python que estás utilizando.
#%%
import sys
print(sys.version)
# %%
# 2. Importa la biblioteca numpy y muestra su versión.
import numpy as np
print(np.__version__)
# %%
# 3. Crea una variable llamada "nombre" con tu nombre y otra "edad" con tu edad, e imprime un mensaje que incluya ambas.
#%%
numbre = "Goubiah"
edad = 30
print(f"Mi nombre es {numbre} y tengo {edad} años")
# %%
# 4. Dada la cadena "Python es genial", extrae la palabra "genial" y conviértela a mayúsculas.
cadena = "Python es genial"
palabra = cadena.split()[-1].upper()
print(palabra)
# 5. Escribe una condición que imprima "Mayor de edad" si la variable edad es mayor o igual a 18, de lo contrario imprime "Menor de edad".
#%%
edad = 17.9999
if ( edad >= 18 ):
    print("Mayor de edad")
else:
    print("Menor de edad")
# 6. Usa un bucle para imprimir los números del 1 al 5.
#%%
for i in range(1,6):
    print(i)
# %%
for numero in [1,2,3,4,5]:
    print(numero)
# 7. Crea una función que reciba dos números y retorne su suma.
#%%
def suma(numero1, numero2):
    misuma = numero1 + numero2
    return misuma

# 8. Crea una función que, dado un número, determine si es par o impar.
#%%
def par_o_impar(numero):
    residuo = numero % 2
    if residuo == 1:
        return "Numero es impar"
    else:
        return "Numero es par"

# 9. Dada una lista [3, 1, 4, 1, 5, 9, 2, 6, 5], utiliza slicing para obtener los números 1415.
#%%
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(lista[1:5])

# 10. Crea una función que retorne los números pares de una lista dada.# %%

# 11 Genera una lista con los números cuadrados del 1 al 100... Si utilizas list comprehension, eres un Jedi.

# 12 Crea una función que reciba una cadena y retorne la misma cadena de caracteres invertida.

#"Hola que hace" => "ecah euq aloH"

# 13. Usa un bucle while para imprimir los números del 5 al 1 en orden descendente.

# 14. Crea una función que determine si una palabra es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

# 15. Escribe una función que cuente la cantidad de veces que aparece una letra en una cadena.
def contar_letra(cadena, letra):
    '''
    Cadena = "Cadena de prueba"
    letra = "a"
    resultado = 3 
    '''

# 16. Crea una función que retorne el número mayor de una lista. Eres un jedi si lo haces con numpy.

# 17. Escribe una función que multiplique todos los números de una lista.

# 18. Crea una función que reciba una lista de palabras y retorne la palabra más larga.

def lista_mas_larga(lista):
    '''
    lista = ["I", "love", "python"]
    resultado = python
    '''

# 19. Escribe una función que determine si una lista tiene elementos duplicados. True si tiene duplicados False si no
# [1,2,3,4,5,6,"Hola"] => False
# [1,2,3,4,5,6,"Hola","Hola"] => True

# 20. Crea una función que remueva todos los elementos duplicados de una lista.
# [1,2,3,4,5,6,"Hola"] => [1,2,3,4,5,6,"Hola"]
# [1,2,3,4,5,6,"Hola","Hola"] => [1,2,3,4,5,6,"Hola"]
