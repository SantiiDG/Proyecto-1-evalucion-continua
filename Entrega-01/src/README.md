# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<21\>/\<22\>)
Autor/a: \<Santiago Diestro Gallego\>   uvus:\<sandiegal\>

Este proyecto tiene como objetivo analizar las condiciones laborales de los trabajadores de la empresa IBM. El dataset está compuesto por 12 columnas formadas a su vez por datos de tipo str, los cuales convertiremos a tipo int para hacer representación de 6 de ellas, las cuales me han sido asignadas.
 
## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<modulo1.py\>**: Este módulo alberga las funciones que se encargan de leer el dataset, almacenar los datos leidos en una lista de tuplas, además de convertir dichos datos a tipo int. 
  * **\<modulo1_test.py\>**: Este módulo contiene la funcion que se encarga de representar los elementos leidos en el modulo1.py, además de la llamada a dicha función para que muestre por consola los datos. 
  * **\<csv_extractor.py\>**: Contiene las funciones necesarias para crear un nuevo fichero csv con las columnas que se me han asignado del dataset, descartando de este modo las que no.
  * **\<csv_extractor_test.py\>**: Se encarga de ejecutar las funciones del anterior módulo (csv_extractor.py).
* **/data**: Contiene los dataset del proyecto.
    * **\<IBM employee.csv\>**:  Este es el dataset completo se representan las condiciones laborales de los empleados de la empresa IBM
    * **\<IBM employee_cut.csv\>**: Este es el dataset que utilizaré yo en concreto, pues solo contiene las columnas que se me han asignado.
    
## Estructura del *dataset*

Aquí debes describir la estructura del dataset explicando qué representan los datos que contiene y la descripción de cada una de las columnas.

El dataset está compuesto por \<12\> columnas, con la siguiente descripción:

* **\<columna 1>**: de tipo \<str\>, representa el aumento de salario porcentual que tendrán los empleados
* **\<columna 2>**: de tipo \<str\>, representa la clasificación del rendimiento que tienen.
* **\<columna 3>**: de tipo \<str\>, representa la satisfacción al relacionarse en el trabajo.
* **\<columna 4>**: de tipo \<str\>, representa las horas estandard que trabajan.
* **\<columna 5>**: de tipo \<str\>, representa el nivel de opciones sobre acciones.
* **\<columna 6>**: de tipo \<str\>, representa el número total de años trabajados.
* **\<columna 7>**: de tipo \<str\>, representa el tiempo de entrenamiento durante el año pasado.
* **\<columna 8>**: de tipo \<str\>, representa el equilibrio entre el trabajo y la vida de los trabajadores.
* **\<columna 9>**: de tipo \<str\>, representa los años que llevan el la compañía
* **\<columna 10>**: de tipo \<str\>, representa los años que llevan en su puesto de trabajo.
* **\<columna 11>**: de tipo \<str\>, representa los años desde la última promoción.
* **\<columna 12>**: de tipo \<str\>, representa los años que llevan con el actual gerente.

## Tipos implementados

Para poder trabajar correctamente con los datos mencionados anteriormente, se ha definido una tupla (namedtuple), nombrada cómo DatosEmpleados: DatosEmpleados = namedtuple('DatosEmpleados', ',percent_salary_hike, performance_rating, standard_hours, stock_option_level, training_times_last_year, work_life_balance').

## Funciones implementadas
En esta primera parte del proyecto, he implementado una serie de funciones que están repartidas por los distintos modulos del mismo.
### \<modulo 1\>

* **<def lee_y_almacena_datos(fichero)>**: Esta función lee el fichero csv (IBM_employee_cut.csv), en utf-8 para poder leer las tildes o la “ñ”.Se va a encargar de devolver una lista de tuplas con los datos del fichero

### \<test modulo 1\>

* **<def test_lee_y_almacena_datos(datos):>**: esta funcion se encarga de implementar los datos recogidos en la función del modulo 1 y mostrar por pantalla los 5 primeros registros y el número total de los mismos. 

### \<csv_extractor\>
* **<funciones:>**: Se encargan de extraer ciertas columnas deseadas de un archivo csv y crear uno nuevo.

**Cabe decir que no describo todas sus funciones una por una como en los anteriores módulos debido a que está creado por Toñi y no comprendo a la perfección el funcionamiento de las mismas**

### \<csv_extractor_test\>
* **<main>**: esta funcion se encarga de ejecutar las funciones del modulo csv_extractor.py y de este crear el nuevo archivo csv con las columnas ya extraidas.
