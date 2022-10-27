import numpy as np
from random import randint
import matplotlib.pyplot as plt # Dibujo de las gráficas 

try:
    from src.constants import THRESHOLD, NUMBER_OF_SAMPLES, SAMPLE_INTERVAL, RANGE
    from src.get_thresholds import plotThreshold
    from src.read_data import signal
except:
    from constants import THRESHOLD, NUMBER_OF_SAMPLES, SAMPLE_INTERVAL, RANGE
    from get_thresholds import plotThreshold
    from read_data import signal

def plotFinalThreshold(slice: int, trozos:list[str] = ['C', 'R', 'G'], neurons:list[str]  = ['LP', 'VD'], number_of_images:int = 2, img_path:str = "img/04_calculo_spikes/"):
    '''plot and save a random part of a signal  and neuron
    Params: 
    `slice` size of the X graph
    `trozos`: list of the letters of the *trozo* must be element of `['C', 'R', 'G']`.
    `neurons`: neurons must be elements of `['LP', 'VD']`
    `number_of_images`: number of random images
    `img_path`: path t save the images
    ``
    '''
    plt.ion()
    for trozo in trozos:
        for neuron in neurons:
            upper_threshold =  THRESHOLD[trozo][neuron]['upper'] 
            lower_threshold  = THRESHOLD[trozo][neuron]['lower'] 

            initial_values = [randint(0,NUMBER_OF_SAMPLES[trozo]-2) for i in range(number_of_images)]
            for init in initial_values:
                name = img_path+f'3_trozo_{trozo}_neuron_{neuron}_init_{init}_{lower_threshold}_ {upper_threshold}.png'
                title = f'For signal {trozo} neuron {neuron} on [{init}, {init+slice}] '#with thresholds({lower_threshold} and {upper_threshold})'
                plotThreshold(
                    RANGE[trozo][init:slice+init],
                    (signal[trozo][neuron].to_list())[init:slice+init], 
                        name,
                        lower_threshold,
                        upper_threshold,
                        title)


if __name__ == '__main__':
    plotFinalThreshold(8000, number_of_images= 6)