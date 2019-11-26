# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:42:13 2019

@author: Kike
"""
#DataFrame

import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)
arr_pand

df1 = pd.DataFrame(arr_pand) # dataframe conjunto de series
s1 = df1[0]
s2 = df1[1]
s3 = df1[2]

s1[0] # acceder a la serie
listax =[8,9]
seriex = pd.Series(listax)
df1.insert(5,5,seriex)

df1[6]=s2 # añanir otra columna "serie"
df1[4]=s1*s2 # operaciones entre columnas "series"


datos_fisicos_uno = pd.DataFrame(
        arr_pand,
        columns =['Estatura (cm)',
                 'Peso (kg)',
                 'Edad (anios)'])


datos_fisicos_dos = pd.DataFrame(
        arr_pand,
        columns =['Estatura (cm)',
                 'Peso (kg)',
                 'Edad (anios)'],
        index=['Luis', 'Enrique'])

df1.index = ['Luis','Enrique'] 
df1.columns = ['A','B','C','D','E','F','G']
 




 
 
 
 
 
 
