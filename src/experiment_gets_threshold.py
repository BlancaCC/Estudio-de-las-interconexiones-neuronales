from read_data import read_data
from get_thresholds import get_threshold_count


### Variables globales

data_path = './DatosSinapsisArtificial/' # dirección de los datos
distances = [1.281, 1.645, 1.4, 1.956, 2.57,3.891,4.892, 5.326 ]
trozos_files = list(
    map( 
    lambda letra: data_path+'Trozo'+ letra + '.zip',
    "C R G".split()
    )
)
columns_names = ["LP", "VD"]

# Caso en que tienen dos columnas
for trozo_file in trozos_files[:-1] :
    trozo = read_data(trozo_file, columns_names)
    for neuron in columns_names:
        
        title = f"""
    =======================================================================================
        Calculando umbrales de {trozo_file} para la neurona {neuron}
    =======================================================================================
        """
        get_threshold_count(trozo[neuron].tolist(), distances, title)
        print('')

# G, la última tiene tres columnas 
trozo_file = trozos_files[-1]
trozo = read_data(trozo_file, ["LP", "VD", "GABAInjection"])
for neuron in columns_names:
    title = f"""
    =======================================================================================
        Calculando umbrales de {trozo_file} para la neurona {neuron}
    =======================================================================================
    """
    get_threshold_count(trozo[neuron].tolist(), distances, title)
    print('')
