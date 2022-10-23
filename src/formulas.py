import numpy as np
import math

def words(X:np.array,bits:int,stride:int) -> list[list[int]]:
    '''
    Formación de las palabras de una secuencia binaria
    `X` secuencia binaria temporal correspondiente a una neurona 
    `bits` tamaño de cada palabra que se tomará de la secuencia binaria
    `stride` deslizamiento secuencial de la ventana con la que se forman las palabras 
    Devuelve un vector que contiene todas las palabras formadas a partir de la secuencia binaria temporal de una 
    neurona
    '''
    # Es necesario que la dirección que se tome sea lo suficiente 
    # para que se puedan tomar la cadena de bits si que "se salga"
    X_words = [X[i:(i+bits)] for  i in range(0,len(X)+1-max(stride,bits),stride)]
    return(X_words) 

def probability_dict(pairs: list ) -> dict : 
    ''' Dada una lista `pairs` de enteros o de listas de enteros
    devuelve un diccionario con las probabilidades. 

    En caso de que la lista sea de listas, deberá de consultarse
    con `tuple`.  
    '''
    size = len(pairs)
    values, _ , count = np.unique(pairs, return_inverse=True, return_counts=True, axis=0)
    # caso bits = 1
    if type(pairs[0]) == int:
        join_probability = dict(
            (case, count/size) 
            for case,count in  zip(values, count)
        )
    # caso bits > 1
    else:
        try:
            join_probability = dict(
                (case, count/size) 
                for case,count in  zip(map(lambda x: tuple(x),values), count)
            )
        # para join probability si bits > 1
        except:
            values = list(
                map(
                    lambda v: tuple(map(lambda x : tuple(x), v)),
                    values
                )
            )
            join_probability = dict(
                (case, count/size) 
                for case,count in  zip(values, count)
            )

    return join_probability

def entropy(X_words:np.array) -> float:
    '''
    Cálculo de la entropía de un conjunto de datos
    `X` secuencia de palabras binaria temporal correspondiente a una neurona 
    Devuelve el valor numérico de la entropía correspondiente a la secuencia binaria temporal de una neruona   
    '''
    probability = probability_dict(X_words)
    H =  - sum(map( 
        lambda p:p*math.log(p,2),
        probability.values()
    ))

    return H


def mutual_information(X:list[float],Y:list[float],bits:int,stride:int) -> float:
    ''' 
    Cálculo de la información mutua entre dos series binarias temporales
    `X` secuencia binaria temporal correspondiente a una neurona 
    `Y` secuencia binaria temporal correspondiente a una neurona 
    `bits` tamaño de cada palabra que se tomará de la secuencia binaria
    `stride` deslizamiento secuencial de la ventana con la que se forman las palabras

    La función devuelve la información mutua entre dos neuronas
    '''
    X_words = words(X,bits, stride)
    Y_words = words(Y,bits, stride)

    return entropy(X_words) + entropy(Y_words) - entropy(list(zip(X_words, Y_words)))

# ----- TESTS -----

def words_test():
    l = [1,2,3,4,5,6,7,8,9]
    out_test = [[1,2], [4,5], [7,8]]
    output = words(l, 2, 3)
    assert out_test == output, f"Fail word test, {out_test} expected but {output} arose"

def probability_test():
    print('Test de probabilidad')
    l1 = [1,2,3,1]
    l1_expected = {1: 0.5, 2: 0.25, 3: 0.25}
    l1_out = probability_dict(l1)
    
    assert l1_out == l1_expected, f'Fail, gets {l1_out} but {l1_expected} expected'

    l2 = [[0,1],[1,1],[0,0],[1,1]]
    l2_expected = {(0, 0): 0.25, (0, 1): 0.25, (1, 1): 0.5}
    l2_out = probability_dict(l2)
    assert l2_out == l2_expected, f'Fail, gets {l2_out} but {l2_expected} expected'

def entropy_test():
    # Se comprueba que no falle la ejecución
    words_1 = [[0,1],[1,1],[0,0],[1,0]]
    entropy(words_1)

    words_2 = [[(0,1), (1,0)],
    [(1,1), (1,0)],
    [(0,1), (1,1)],
    [(1,1), (0,0)]]
    entropy(words_2)

def mutual_information_test():
    size = 100
    X = np.random.rand(size)
    Y = np.random.rand(size)
    bits = 3
    stride = 2
    mutual_information(X, Y,bits,stride) 

if __name__ == '__main__':
    words_test()
    probability_test()
    entropy_test()
    mutual_information_test()
    print('Todo correcto')


    

