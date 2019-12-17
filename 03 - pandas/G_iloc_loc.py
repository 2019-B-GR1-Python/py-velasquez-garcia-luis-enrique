# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:04:31 2019

@author: Kike
"""

import pandas as pd

path_guardado_bin = "C://Users//Kike//Documents//GitHub//py-velasquez-garcia-luis-enrique//03 - pandas//data//artwork_data_complete.pickle"

df = pd.read_pickle(path_guardado_bin)
df2 = df.set_index('id') # convierte en index la columna que enviemos
datos ={
        "nota 1":{
                "Pepito":7,
                "Juanita":8,
                "Maria":9},
        "disciplina":{
                "Pepito":5,
                "Juanita":9,
                "Maria":2}
        }
        
notas = pd.DataFrame(datos)

notas.loc["Pepito"] # puedo mandar cualquier COLUMNA

notas.iloc[0] # solo indices, obtine la fila

type(notas.loc["Pepito"]) # Serie

notas.loc["Pepito", "disciplina"] # devuelve un valor

notas.loc["Pepito",["disciplina","nota 1"]]

notas.loc[["Pepito", "Juanita"],["nota 1"]] # primer arreglo filtra, segundo escoge columnas

notas.loc[["Pepito", "Juanita"],"nota 1"]

notas.loc[[False, True, True]] # mostrar datos "apagado" "encendido"

condicion_notas = notas["nota 1"] > 7 # filtrar por condiciones

notas.loc[condicion_notas]


mayores_siete = notas.loc[condicion_notas,["nota 1"]] 

notas.loc["Maria", "disciplina"] = 7 # cambiar valores 

notas.loc[:, "disciplina"] = 7 # cambiar todos los valores de una columna

#Estudnaites con disciplina menor a 7, subirles a 7
notas.loc[notas["disciplina"] < 7, ["disciplina"] ] = 7 

#Solo pepito tiene 10 en todo
notas.loc[["Pepito"],:] = 10

#disciplina de todos los estudiantes queda en 7
notas.loc[:,["disciplina"]]=7



















primero = df.loc[0] # obtiene la fila del index!!!

primeroi = df.iloc[0]