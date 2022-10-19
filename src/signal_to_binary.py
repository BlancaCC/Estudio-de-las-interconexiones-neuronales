import numpy as np

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