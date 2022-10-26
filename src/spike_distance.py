from constants import NUMBER_OF_SAMPLES, NEURONS
from signal_to_binary import binary_signal
import numpy as np

print(f" Trozo | Neurona | Intervalo mínimo entre spikes | Cuantil  Media | std   ")
print(' --- | --- | ---  | --- | ---  --- | ---  ')

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


        print(f' {trozo}  | {neuron } | {minimum_distance } | {cuantil}% | {cuantil_distance} | {np.mean(index_with_spike) :.3f} | {np.std(index_with_spike):.3f}  ')
