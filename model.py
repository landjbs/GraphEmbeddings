import numpy as np
import tensorflow as tf

def gen_data(dLen, mainNodes):
    assert dLen >= (mainNodes**2), 'dLen should be geq than main nodes squared'
    dataMatrix = np.random.zeros(shape=(dLen, dLen))
    cityLocs = np.random.randint(low=0, high=(dLen**2), size=mainNodes)
    while len(set(cityLocs)) < mainNodes:
        cityLocs.append(np.random.randint(0, (dLen**2), size=mainNodes))
    return np.
