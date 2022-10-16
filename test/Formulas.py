import numpy as np
import math

def probabilidad(X):

    X_cases, counts = np.unique(X, return_counts = True, axis = 0)
    probs = np.zeros(len(X))
    for i in range(len(X)):
        for j in range(len(X_cases)):
            if np.array_equal(X[i],X_cases[j]):
                probs[i] = counts[j]/len(X)
    return probs

def palabras(X,bits):

    '''
    X es un vector con una sucesión de 1's y 0's, y bits es la longitud en la que se va a dividir dicho vector para formar las 
    palabras. Esta función devuelve un vector con las palabras (a modo de subvectores de unos y ceros) en las que se ha dividido el
    vector X.
    '''

    number_index = len(X)/bits
    return np.array_split(X,number_index)

def entropia(X,bits):

    '''
    Cálculo de la entropía de un conjunto de datos, donde X es el vector que contiene las palabras y bits la variable correspondiente a
    la longitud de dichas palabras      
    '''
    X_words = palabras(X,bits)
    probs = probabilidad(X_words)
    H = 0
    for p in probs:
        H += -p*math.log(p,2)
    return H