"""
Implementación de las funciones relacionadas con el algoritmo de codificación SAX
"""
import numpy as np

def PAA ( C : list[float], w:int) -> list[float]:
    ''' Realiza la transformación Piecewise Aggregation Approximation
    Argumentos: 
    `C` serie temporal a transformar
    `w`tamaño de la nueva serie
    '''
    n = len(C)
    w_n = w / n
    n_w = n //w # debe de ser un entero

    bar_C = [
        w_n *sum(
            C[n_w*(i-1) : n_w*i] # no se le suma 1 porque python empieza en 0
        )
        for i in range(1,w+1)
    ]
    return bar_C

def normalize(X):
    '''Normaliza según una distribución normal
    '''
    sigma = np.std(X)
    mu = np.mean(X)
    return (X - mu)/sigma

def between_index(n:float, l:list[float], alphabet_size:int)-> int:
    '''
    Devuelve el índice del número anterior para el que es menor
    '''
    cnt = 0
    while cnt < alphabet_size and n > l[cnt]:
        cnt += 1
    return cnt

def PAA_to_SAX(bar_C:list[float], alphabet_size:int):
    """
    Realiza paso 2 de discretización
    Argumentos: 
    `bar_C`: Serie temporal 
    `alphabet_size`: tamaño del alfabeto de la nueva serie.
    ``
    # Pasos a realizar 
    # 1. Normalización de bar_C
    # 2. Sacar percentiles en función de `alphabet_size` y suponiendo normalidad.
    # 3. Calcular alfabeto(lista de número no de caracteres pa poder utilizar nuestro algoritmos de MI)
    # 4. Asignar a cada bar_C el *caracter/entero* que le corresponda 
    """
    # 1. Normalización de bar_C
    normalized = normalize([bar_C])[0]
    # 2 Cálculo de percentiles
    X = np.random.normal(0,1,100)
    step = 100/alphabet_size
    percentiles = [
        np.percentile(X, i*step)
        for i in range(alphabet_size)
    ]
    new_signal = list(
        map(lambda x: between_index(x,percentiles,alphabet_size ),
        normalized
        )
    )
    return new_signal

def SAX( signal:list[float], word_size:int, alphabet_size:int)->list[int]:
    '''
    Return SAX sybolic represetation for temporal series 
    ''' 
    # Transformamos el tamaño de palabra en la longitud nueva deseada
    bar_C =  PAA (signal, len(signal)//word_size)
    sax = PAA_to_SAX(bar_C, alphabet_size)
    return sax

### test 

if __name__ == '__main__':
    print('Test PAA')
    C = [1,2,1,0, 0, 0 ]
    w =  3
    print(PAA(C,w))

    # test: between_index
    print('\nbetween_index')
    a = 3
    l = [0,1,2]
    for i in [-0.1,0.1,1.1,2.2]:
        print(f' para {i} -> {between_index(i,l,3)}')

    # Test: PAA_to_SAX
    print('\nPAA_to_SAX')
    s = [1,1,1,1,2,2,3,10,-10,2,2,2,2,1,1,1,1,0,0,3,0,3]
    print(s)
    for a in range(1,10, 3):
        print(f'''{a}:
        {PAA_to_SAX(s, a)}
''')

    # Text SAX
    print('\nTest of SAX')
    from read_data import signal
    from constants import NEURONS
    from formulas import mutual_information,words

    trozo = 'C'
    a = 1
    w = 1
    b = 86
    print(signal[trozo][NEURONS[1]].to_list()[0:20])
    sax_signal_1 = SAX(
                signal=signal[trozo][NEURONS[1]].to_list(),
                word_size=w,
                alphabet_size=a
            )

    print('sax_signal',sax_signal_1[100:120])
    sax_words = words(sax_signal_1, b,b)
    print('sax words',sax_words[:5])
    print('mutual information', mutual_information(sax_signal_1,sax_signal_1, 3, 3))
   
    