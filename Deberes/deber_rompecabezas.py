# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:54:36 2019

@author: Kike
"""

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

def mostrar_rompecabezas(columnas, filas, imagen, piezas):
    puzzle = np.zeros([filas, int(imagen.shape[0] / filas), imagen.shape[1], 3], dtype=int)
    for i in range(1, filas + 1):
        puzzle[i -1] = np.concatenate(piezas[(i - 1) * columnas: i * columnas], 1)
    puzzle = np.concatenate(puzzle, 0)
    return puzzle

def crear_rompecabezas(columnas, filas, imagen):
    contador = 0
    deslizarVertical = np.split(imagen, filas)
    piezas = np.zeros([columnas * filas, int(imagen.shape[0] / filas),int(imagen.shape[1] / columnas), 3], dtype=int)
    for slice in deslizarVertical:
        deslizarHorizontal = np.hsplit(slice, columnas)
        for horizontal in deslizarHorizontal:
            piezas[contador] = horizontal
            contador += 1
    return piezas

def mezclar_rompecabezas(columnas, filas, imagen):
    rompecabezas = crear_rompecabezas(columnas, filas, imagen)
    np.random.shuffle(rompecabezas)
    return rompecabezas

def jugar(pos_antes, pos_despues, rompecabezas):
    aux_rompecabezas = np.copy(rompecabezas)
    rompecabezas[pos_antes] = rompecabezas[pos_despues]
    rompecabezas[pos_despues] = aux_rompecabezas[pos_antes]
    return rompecabezas


def completado(imagen, puzzled_image):
    return np.array_equal(imagen, puzzled_image)


image = misc.face() 
columnas = input("Número de columnas del rompecabezas: ")
filas = input("Número de filas del rompecabezas: ")
#imprimir_matriz(int(columnas), int(filas))
rompecabezas = mostrar_rompecabezas(int(columnas), int(filas), image, mezclar_rompecabezas(int(columnas), int(filas), image))
plt.imshow(rompecabezas)
plt.show()
nuevo_rompecabezas = rompecabezas
while not completado(image, nuevo_rompecabezas):
    print("Jugar:")
    try:
        pos_antes = int(input("Desde la posición:"))
        pos_despues = int(input("Hacia la posición:"))
        nuevo_puzzle = crear_rompecabezas(int(columnas), int(filas), nuevo_rompecabezas)
        nuevo_puzzle = jugar(pos_antes - 1, pos_despues - 1, nuevo_puzzle)
        nuevo_rompecabezas = mostrar_rompecabezas(int(columnas), int(filas), rompecabezas, nuevo_puzzle)
        plt.imshow(nuevo_rompecabezas)
        plt.show()
    except:
        
        print("Juego Terminado")