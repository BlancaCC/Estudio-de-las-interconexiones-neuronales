from constants import NUMBER_OF_SAMPLES, NEURONS
from signal_to_binary import binary_signal
import numpy as np

print(f" Trozo | Neurona | Intervalo mínimo entre spikes | Media | std   ")
print(' --- | --- | --- | --- | ---  ')

for trozo in 'C R G'.split():
    for neuron in NEURONS:
        index_with_spike = list(filter(
                            lambda x: binary_signal[trozo][neuron][x] == 1,
                            list(range(NUMBER_OF_SAMPLES[trozo]))
                            ))

        number_of_spikes = len(index_with_spike)

        minimum_distance = min([
            index_with_spike[i+1]-index_with_spike[i]
            for i in range(number_of_spikes-1)
            ])

        print(f' {trozo}  | {neuron } | {minimum_distance } | {np.mean(index_with_spike) :.3f} | {np.std(index_with_spike):.3f}  ')
