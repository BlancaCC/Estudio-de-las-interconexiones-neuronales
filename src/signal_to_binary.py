import numpy as np
from sympy import N

from constants import NUMBER_OF_SAMPLES


try:
    from read_data import signal 
    from constants import NEURONS, THRESHOLD
except:
    from src.read_data import signal 
    from src.constants import NEURONS, THRESHOLD


def signal_to_binary(signal:list[float], lower_threshold:float, upper_threshold:float)-> list[int]:
    '''
    Dada una señal `signal` que es una lista unidimensional de la señal. 
    Para que cuento como señal debe de superar `upper_threshold` y ser la primera 
    vez o que ya se haya alcanzado un valor inferior a `lower_threshold`.

    Además una vez que se supera el threshold se colocará cuando la tendencia vaya a bajar.
    Esto queda reflejado con los siguientes estados: 
    - Estado 1: 
        Si `s > upper_threshold` entonces:
            i) `last = s`
            ii) pasar a estado 2.
    - Estado 2: 
        Si `s` < `last` entonces:
            i) poner un spike en señal anterior
            ii) `last = -inf`
            iii) pasar a estado 3
        Si no entonces: 
            i) last = s 
    - Estado 3: 
        Si s < lower_threshold:
            i) Cambiar a estado 1
    '''
    state = 1
    binary_signal = list(np.zeros(len(signal)))
    last = - np.Infinity
    
    for i,s in enumerate(signal):
        if state == 1:
            if s > upper_threshold:
                last = s
                state = 2
        elif state == 2:
            if s < last:
                binary_signal[i-1] = 1
                last = - np.Infinity
                state = 3
            else:
                last = s
        elif state == 3:
            if s < lower_threshold:
                state = 1
    return binary_signal

# Señales binarias brutas
binary_signal = {}
for trozo, s in signal.items():
    binary_signal[trozo] = {}
    for neuron in NEURONS:
        binary_signal[trozo][neuron] = signal_to_binary(
                s[neuron].to_list(), 
                    THRESHOLD[trozo][neuron]['lower'],
                    THRESHOLD[trozo][neuron]['upper']
                )
            
# Señales binarias transformadas
radio = {
    'C': 10,
    'R': 16, 
    'G': 65
}
transformed_binary_signal = {}
for trozo, s in signal.items():
    r = radio[trozo]
    n = NUMBER_OF_SAMPLES[trozo] //r
    transformed_binary_signal[trozo] = {}
    for neuron in NEURONS:
        transformed_binary_signal[trozo][neuron] = [ 
            max( binary_signal[trozo][neuron][i*r : (i+1)*r]) 
            for i in range(0, n)
        ]
