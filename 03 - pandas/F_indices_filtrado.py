# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:50:10 2019

@author: Kike
"""

import pandas as pd

path_guardado_bin = "C://Users//Kike//Documents//GitHub//py-velasquez-garcia-luis-enrique//03 - pandas//data//artwork_data_complete.pickle"
df = pd.read_pickle(path_guardado_bin)

## Obtener nombres de los artistas

serie_artistas_repetidos = df["artist"] # obtener una columna de un data frame

artistas = pd.unique(serie_artistas_repetidos)

# cuantos artistas hay en el data set????

artistas.size # permite ver cuantos artistas hay sin repetirse

len(artistas)

blake = df["artist"]=="Blake, William" # solo las obras de un artista determinado en etse caso blake
#serie de booleanos

blake.value_counts() ## devuelve todos los artistas pero filtrado cuantas coniciden con william blake
df["artist"].value_counts() # devuelve la cantidad de cad artista

df_blake = df[blake] # obtiene solo las obras de un artista especifico
len(df_blake) # el el numero de obras por blake
df_blake.size
