import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

datos = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "materia": ["Matemáticas", "Historia", "Ciencias", "Lenguaje",
                "Matemáticas", "Historia", "Ciencias", "Lenguaje",
                "Matemáticas", "Historia", "Ciencias", "Lenguaje",
                "Matemáticas", "Historia", "Ciencias", "Lenguaje",
                "Matemáticas", "Historia", "Ciencias", "Lenguaje"],
    "nota": [80, 65, 90, 75,
             95, 70, 85, 60,
             78, 82, 93, 68,
             73, 88, 77, 50,
             92, 63, 85, 79],
    "aprobado": ["Sí", "No", "Sí", "Sí",
                 "Sí", "Sí", "Sí", "No",
                 "Sí", "Sí", "Sí", "Sí",
                 "Sí", "Sí", "Sí", "No",
                 "Sí", "No", "Sí", "Sí"]
}

datos = pd.DataFrame(datos)
datos = datos.set_index('id')
nota_Matemáticas = (datos[datos['materia']== 'Matemáticas']['nota']).values
nota_Historia = (datos[datos['materia']=="Historia"]["nota"]).values
nota_Ciencias = (datos[datos['materia']=="Ciencias"]["nota"]).values
nota_Lenguaje = (datos[datos['materia']=="Lenguaje"]["nota"]).values

# Grafica de cola de raton donde dividimos por notas de cada materia
plt.boxplot([nota_Matemáticas,nota_Historia,nota_Ciencias,nota_Lenguaje])

plt.title("Distribución de Notas")
plt.xticks([1, 2, 3, 4], ['Matemáticas', 'Historia', 'Ciencias','Lenguaje'])
plt.ylabel("Notas")
plt.show()


# Grafica de torta de alumnos aprobados 
alumnos_apro = len((datos[datos['aprobado']=="Sí"]["aprobado"]).values)
alumnos_rep = len((datos[datos['aprobado']=="No"]["aprobado"]).values)

categorias = ['Aprobado', 'No aprobados']
valores = [((alumnos_apro*100)/(alumnos_apro+alumnos_rep)),((alumnos_rep*100)/(alumnos_apro+alumnos_rep))]
startangle = 90
colors = ['lightskyblue', 'red']
plt.pie(valores, labels= categorias, colors=colors,startangle=startangle, autopct='%1.1f%%')
plt.title("Distribución de aprobados")
plt.show()