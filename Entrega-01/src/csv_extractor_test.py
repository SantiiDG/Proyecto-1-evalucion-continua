# -*- coding: utf-8 -*-
'''
Created on 22 oct 2021

@author: reinaqu_2
'''
import csv_extractor 

def main():
    columnas_a_extraer=['PercentSalaryHike', 'PerformanceRating','StandardHours', 'StockOptionLevel', 'TrainingTimesLastYear', 'WorkLifeBalance']
    csv_extractor.extrae_columnas_csv("../data/IBM employee.csv", 
                                      "../data/IBM employee-cut.csv",
                                      columnas_a_extraer,encoding='utf-8')

if __name__=="__main__":
    main()