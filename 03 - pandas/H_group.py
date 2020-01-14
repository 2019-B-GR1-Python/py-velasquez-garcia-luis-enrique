# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:20:15 2020

@author: Kike
"""

import pandas as pd
import math
import numpy as np

path_guardado_bin = "C://Users//Kike//Documents//GitHub//py-velasquez-garcia-luis-enrique//03 - pandas//data//artwork_data_complete.pickle"

df = pd.read_pickle(path_guardado_bin)

seccion_df = df.iloc[49980:50019,:].copy()

df_agrupado = seccion_df.groupby('artist')
type(df_agrupado)

for a,b in df_agrupado:
    print(type(a)) # str
    print(type(b)) # dataFrame

for columnda_agrupada, df_completo in df_agrupado:
    print(type(columnda_agrupada)) # str
    print(type(df_completo)) # dataFrame

for acquisitionYear, registros in df_agrupado:
    print(registros)

### Ejercicio
a = seccion_df['units'].value_counts() # contar todos los valores que tiene la columna
a.empty # verifica si la serie o columna esta vacia

def llenar_valores_vacios(series, tipo):
    lista_valores = series.value_counts()
    if(lista_valores.empty == True):
        return series
    else:
        if(tipo == 'promedio'):
        
            suma = 0
            numero_valores = 0
            for valor_serie in series:
                if(isinstance(valor_serie,str)):
                    valor = int(valor_serie)
                    numero_valores = numero_valores + 1
                    suma = suma +valor
                else:
                    pass
                    
            promedio = suma / numero_valores
            series_valores_llenos = series.fillna(promedio) #funcion fillna llena los valores nan con el valor en este caso promedio
            return series_valores_llenos  
       
        if(tipo == 'value_counts'):
            for valor_serie in series:
                if(valor == 'nan'):
                    valor == 'mm'
            series_valores_llenos2 = series.fillna(valor)
                
            


def transformar_df(df):
    df_artist = df.groupby('artist')
    lista_df=[]
    
    for artista, df in df_artist:
        copia = df.copy()
        serie_w = copia['width']
        serie_h = copia['height']
        serie_u = copia['units']
        serie_i = copia['inscription']
        copia.loc[:,'width'] = llenar_valores_vacios(
                serie_w, 'promedio')
        copia.loc[:,'height'] = llenar_valores_vacios(
                serie_h, 'promedio')
        copia.loc[:,'units'] = llenar_valores_vacios(
                serie_u, 'value_counts')
        copia.loc[:,'inscription'] = llenar_valores_vacios(
                serie_i, 'value_counts')
        
        lista_df.append(copia)
        
        df_completo_con_valores = pd.concat(lista_df)
        return df_completo_con_valores
    
df_valores_llenos = transformar_df(seccion_df)
    













