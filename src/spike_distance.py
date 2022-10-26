from xmlrpc.client import boolean
from constants import NUMBER_OF_SAMPLES, NEURONS
from signal_to_binary import binary_signal
from formulas import words
import numpy as np

def false_window (window: list[int])-> boolean: 
    '''
    Devuelve `True` si la ventana `window` es falsa, `False` en caso contrario
    '''
    return sum(window) > 1

def false_window_percent(words : list[list[int]])-> float:
    '''
    Devuelve el porcentaje de ventanas falsas que haya en estas palabras
    '''
    size = len(words)
    number_of_false_window = len(
        list(
        filter(
            lambda x: x == True,
            map(
                false_window,
                words
            )
        )
    ))

    return number_of_false_window*100/size

def findTheSize(X,percent = 5, tol = 0.1, min = 40, max = 100000)->tuple: 
    '''
    Búsqueda binaria para encontrar un tamaño de ventana en la cual el porcentaje indicado sean ventajas falsas
    '''

    false_window = 100
    while abs(percent- false_window) > tol and max > min + 2:
        w = (max + min) // 2 # ancho de ventana candidato
        word_list = words(X, w, w)
        false_window = false_window_percent(word_list)
        if false_window > percent:
            max = w
        else:
            min = w
    return w, false_window


if __name__ == '__main__':

    print(f" Trozo | Neurona | Intervalo mínimo entre spikes | Cuantil | Cuantil | porcentaje ventanas falsas | tamaño admitir ventanas falsas|  Media | std   ")
    print(' --- | --- | ---  | --- | --- | --- | --- | --- | ---  ')

    for trozo in 'C R G'.split():
        for neuron in NEURONS:
            index_with_spike = list(filter(
                                lambda x: binary_signal[trozo][neuron][x] == 1,
                                list(range(NUMBER_OF_SAMPLES[trozo]))
                                ))


            number_of_spikes = len(index_with_spike)
            distances = [
                # distance and index 
                index_with_spike[i+1]-index_with_spike[i]
                for i in range(number_of_spikes-1)
                ]
            distances.sort()
            minimum_distance = distances[0]
            cuantil = 5
            cuantil_distance = distances[ number_of_spikes*cuantil // 100]

            w_tam, percent = findTheSize(binary_signal[trozo][neuron],cuantil, 0.1, cuantil_distance, (NUMBER_OF_SAMPLES[trozo]-1)//10)

            print(f' {trozo}  | {neuron } | {minimum_distance }| {cuantil/100} | {cuantil_distance}| {percent:.2f}% | {w_tam} | {np.mean(index_with_spike) :.2f} | {np.std(index_with_spike):.2f}  ')
