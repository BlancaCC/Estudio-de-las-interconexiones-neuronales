import numpy as np

THRESHOLD = { 
    'C': {
        "LP": {
            'lower': -0.320,
            'upper': 0.402
        },
        'VD':{
            'lower': -0.084,
            'upper':  0.205 
        }
    },
    'R': {
        "LP": {
            'lower': -0.534, 
            'upper': 0.920
        },
        'VD':{
            'lower': -0.085, 'upper': 0.206 
        }
    },
    'G': {
        "LP": {
            'lower': -0.316,
            'upper': 0.397
        },
        'VD':{
            'lower': -0.12,
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