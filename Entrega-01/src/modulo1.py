# coding=utf-8
'''
Created on 25 oct 2021

@author: santi
'''
import csv
from collections import namedtuple

DatosEmpleados = namedtuple('DatosEmpleados', ',percent_salary_hike, performance_rating, standard_hours, stock_option_level, training_times_last_year, work_life_balance')
#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 1
#----------------------------------------------------------------------------------------------------------------------------

def lee_y_almacena_datos(fichero):
    '''
    Lee un fichero de entrada y devuelve una lista de tuplas . 
    Tenga en cuenta que los tipos numéricos deben ser de tipo int.
    
    Entrada:
    @param fichero: ruta del fichero csv que contiene los datos en codificación utf-8 
    @type fichero: str

    Salida:
    @return: lista de tuplas con la información de los Extranjeros
    @rtype: [DatosEmpleados (int,int,int,int,int,int)]   
    '''
    registros = []
    with open(fichero, encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        for percent_salary_hike, performance_rating, standard_hours, stock_option_level, training_times_last_year, work_life_balance in lector:
            tupla=DatosEmpleados(int (percent_salary_hike), int (performance_rating), int (standard_hours), int (stock_option_level), int (training_times_last_year), int (work_life_balance))
            registros.append(tupla)
    return registros
