from array import array
from macpath import join
from tokenize import Double
import numpy as np
import math

def probability(X:np.array) -> np.array:
    ''' 
    Calculo de las probabilidades de un vector de palabras 
    `X` secuencia de palabras formadas a partir de una secuencia binaria temporal de una neurona
    Devuelve un array con las probabilidades correspondientes para cada palabra contenida en el array X
    '''
    X_cases, counts = np.unique(X, return_counts = True, axis = 0)
    probs = np.zeros(len(X))
    for i in range(len(X)):
        for j in range(len(X_cases)):
            if np.array_equal(X[i],X_cases[j]):
                probs[i] = counts[j]/len(X)
    return probs

def words(X:np.array,bits:int,stride:int) -> np.array:
    '''
    Formación de las palabras de una secuencia binaria
    `X` secuencia binaria temporal correspondiente a una neurona 
    `bits` tamaño de cada palabra que se tomará de la secuencia binaria
    `stride` deslizamiento secuencial de la ventana con la que se forman las palabras 
    Devuelve un vector que contiene todas las palabras formadas a partir de la secuencia binaria temporal de una 
    neurona
    '''
    list = []
    for i in range(0,len(X)-stride,stride):
        list.append(X[i:(i+bits)])
    X_words = np.array(l)
    print(X_words)
    return(X_words)

def entropy(X:np.array,bits:int,stride:int) -> Double:
    '''
    Cálculo de la entropía de un conjunto de datos
    `X` secuencia binaria temporal correspondiente a una neurona 
    `bits` tamaño de cada palabra que se tomará de la secuencia binaria
    `stride` deslizamiento secuencial de la ventana con la que se forman las palabras 
    Devuelve el valor numérico de la entropía correspondiente a la secuencia binaria temporal de una neruona   
    '''
    X_words = words(X,bits,stride)
    probs = probability(X_words)
    H = 0
    for p in probs:
        H += -p*math.log(p,2)
    return H

def join_probability(x:int,y:int,pairs:np.array) -> np.array:
    ''' 
    Cálculo de la probabilidad conjunta entre dos eventos temporales
    `x` valor 0/1 correspondiente a un intervalo de tiempo t de la neurona Lp
    `y` valor 0/1 correspondiente a un intervalo de tiempo t de la neurona Ld
    `pairs` array de vectores de dimensión 2 que contiene la secuencia temporal binaria de ambas neuronas agrupadas
            en palabras
    
    `join_prob` probabilidad conjunta entre x e y
    '''
    xy = np.array(x,y)
    cases, counts = np.unique(pairs, return_counts=True, axis=0)
    join_prob = 0
    for j in range(len(cases)):
            if np.array_equal(xy,cases[j]):
                join_prob = counts[j]/len(pairs)
    return join_prob

def join_entropy(X:np.array,Y:np.array,bits:int,stride:int) -> Double:
    ''' 
    Cálculo de la entropia conjunta entre dos secuencias binarias temporales`
    `X` secuencia binaria temporal correspondiente a una neurona 
    `Y` secuencia binaria temporal correspondiente a una neurona 
    `bits` tamaño de cada palabra que se tomará de la secuencia binaria
    `stride` deslizamiento secuencial de la ventana con la que se forman las palabras

    '''
    X_words = words(X,bits,stride)
    Y_words = words(Y,bits,stride)
    pairs = zip(X,Y)
    H = 0
    for x in X_words:
        for y in Y_words:
            H += -join_probability(x,y,pairs)*math.log(join_probability(x,y,pairs),2)
    return H

def mutual_information(X:np.array,Y:np.array,bits:int,stride:int) -> Double:
    ''' 
    Cálculo de la información mútua entre dos series binarias temporales
    `X` secuencia binaria temporal correspondiente a una neurona 
    `Y` secuencia binaria temporal correspondiente a una neurona 
    `bits` tamaño de cada palabra que se tomará de la secuencia binaria
    `stride` deslizamiento secuencial de la ventana con la que se forman las palabras

    La función devuelve la información mútua entre dos neuronas
    '''
    return entropy(X,bits,stride)+entropy(Y,bits,stride)-join_entropy(X,Y,bits,stride)


    

    

