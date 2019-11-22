# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:57:41 2019

@author: Kike
"""

import numpy as np
import pandas as pd


lista_numeros = [1,2,3,4]
tupla_numeros=(1,2,3,4)
np_numeros = np.array((1,2,3,4))

# serie
# estructura de datos más facil, puede ser una fila o columna
# deltaframe son muchas filas o muchas columnas

serie_a = pd.Series(      # nueva instancia de series, siempre hay q enviar un iterable -> lista tupla o array
        lista_numeros) 

serie_b = pd.Series(      # nueva instancia de series, siempre hay q enviar un iterable
        tupla_numeros) 

serie_c = pd.Series(     
        np_numeros) 

serie_d = pd.Series([
        True,
        False,
        12,
        12.12,
        "Kike",
        None,
        (),
        [],
        {"nombre":"Kike"}])

serie_d[3] # accede a los elementos de la serie

lista_ciudades = ["Ambato",
                  "Cuenca",
                  "Loja",
                  "Quito"]

serie_ciudad = pd.Series( # puedo cambiar el indice 
        lista_ciudades,
        index=["A",
               "C",
               "L",
               "Q",])

serie_ciudad["Q"] # devuelve el elemento segun el indice
serie_ciudad[3] # no se altera el indice original

valores_ciudad = {
        "Ibarra":9500,
        "Guayaquil":10000,
        "Cuenca":7000,
        "Quito":8000,
        "Loja":3000
        }

serie_valor_ciudad = pd.Series( # serie con diccionario
        valores_ciudad)

serie_valor_ciudad["Guayaquil"]
serie_valor_ciudad[1]

ciudades_menores_5000 = serie_valor_ciudad < 5000 # condiciones, esto devuelve un boolean
ciudades_menores_5000 # las q cumplen la condicion

s5 = ciudades_menores_5000[ciudades_menores_5000] # filtracion de series

serie_valor_ciudad = serie_valor_ciudad*1.1

serie_valor_ciudad[3] = serie_valor_ciudad[3]-50

serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"]-50

print("Lima" in serie_valor_ciudad) # verifico si exite ese elemento en la serie
print("Loja" in serie_valor_ciudad)

rsquere = np.square(serie_valor_ciudad)
sen_serie = np.sin(serie_valor_ciudad)


ciudades_uno =pd.Series({
        "Montañita":300,
        "Guayaquil":10000,
        "Quito":2000})

ciudades_dos =pd.Series({
        "Loja":300,
        "Guayaquil":10000})

ciudades_uno["Loja"] = 0
ciudades_dos["Montañita"]= 0
ciudades_dos["Quito"] = 0

print(ciudades_uno + ciudades_dos)

ciud_add = ciudades_uno.add(ciudades_dos) # parecido a la suma

ciudades_concatenadas = pd.concat([  # concatenar, listas, tuplas, series, se repiten los elementos
        ciudades_dos,
        ciudades_uno])


ciudades_concatenadas_ver_integridad = pd.concat([  # concatenar verificando la integridad de datos
        ciudades_dos,
        ciudades_uno], verify_integrity = True)

ciu_append = ciudades_uno.append( # tambien concatena :)
        ciudades_dos)

ciu_append = ciudades_uno.append( # tambien concatena y tambien verifica integridad :)
        ciudades_dos, verify_integrity = True)


ciudades_uno.max() # devuelve el valor maximo de las series

pd.Series.max(ciudades_uno)
pd.Series.min(ciudades_uno)

np.min(ciudades_uno)
np.max(ciudades_uno)


# Estadiscticas

ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)

ciudades_uno.head(2) # dos primeros
ciudades_uno.tail(2) #dos ultimos

ciudades_uno.sort_values().head(2) #ordeanmiento ascendente
ciudades_uno.sort_values(ascending = False).head(2) # ordenamiento descendente

ciudades_uno.sort_values().tail(2)
ciudades_uno.sort_values(ascending = False).tail(2)










































