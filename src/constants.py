import numpy as np

THRESHOLD = { 
    'C': {
        "LP": {
            'lower': -0.211,
            'upper': 0.402
        },
        'VD':{
            'lower': -0.041,
            'upper':  0.205 
        }
    },
    'R': {
        #1.4 | 1.956| -0.306 | 0.348 | 52341 
        "LP": {
            'lower': -0.306, 
            'upper':  0.348 
        }, # correcto
        'VD':{
            'lower':-0.085 , 
            'upper': 0.206
        }
    },
    'G': {
      #  5.326 | 5.326| -0.432 | 0.432 | 2021
        "LP": {
            'lower': -0.432,
            'upper': 0.75
        },
        # 3.891 | 4.892| -0.087 | 0.207 | 15571  
        'VD':{
            'lower': -0.085 ,
            'upper': 0.207
        }
    }
}

NUMBER_OF_SAMPLES = {
    'C' : 19847700,
    'G' : 16384000,
    'R' : 16384000
}
SAMPLE_INTERVAL= 0.1

RANGE = dict(
    map(
        lambda trozo: (
            trozo, 
                SAMPLE_INTERVAL * np.arange(start=0, stop=NUMBER_OF_SAMPLES[trozo])
            )
        ,
        ['C', 'G', 'R']
    )
)

data_path  = './DatosSinapsisArtificial/'
fileTrozoC , fileTrozoG, fileTrozoR  =  map( 
    lambda letra: data_path+'Trozo'+ letra + '.zip',
    "C R G".split()
    )

FILES_NAMES = {
    'C': fileTrozoC,
    'G' : fileTrozoG,
    'R' : fileTrozoR
}

NEURONS = ["LP", "VD"]
ALL_COLUMNS = ["LP", "VD", "GABAInjection"]