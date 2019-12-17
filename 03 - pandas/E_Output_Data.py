# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:57:44 2019

@author: Kike
"""
import numpy as np
import pandas as pd
import os
import sqlite3
import xlsxwriter


path_guardado_bin = "C://Users//Kike//Documents//GitHub//py-velasquez-garcia-luis-enrique//03 - pandas//data//artwork_data_complete.pickle"
df5 = pd.read_pickle(path_guardado_bin)
df =df5.iloc[49980:50519,:].copy() # copiar cierta seccion del df5 a la variable df, solo es una seccion

#   TIPOS DE ARHIVO:
#   JSON
#   Excel
#   SQL


###### EXCEL ########
path_guardado ='C://Users//Kike//Documents//GitHub//py-velasquez-garcia-luis-enrique//03 - pandas//data//mi_df_completo.xlsx' # podemos guardar algo con cualquier nombre de excel
df.to_excel(path_guardado)
df.to_excel(path_guardado, index=False)

columnas = ['artist','title','year']
df.to_excel(path_guardado, columns = columnas) #se muestran solo las columnas que estan en la varialbe columnas

####MULTIPLES HOJAS DE TRABAJO######
path_multiple ='C://Users//Kike//Documents//GitHub//py-velasquez-garcia-luis-enrique//03 - pandas//data//mi_df_multiple.xlsx'

writer = pd.ExcelWriter(path_multiple,
                        engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = 'Primera') # crear una nueva hoja de excel

df.to_excel(writer, sheet_name = 'Segunda',
            index=False)

df.to_excel(writer, sheet_name = 'Tercera',
            columns=columnas)

writer.save() # aqui recien se crea el archivo

####MULTIPLES HOJAS DE TRABAJO ######

#sacar el numero de registro de cierta columna
num_artistas = df['artist'].value_counts()

path_colores ='C://Users//Kike//Documents//GitHub//py-velasquez-garcia-luis-enrique//03 - pandas//data//mi_df_colores.xlsx'

writer = pd.ExcelWriter(path_colores,
                        engine = 'xlsxwriter')

# una serie es una columnda en excel
num_artistas.to_excel(writer,
                      sheet_name='Artistas') # crear nueva hoja

hoja_artistas = writer.sheets['Artistas'] #seleccionar la hoja

rango_celdas = 'B2:B{}'.format(len(num_artistas.index)+1) # es un string
 # B{} sirve para hacer dinamico el numero de la celda
#.format()es la funcion q obtiene el dato para meterlo en {} 

formato_artistas ={ # diccionario, es la configuracion de los colores y rangos para asignar colores 
        "type":"2_color_scale",
        "min_value":"10",
        "min_type":"percentile",
        "max_value":"99",
        "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas,
                                formato_artistas)

writer.save() 

##### graficos #####
path_grafico = 'C://Users//Kike//Documents//GitHub//py-velasquez-garcia-luis-enrique//03 - pandas//data//mi_df_colores.xlsx'
workbook = xlsxwriter.Workbook(path_grafico)
worksheet = workbook.add_worksheet()

worksheet.write_column('B2', num_artistas)

chart = workbook.add_chart({'type': 'line'})
chart.add_series({
    'values': '=Sheet1!$B$2:$B$85',
    'marker': {
        'type': 'square',
        'size': 10,
        'border': {'color': 'black'},
        'fill':   {'color': 'red'},
    },
})
worksheet.insert_chart('C1', chart)

workbook.close()

##### SQL  ######

with sqlite3.connect("bdd_artist.db") as conexion: ## .db archivos de sqlite
    df5.to_sql('py_artistas', conexion)
    # el archivo se crea en la carpeta donde esta el script, usar Dbeaver para abrirlo
    
### MYSQL ###
    #with mysql.connect('mysql://user:password@ip:puerto/nombre_base') as conexion:
        #df5.to_sql('tabla_mysql', conexion)
        
### JSON ####
        
df.to_json('artistas.json') # el formato no es lo mas adecuado

df.to_json('artistas_tabla.json', orient='table') # el formato con el q sea crea es como tabla

    
    
    
    
    




















