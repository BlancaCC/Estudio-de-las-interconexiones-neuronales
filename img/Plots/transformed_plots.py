
import numpy as np
import matplotlib.pyplot as plt # Dibujo de las gráficas 
import pandas as pd

def transformed_plot(X,Y,title):
    plt.plot(X,Y,label="Información Mutua")
    plt.legend(bbox_to_anchor=(1.01,1))
    plt.tight_layout()
    plt.title(title, fontsize = 6) 
    plt.pause(0.01)
    plt.close()
    
data = pd.read_csv("transformed_mutual_information_C.txt",sep="|",header=0,skiprows=[1])
transformed_plot(data[' bits '],data[' IM(LP,VD) '],"pruebilla")