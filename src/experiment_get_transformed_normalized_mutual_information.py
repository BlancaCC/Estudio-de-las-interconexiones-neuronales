"""
Muestra una tabla con las distintas Informaciones mutuas normalizadas
"""
import sys

from signal_to_binary import binary_signal
from constants import NEURONS, NUMBER_OF_SAMPLES
from formulas import normalized_mutual_information

# Global variables
bits = list(range(1, 9))

window_sizes = {
    'C' : [11,87, 187],
    'R' : [17,42, 125],
    'G' : [66,93, 248]
}
# Si no se introducen argumentos al llamar el programa calcula la información mutua
# para todos los ficheros
print('| trozo | window size  | bits | stride | IM(LP,VD) | E(LP -> VD)| E( VD -> LP) |  ')
print('| :-: | :-: |  :-: | :-: | :-: | :-: | :-: | ')

if (len(sys.argv) == 1):
    trozos = "C R G".split()
else: 
    trozos =  sys.argv[1:]

for trozo in trozos:
    for w in window_sizes[trozo]:
        n = NUMBER_OF_SAMPLES[trozo] //w
        transformed_binary_signal = {}
        for neuron in NEURONS:
            transformed_binary_signal[neuron] = [ 
                max( binary_signal[trozo][neuron][i*w : (i+1)*w]) 
                for i in range(0, n)
            ]

        for b in bits:
            stride = [b]
            for s in stride:
                if s <= b:
                    MI, E_XY, E_YX  = normalized_mutual_information(
                        transformed_binary_signal[NEURONS[0]],
                        transformed_binary_signal[NEURONS[1]],
                        b,
                        s
                    )
                print(f' | {trozo}| {w} | {b} | {s} | {MI} | {E_XY} | {E_YX} |  ')

 