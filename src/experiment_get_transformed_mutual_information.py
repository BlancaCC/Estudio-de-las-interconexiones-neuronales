""" 
"""
import sys

from signal_to_binary import binary_signal  
from constants import  NEURONS
from formulas import mutual_information


# Global variables
bits = list(range(1,9))


## Read signal 
if(len(sys.argv) == 1):
    print ('| trozo | window | bits | stride | IM(LP,VD) |   ')
    print('| :-: | :-: | :-: | :-: | :-: |  ')
    for trozo in "C R G".split():
        for b in bits:
            stride = [b]
            for s in stride:
                if s <= b:
                    MI = mutual_information(
                        transformed_binary_signal[trozo][NEURONS[0]],
                        transformed_binary_signal[trozo][NEURONS[1]],
                        b,
                        s
                        )
                    print(f' | {trozo}| {b} | {s} | {MI} |  ')

else:
    
    for trozo in sys.argv[1:] :
        print ('| trozo | bits | stride | IM(LP,VD) |   ')
        print('| :-: | :-: | :-: | :-: | ')
        for b in bits:
            stride = [b]
            for s in stride:
                    if s <= b:
                        MI = mutual_information(
                            binary_signal[trozo][NEURONS[0]],
                            binary_signal[trozo][NEURONS[1]],
                            b,
                            s
                            )
                        print(f' | {trozo}| {b} | {s} | {MI} |  ')           
                


