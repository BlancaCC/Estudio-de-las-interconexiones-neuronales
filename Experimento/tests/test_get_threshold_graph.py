from numpy import arange
from utils.get_threshold_graph import get_threshold_graph
import numpy as np

def test_get_threshold_graph(): 
    x = np.arange(0,10,0.1)
    y = np.sin(x)
    get_threshold_graph(x,y,'tests/img/', [0.1, 0.2])