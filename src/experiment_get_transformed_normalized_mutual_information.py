"""
Muestra una tabla con las distintas Informaciones mutuas normalizadas
"""
import sys

from signal_to_binary import transformed_binary_signal
from constants import NEURONS
from formulas import normalized_mutual_information

binary_signal = transformed_binary_signal
# Global variables
bits = list(range(1, 9))


# Si no se introducen argumentos al llamar el programa calcula la información mutua
# para todos los ficheros
print('| trozo | bits | stride | IM(LP,VD) | E(LP -> VD)| E( VD -> LP) |  ')
print('| :-: | :-: | :-: | :-: | :-: | :-: | ')

if (len(sys.argv) == 1):
    trozos = "C R G".split()
else: 
    trozos =  sys.argv[1:]

for trozo in trozos:
    for b in bits:
        stride = [b]
        for s in stride:
            if s <= b:
                MI, E_XY, E_YX  = normalized_mutual_information(
                    binary_signal[trozo][NEURONS[0]],
                    binary_signal[trozo][NEURONS[1]],
                    b,
                    s
                )
                print(f' | {trozo}| {b} | {s} | {MI} | {E_XY} | {E_YX} |  ')

 