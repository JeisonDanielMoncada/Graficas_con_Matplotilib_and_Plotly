import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]


# Grafica de dispersion entre las calificaciones de matematicas y ciencias

plt.scatter(matematicas, ciencias, color='blue')
plt.title('Relacion entre las calificaciones de Matematicas y Ciencias')
plt.xlabel('Calificacion de Matematicas')
plt.ylabel('Calificacion de Ciencias')

plt.show()

# Gráfico de barras de error:

materias = ('Matematicas', 'Ciencias', 'Literatura')
promedios = (np.mean(matematicas), np.mean(ciencias), np.mean(literatura))
errores = (np.mean(errores_matematicas), np.mean(errores_ciencias), np.mean(errores_literatura))

plt.errorbar(materias, promedios, yerr=errores, fmt='o',capsize=5)
plt.title('Calificacion promedio en barras de error')
plt.xlabel('Materias')
plt.ylabel('Calificacion promedio')

plt.show()

# Grafica de Histograma de matematicas

bin = round(np.mean(np.sqrt(matematicas)),0)
bin2 = 1+ np.log2(len(matematicas))
# aunque al calcular el bins con la raiz cuadrada de la materia nos da 9 con 10 nos da la grafica solicitada
plt.hist(matematicas, bins=10)
plt.title('Distribucion de las calificaciones de Matematicas')
plt.xlabel('Calificacion de Matematicas')
plt.ylabel('Frecuencia')

plt.show()

