#%% Teoría

# Bienvenido al Seminario de Codificación en Vivo de NumPy
# En los próximos 50 minutos, cubriremos los siguientes temas en NumPy:
# 1. Introducción a NumPy
# 2. Creación de matrices NumPy
# 3. Operaciones de matrices: Aritmética y Difusión (Broadcasting)
# 4. Indexación, Segmentación y Recorrido
# 5. Reorganización y apilamiento de matrices
# 6. Funciones útiles de NumPy
# 7. Estadísticas básicas con NumPy
# 8. Indexación booleana y matrices enmascaradas
# 9. Guardar y cargar matrices NumPy
# ¡Comencemos!

# Primero, asegúrate de que NumPy esté instalado o instálalo usando pip
# !pip install numpy

# Importar la biblioteca NumPy
import numpy as np

# Sección 1: Introducción a NumPy
# NumPy es un paquete fundamental para la computación científica en Python. Proporciona un objeto de matriz multidimensional de alto rendimiento y herramientas para trabajar con estas matrices.

# Sección 2: Creación de matrices NumPy
# Crear una matriz NumPy simple
simple_array = np.array([1, 2, 3, 4, 5])
print("Matriz Simple:", simple_array)

# Crear una matriz 2D (matriz)
dos_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matriz 2D:\n", dos_d_array)

# Crear matrices con marcadores iniciales
matriz_ceros = np.zeros((3, 3))
matriz_unos = np.ones((2, 2))
print("Matriz de Ceros:\n", matriz_ceros)
print("Matriz de Unos:\n", matriz_unos)

# Crear una matriz con un rango de elementos
matriz_rango = np.arange(10)
print("Matriz de Rango:", matriz_rango)

# Crear una matriz con un rango de números decimales
matriz_float = np.arange(1, 3, 0.1)
print("Matriz de Rango Decimal:", matriz_float)

# Sección 3: Operaciones de matrices: Aritmética y Difusión (Broadcasting)
# Realizar operaciones aritméticas elemento por elemento
matriz_suma = simple_array + 2
print("Matriz de Suma:", matriz_suma)

# Difusión (Broadcasting)
matriz_difusion = simple_array * dos_d_array
print("Multiplicación Difundida:\n", matriz_difusion)

# Sección 4: Indexación, Segmentación y Recorrido
# Indexar una matriz 2D
elemento = dos_d_array[1, 2]  # Acceder al elemento en la segunda fila, tercera columna
print("Elemento Indexado:", elemento)

# Segmentación de matrices
matriz_segmentada = dos_d_array[:, 1]  # Obtener la segunda columna
print("Matriz Segmentada:", matriz_segmentada)

# Recorrer matrices
for fila in dos_d_array:
    print("Fila:", fila)

# Sección 5: Reorganización y apilamiento de matrices
# Reorganizar una matriz
matriz_reorganizada = np.reshape(matriz_rango, (2, 5))
print("Matriz Reorganizada:\n", matriz_reorganizada)

# Apilamiento de matrices vertical y horizontalmente
matriz_vstack = np.vstack((simple_array, simple_array))
matriz_hstack = np.hstack((simple_array, simple_array))
print("Matriz VStack:\n", matriz_vstack)
print("Matriz HStack:", matriz_hstack)

# Sección 6: Funciones útiles de NumPy
# Funciones matemáticas
matriz_cuadrada = np.square(simple_array)
print("Matriz Cuadrada:", matriz_cuadrada)

# Funciones estadísticas
valor_promedio = np.mean(dos_d_array)
print("Valor Promedio:", valor_promedio)

# Sección 7: Estadísticas básicas con NumPy
# Calcular la media, mediana y desviación estándar
print("Media:", np.mean(dos_d_array))
print("Mediana:", np.median(dos_d_array))
print("Desviación Estándar:", np.std(dos_d_array))

# Sección 8: Indexación booleana y matrices enmascaradas
# Crear un índice booleano
mayor_que_cinco = (dos_d_array > 5)
print("Mayor que cinco:\n", dos_d_array[mayor_que_cinco])

# Matriz enmascarada: ocultar algunos valores
matriz_enmascarada = np.ma.masked_where(dos_d_array > 5, dos_d_array)
print("Matriz Enmascarada:\n", matriz_enmascarada)

# Sección 9: Guardar y cargar matrices NumPy
# Guardar una matriz en un archivo binario en formato .npy de NumPy
np.save('matriz_guardada.npy', dos_d_array)

# Cargar la matriz desde un archivo .npy
matriz_cargada = np.load('matriz_guardada.npy')
print("Matriz Cargada:\n", matriz_cargada)

# Conclusiones y sesión de preguntas y respuestas sobre NumPy y sus aplicaciones
# Esto marca el final de nuestro seminario de codificación en vivo de NumPy.
# ¡Siéntete libre de hacer preguntas o compartir cualquier problema que estés tratando de resolver con NumPy!

#%% Teoría avanzada, ejemplos de la vida real

# Bienvenido a nuestro Seminario Práctico de Codificación en Vivo de NumPy
# Hoy, exploraremos algunos ejemplos prácticos de codificación donde NumPy brilla.
# Exploraremos:
# 1. Análisis de datos en un conjunto de valores
# 2. Operaciones en matrices y su uso en álgebra lineal
# 3. Operaciones de imagen utilizando matrices NumPy
# 4. Simulación de problemas del mundo real (caminatas aleatorias)
# Recuerda, ¡todo se trata de codificación práctica! ¡Empecemos a trabajar!

# Asegúrate de tener NumPy instalado antes de comenzar
# !pip install numpy

# Importar NumPy para empezar
import numpy as np

# Sección 1: Análisis de datos en un conjunto de valores
# Analicemos algunos datos de altura de un grupo de personas
alturas = np.array([1.50, 1.78, 1.62, 1.90, 1.55, 1.69, 1.75, 1.80])

# Calcular e imprimir estadísticas básicas
print("# Estadísticas Básicas de Alturas")
print("Altura media:", np.mean(alturas))
print("Desviación Estándar:", np.std(alturas))
print("Altura mínima:", np.min(alturas))
print("Altura máxima:", np.max(alturas))

# Supongamos que queremos saber cuántas personas están por encima de la altura promedio
por_encima_del_promedio = alturas > np.mean(alturas)
print("Número de personas por encima de la altura promedio:", np.sum(por_encima_del_promedio))

# Sección 2: Operaciones en matrices y su uso en álgebra lineal
# Realizar algunas operaciones de matrices que son fundamentales en álgebra lineal
print("\n# Operaciones de Matrices")

# Multiplicación de matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

# Producto punto
print("Producto punto de A y B:\n", np.dot(A, B))

# Determinante de una matriz
print("Determinante de A:", np.linalg.det(A))

# Inversa de una matriz
print("Inversa de A:\n", np.linalg.inv(A))

# Eigenvalores y eigenvectores
eigenvalores, eigenvectores = np.linalg.eig(A)
print("Eigenvalores de A:", eigenvalores)
print("Eigenvectores de A:\n", eigenvectores)

# Sección 3: Operaciones de imagen utilizando matrices NumPy
# Supongamos que queremos procesar y analizar datos de imágenes
print("\n# Operaciones de Imagen")

# Para simplificar, creemos una imagen en escala de grises de 5x5 (0=negro, 255=blanco)
imagen = np.random.randint(0, 256, size=(5, 5), dtype=np.uint8)
print("Imagen Aleatoria:\n", imagen)

# Invertir la imagen restando de 255
imagen_invertida = 255 - imagen
print("Imagen Invertida:\n", imagen_invertida)

# Sección 4: Simulación de problemas del mundo real (caminatas aleatorias)
print("\n# Simulación de Caminatas Aleatorias")

# Parámetros de caminata aleatoria
pasos = 1000  # Número de pasos
caminata = np.random.choice([-1, 1], size=pasos)  # Elegir -1 o 1
posicion = np.cumsum(caminata)  # Suma acumulativa para obtener la posición

# Grafiquemos la caminata aleatoria
# Nota: Debes tener matplotlib instalado para ejecutar este código de gráficos
# !pip install matplotlib
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 4))
plt.plot(posicion)
plt.title("Caminata Aleatoria 1D")
plt.xlabel("Número de pasos")
plt.ylabel("Posición")
plt.show()

# Conclusión Final
# Hemos cubierto algunas aplicaciones prácticas de NumPy, y esto solo rasca la superficie.
# La eficiencia y funcionalidad de NumPy se pueden aplicar a una multitud de problemas en ciencia e ingeniería.
# Gracias por participar y sigue experimentando con NumPy para resolver tus propios desafíos únicos!

#%% Estadísticas avanzadas

# Continuemos explorando operaciones estadísticas usando NumPy
# Comenzando con la importación de NumPy
import numpy as np

# Usando los mismos datos de alturas de nuestro ejemplo práctico del seminario
alturas = np.array([1.50, 1.78, 1.62, 1.90, 1.55, 1.69, 1.75, 1.80])

# Ya hemos calculado la media, mínimo, máximo y desviación estándar. Veamos algunas otras estadísticas:

# Varianza
varianza_alturas = np.var(alturas)
print("Varianza de alturas:", varianza_alturas)

# Mediana
mediana_alturas = np.median(alturas)
print("Mediana de alturas:", mediana_alturas)

# Percentiles
percentil_25 = np.percentile(alturas, 25) # Percentil 25
percentil_50 = np.percentile(alturas, 50) # Igual que la mediana, percentil 50
percentil_75 = np.percentile(alturas, 75) # Percentil 75
print("Percentil 25:", percentil_25)
print("Percentil 50 (Mediana):", percentil_50)
print("Percentil 75:", percentil_75)

# Rango de alturas (máximo - mínimo)
rango_alturas = np.ptp(alturas)
print("Rango de alturas:", rango_alturas)

# Ordenar el arreglo para comprender mejor su distribución
alturas_ordenadas = np.sort(alturas)
print("Alturas ordenadas:", alturas_ordenadas)

# Calcular la moda utilizando scipy ya que NumPy no tiene una función directa
from scipy import stats
moda_alturas = stats.mode(alturas)
print("Moda de alturas:", moda_alturas.mode[0])
print("Cantidad en la moda:", moda_alturas.count[0])

# Calcular el rango intercuartil (IQR)
IQR = np.percentile(alturas, 75) - np.percentile(alturas, 25)
print("Rango Intercuartil (IQR):", IQR)

# Coeficiente de correlación (para más de una medida)
# Creemos otro arreglo para pesos y ver la correlación entre altura y peso
pesos = np.array([50, 68, 59, 90, 55, 64, 70, 80])

# Calcular la matriz de coeficiente de correlación entre alturas y pesos
matriz_correlacion = np.corrcoef(alturas, pesos)
print("Matriz de coeficiente de correlación entre alturas y pesos:\n", matriz_correlacion)

# El valor correspondiente a la correlación entre diferentes variables es de interés, que no es 1
coeficiente_correlacion = matriz_correlacion[0, 1] 
print("Coeficiente de correlación entre alturas y pesos:", coeficiente_correlacion)

# Matriz de covarianza para ver la covarianza entre los conjuntos de valores
matriz_covarianza = np.cov(alturas, pesos)
print("Matriz de covarianza entre alturas y pesos:\n", matriz_covarianza)

# El valor de covarianza de interés
valor_covarianza = matriz_covarianza[0,1]