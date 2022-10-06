"""
Funciones auxiliares para el cálculo de los picos 
"""

import numpy as np

def threshold(data : list , portion = 2.0) -> tuple: 
    '''
    Recibe una lista con los datos 
    y a partir de ahí determina dos hu
    '''
    mean = np.mean(data)
    std = np.std(data)

    print('chivato:', mean,std)

    higher_threshold = mean + portion*std
    lower_threshold = mean - portion*std   
    return higher_threshold, lower_threshold
