#Las Librerías que vamos a necesitar
import pandas as pd
import matplotlib.pyplot as plt

def limpiarDatos(airbnbMad):
    #Eliminamos las filas que tengan valores nulos en la columna y 'name'
    airbnbMad = airbnbMad.dropna(subset=["name"])
    #Eliminamos las filas que tengan precio 0 (la columna 'price' no tienen valores nulos ni negativosS, por lo que es necesario eliminar los valores 0)
    airbnbMad = airbnbMad.drop(airbnbMad[airbnbMad.price == 0].index)
    #Eliminamos los valores duplicados en la columna id (si tienen el mismo id, son el mismo alojamiento)
    airbnbMad.drop_duplicates(subset="id")
    return airbnbMad

def CountDistritos(airbnbMad):
    #Contamos el número de alojamientos por distrito y creamos un diagrama de barras
    airbnbMad['neighbourhood_group'].value_counts().plot(kind='bar', figsize=(20,10),color='green')
    plt.title("Distribución de alojamientos por distrito")
    plt.ylabel("Numero de alojamientos")
    #Mostamos el diagrama
    plt.show()

CountDistritos(limpiarDatos(pd.read_csv("listings.csv")))