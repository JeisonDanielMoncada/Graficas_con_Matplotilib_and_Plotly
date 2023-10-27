import plotly.graph_objects as go
import numpy as np
import pandas as pd

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


# CREAMOS EL GRAFICO DE CAJA PARA LAS NOTAS POR MATERIA

fig = go.Figure()  # Crear una figura vacía

# Añadir el trazado de cajas a la figura  de cada Materia
fig.add_trace(go.Box(
    y=nota_Matemáticas, # Datos para el gráfico de cajas
    name='Matemáticas',  # Etiqueta del gráfico de cajas
    jitter=0.3,  # Controlar la dispersión horizontal de los puntos
    whiskerwidth=0.2, # Controlar el ancho de las cajas
    fillcolor='lightgray' # Color de relleno de las cajas
))  
fig.add_trace(go.Box(
    y=nota_Historia, # Datos para el gráfico de cajas
    name='Historia',  # Etiqueta del gráfico de cajas
    jitter=0.3,  # Controlar la dispersión horizontal de los puntos
    whiskerwidth=0.2, # Controlar el ancho de las cajas
    fillcolor='lightgray' # Color de relleno de las cajas
    
))  

fig.add_trace(go.Box(
    y=nota_Ciencias, # Datos para el gráfico de cajas
    name='Ciencias',  # Etiqueta del gráfico de cajas
    jitter=0.3,  # Controlar la dispersión horizontal de los puntos
    whiskerwidth=0.2, # Controlar el ancho de las cajas
    fillcolor='lightgray' # Color de relleno de las cajas
))  

fig.add_trace(go.Box(
    y=nota_Lenguaje, # Datos para el gráfico de cajas
    name='Lenguaje',  # Etiqueta del gráfico de cajas
    jitter=0.3,  # Controlar la dispersión horizontal de los puntos
    whiskerwidth=0.2, # Controlar el ancho de las cajas
    fillcolor='lightgray' # Color de relleno de las cajas
)) 

# Personalizar el diseño del gráfico
fig.update_layout(
    title='Distribucion de Notas por Materia',  # Título del gráfico
    yaxis_title='Notas'  # Etiqueta del eje y
)

# Mostrar el gráfico
fig.show()


# CREAMOS LA GRAFICA  DE PAI DE APROBADS
alumnos_apro = len((datos[datos['aprobado']=="Sí"]["aprobado"]).values)
alumnos_rep = len((datos[datos['aprobado']=="No"]["aprobado"]).values)

labels = ['Aprobado', 'No aprobados']  # Etiquetas de las categorías
values = [((alumnos_apro*100)/(alumnos_apro+alumnos_rep)),((alumnos_rep*100)/(alumnos_apro+alumnos_rep))] # Valores correspondientes a los alumnos aprodos y no aprobados en %

fig = go.Figure()  # Crear una figura vacía

# Añadir el trazado de torta a la figura
fig.add_trace(go.Pie(
    labels=labels, values=values,  # Etiquetas y valores
    # hole=0.4  # Tamaño del hueco en el centro del gráfico de torta
))

# Personalizar el diseño del gráfico
fig.update_layout(
    title='Cantidad de aprobados y no aprobados en %'  # Título del gráfico
)

# Mostrar el gráfico
fig.show()