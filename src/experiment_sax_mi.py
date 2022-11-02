"""
Cálculo de la información Mutua es SAX
 
"""
"""
Get mutual information for
"""
import sys

from read_data import signal
from constants import  NEURONS
from formulas import mutual_information
from SAX import SAX 

# Recordando al tamaño en que se reduce
words = {
    'C': [11,87,187], #[1,2,11,87,187],
    'R':[17,42,125],
    'G' : [66, 93,248]#[1, 2, 66, 93,248]
}
# Algunos ejemplo de alfabeto
alphabet = [1,2,5,10,20,50]
bits = [1,2,3,4,5,6,7,8]

## Read signal 
if(len(sys.argv) == 1):
    trozos = "C R G".split()
else:
    trozos = sys.argv[1:]
print ('| trozo | bits | words | alphabet size | IM(LP,VD) |   ')
print('| :-: | :-: | :-: | :-: | :-: |')
for trozo in trozos: 
    for a in alphabet:
        for w in words[trozo]:
            sax_signal_0 = SAX(
                signal=signal[trozo][NEURONS[0]].to_list(),
                word_size=w,
                alphabet_size=a
            )
            sax_signal_1 = SAX(
                signal=signal[trozo][NEURONS[1]].to_list(),
                word_size=w,
                alphabet_size=a
            )
            for b in bits:
                MI = mutual_information(
                    sax_signal_0,
                    sax_signal_1,
                    b,
                    b
                    )
                print(f' | {trozo}| {b} | {w} | {a} | {MI} |  ')

    
            


