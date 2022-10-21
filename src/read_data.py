# Bibliotecas
import pandas as pd # Lectura de datos
import matplotlib.pyplot as plt # Dibujo de las gráficas 
import numpy as np # Matrix operations


def read_data(source:str, columns_name:list[str])-> pd.DataFrame:
    '''
    - `source`: ruta y nombre del fichero a leer.
    - `columns_name`: Nombre de las columnas
    '''
    signal = pd.read_csv( 
    source, 
    names = columns_name, 
    delimiter = "\t", 
    skiprows = range(3), 
    index_col = False, 
    decimal = ","
    ) 
    return signal


try:
    from constants import FILES_NAMES, NEURONS, ALL_COLUMNS
except:
    from src.constants import FILES_NAMES, NEURONS, ALL_COLUMNS

    
signal= {
    'C' : read_data(FILES_NAMES['C'], NEURONS),
    'R' : read_data(FILES_NAMES['R'], NEURONS),
    'G' : read_data(FILES_NAMES['G'], ALL_COLUMNS)
}