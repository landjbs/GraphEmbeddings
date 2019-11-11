import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

class City(object):
    """ cities are kernels centered at x, y with routeNum routes to others """
    def __init__(self, x, y, kernel, routeNum):
        self.x = x
        self.y = y
        self.kernel = kernel
        self.routeNum = routeNum


def gen_city(mapLen, kernelSize):
    """ Generates city object on map of mapLen**2 and kernel  """



def gen_data(dLen, cityNum):
    # assert and init data matrix
    assert (dLen**2) >= cityNum, 'dLen squared should be geq than cityNum'
    dataMatrix = np.zeros(shape=(dLen, dLen))
    # city loc assignment
    cityIdx = dict()
    skipNum = 0
    curId =


    for i in range(cityNum + skipNum):
        x, y = np.random.randint(0, dLen), np.random.randint(0, dLen)
        if (x, y) in cityDict:
            skipNum += 1
            continue
        # suburbLocs = np.random.choice()
        connectionNum = np.random.randint(0, cityNum)
        cityDict.update({(x, y): connectionNum})
    # route hubs
    cityIds = list(range(len(cityDict.keys())))
    routeList = list()
    for fromLoc, connectionNum in cityDict.items():
        toIds = np.random.choice(cityIds, size=connectionNum, replace=False)
        for



    dataMatrix[finalX, finalY] = 10
    return dataMatrix

for _ in range(5):
    plt.imshow(gen_data(10, 4))
    plt.show()
