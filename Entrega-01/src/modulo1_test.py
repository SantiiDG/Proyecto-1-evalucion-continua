# coding=utf-8
'''
Created on 25 oct 2021

@author: santi
'''
from modulo1 import *
def test_lee_y_almacena_datos(datos):
    print("Número total de registros con datos empleados: " + str(len(datos)))
    print("Los cinco primeros datos son" , datos[:5])
test_lee_y_almacena_datos(lee_y_almacena_datos("../data/IBM employee-cut.csv"))