from read_data import read_data
from get_thresholds import get_threshold_count


### Variables globales

data_path = './DatosSinapsisArtificial/' # dirección de los datos
distances = [1.956, 2.57,3.891,4.892 ]


trozos_files = list(
    map( 
    lambda letra: data_path+'Trozo'+ letra + '.zip',
    "C G R".split()
    )
)
columns_names = ["LP", "VD"]
#["LP", "VD", "GABAInjection"]

for trozo_file in trozos_files[:-1] :
    for neuron in columns_names:
        trozo = read_data(trozo_file, columns_names)
        title = f"""

        =======================================================================================
            Calculando umbrales de {trozo_file} para la neurona {neuron}
        =======================================================================================
        """
        get_threshold_count(trozo[neuron].tolist(), distances, title)
        print('')

