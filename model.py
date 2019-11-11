import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def gen_data(dLen, mainNodes):
    # assert and init data matrix
    assert (dLen**2) >= mainNodes, 'dLen squared should be geq than main nodes'
    dataMatrix = np.zeros(shape=(dLen, dLen))
    xLocs = np.random.randint(0, dLen, size=mainNodes)
    yLocs = np.random.randint(0, dLen, size=mainNodes)
    cityLocs = list(zip(xLocs, yLocs))
    while len(set(cityLocs)) < mainNodes:
        x = np.random.int(0, dLen, size=mainNodes),
        y = np.random.int(0, dLen, size=mainNodes)
        if not (x, y) in cityLocs:
            cityLocs.add((x, y))


    finalX, finalY = zip(*cityLocs)
    dataMatrix[finalX, finalY] = 10
    return dataMatrix

for _ in range(5):
    plt.imshow(gen_data(10, 4))
    plt.show()
