# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:36 2019

@author: Kike
"""
import pandas as pd
import os

# 1) JSON CSV HTML XML -> grupo de archivos que se puede leer con pandas
# 2) Binary files -> (!#mf-*1234'120)
# 3) Relational Databases
path = "C://Users//Kike//Documents//GitHub//py-velasquez-garcia-luis-enrique//03 - pandas//data//artwork_data.csv"

df = pd.read_csv(
        path,
        nrows = 10)

columnas = ['id','artist','title',
            'medium','year',
            'acquisitionYear','height',
            'width','units']


df2 = pd.read_csv( 
        path,
        nrows = 10,
        usecols = columnas) # filtramos las colmnas que se desea

df3 = pd.read_csv( 
        path,
        nrows = 10,
        usecols = columnas,
        index_col = 'id') # coloca los valores del id o lo que sea en el index 

# guardar el dataframe
# se puede guardar en un formato binario para guardar los cambios hecho en el dataframe
#es con formato .pickle

#NOTA!!! CAMBIAR EL PATH SIEMPRE QUE SE QUIERA GUARDAR OTRO ARCHIVO
# NO SOBREESCRIBIR!!

path_guardado = "C://Users//Kike//Documents//GitHub//py-velasquez-garcia-luis-enrique//03 - pandas//data//artwork_data.pickle"

df3.to_pickle(path_guardado)


df4 = pd.read_csv(
        path)
path_guardado_bin = "C://Users//Kike//Documents//GitHub//py-velasquez-garcia-luis-enrique//03 - pandas//data//artwork_data_complete.pickle"
df4.to_pickle(path_guardado_bin)

df5 = pd.read_pickle(path_guardado)



#######################################33











