# Bibliotecas
import pandas as pd # Lectura de datos
import matplotlib.pyplot as plt # Dibujo de las gráficas 
import numpy as np # Matrix operations
from utils.get_threshold_graph import get_threshold_count

data_path = './DatosSinapsisArtificial/'
fileTrozoC , fileTrozoG, fileTrozoR = map( 
    lambda letra: data_path+'Trozo'+ letra + '.txt',
    "C G R".split()
    )
# Leemos fichero trozoC
print('Cargando datos')
trozoC = pd.read_csv( 
    fileTrozoC, 
    names = ["LP", "VD"], 
    delimiter = "\t", 
    skiprows = range(3), 
    index_col = False, 
    decimal = ","
)


## Data information 
sample_interval = 0.1
samples_per_channel_trozoC = 19847700
samples_per_channel_trozoG = 16384000
samples_per_channel_trozoR = 16384000

LP = "LP"
x_trozoC = sample_interval * np.arange(start=0, stop=samples_per_channel_trozoC)
slice = samples_per_channel_trozoC
x = x_trozoC[0:slice]
signal = trozoC[LP].to_list()[:slice]
#plt.plot(x, signal)
#plt.show()
#https://es.wikipedia.org/wiki/Distribución_normal#Desviación_t%C3%ADpica_e_intervalos_de_confianza
deviations = [
    1.28, 1.64, 1.95, 
    2.576, 2.807, 3.090,
     3.29052, 3.8906, 
     4.4172
]
results = get_threshold_count(signal, deviations)

'''
img_path = '../Memoria/img/thresholds/trozoC/LP/'
print('Sacando gráficos')
#[1,1.28, 1.64, 1.95]
get_threshold_graph(x , l, img_path,[1, 1.64], show_graph=True)
'''
