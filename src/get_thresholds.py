"""
Este fichero contiene las funciones pertinentes para la determinación de umbrales. 
Las funciones que contienen son: 
- `get_threshold_count`: *spikes* detectados para cierto umbral.
- `get_threshold_graph`: saca las gráficas con los umbrales
"""
from src.signal_to_binary import signal_to_binary
import numpy as np
import matplotlib.pyplot as plt # Dibujo de las gráficas 


def get_threshold_count(signal:list[float], std_steps:list[float], name:str)->list[list[float]]:
    '''Devuelve una lista de listas  con el:
      i) threshold inferior, 
      ii) umbral superior,
      iii) número de spikes
    Argumentos: 
    - `signal` lista de la señal
    - `std_lisps` lista de modificaciones del std
    '''
    mean = np.mean(signal)
    std = np.std(signal)

    thresholds_and_spikes_count = dict()
    print(name)
    print(' Distancia del umbral bajo | Distancia alta | Umbral bajo| Umbral alto| Número de *spikes*')
    print(':-: |' * 4 + ':-:   ')
    cnt = 0
    for step in std_steps: 
        lower_threshold = mean - step * std
        for step_upper in std_steps: 
            upper_threshold = mean + step_upper * std 
            spikes_detected = signal_to_binary(signal, lower_threshold, upper_threshold)
            number_of_spikes = spikes_detected.count(1)
            thresholds_and_spikes_count[(lower_threshold,upper_threshold)]= number_of_spikes
            print(f'{step} | {step_upper}| {lower_threshold:.3f} | {upper_threshold:.3f} | {number_of_spikes}  ')

            cnt+=1
    return thresholds_and_spikes_count




"""
path_images = '../Memoria/img/thresholds/'
slice = 1000
l = trozoC[LP].to_list()[:slice]
X = x_trozoC[0:slice] 
"""
def get_threshold_graph(X, l,path_images, std_step = [1,1.28, 1.64, 1.95, 2.32],show_graph=False):
    ''' Saca gráficas de señal y umbral a partir de la desviación típica. 
    Parámetros: 
    - `l` se corresponde a la señal.
    - `X` instante de tiempo en que se midió tal señal.
    - `path_images`: contiene la ruta y el nombre con el que se van a guardar.
    - `std_step`: Los coeficientes con los que se calcularán.
    '''
    mean = np.mean(l)
    std = np.std(l)
    print(mean, std)
    #plt.figure(figsize=(10,10))

    # Experimento 
    # sigmas source: https://es.wikipedia.org/wiki/Distribución_normal#Desviación_t%C3%ADpica_e_intervalos_de_confianza
    #0,80    1,28155
    #0,90	1,64485
    #0,95	1,95996
    #0,98	2,32635
    #0,99	2,57583
    #0,995	2,80703
    #0,998	3,09023
    
    tries = len(std_step) 
    number_of_spikes_matrix = list(np.zeros((tries, tries)))
    for i,lower_step in enumerate(std_step):
        lower_threshold = mean - std*lower_step
        # Vamos a suponer que hay simetría 
        for j,upper_step in enumerate([lower_step]):#enumerate(std_step):
            name = path_images+f'sl{lower_step}su{upper_step}.png'
            upper_threshold = mean + std*upper_step
            spikes_detected = signal_to_binary(l, lower_threshold, upper_threshold)
            
            index_with_spike = list(filter(
                lambda x: spikes_detected[x] == 1,
                list(range(len(l)))
                ))
            number_of_spikes = len(index_with_spike)
            number_of_spikes_matrix[i][j] = number_of_spikes
            title = f'$\sigma_l$ ={lower_step}, $\sigma_u$={upper_step} number of spikes={number_of_spikes}'
            print(title)
        
            plt.plot(X, l, label='Signal')
            plt.plot(X,[upper_threshold for i in X], label='upper threshold')
            plt.plot(X,[lower_threshold for i in X], label='upper threshold')
            plt.scatter([X[i] for i in index_with_spike],[l[i] for i in index_with_spike], label='spike')
            #plt.legend()
            plt.title(title) 
            plt.savefig(name)
            plt.show()

def plotThreshold(X, l,path_images_and_name, lower_threshold, upper_threshold,show_graph=False):

    spikes_detected = signal_to_binary(l, lower_threshold, upper_threshold)
    index_with_spike = list(filter(
                    lambda x: spikes_detected[x] == 1,
                    list(range(len(l)))
                    ))
    plt.plot(X, l, label='Signal')
    plt.plot(X,[upper_threshold for i in X], label='Upper threshold')
    plt.plot(X,[lower_threshold for i in X], label='Lower threshold')
    plt.scatter([X[i] for i in index_with_spike],[l[i] for i in index_with_spike], label='spike')
    #plt.legend()
    #plt.title(title) 
    plt.savefig(path_images_and_name)
    plt.show()

