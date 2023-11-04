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

# %%
