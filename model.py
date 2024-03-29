import math
import numpy as np
import tensorflow as tf
from scipy.stats import norm
from scipy.special import softmax
import matplotlib.pyplot as plt

ZERO_BOOST = 0.0000001

class City(object):
    ''' Cities are kernels centered at x, y with routeNum routes to others '''
    def __init__(self, id, x, y, kernel, routeNum):
        self.id = id
        self.x = x
        self.y = y
        self.kernel = kernel
        self.routeNum = routeNum

    def __str__(self):
        return f'<City Object {self.id} | x={self.x} y={self.y}>'

    def show(self):
        plt.imshow(kernel)
        plt.title(f'{self.id} at ({self.x}, {self.y})')


class Map(object):
    '''
    A map stores a hash of cities, a tensor of the whole map, and methods
    for ML embeddings and regression
    '''
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.channelNames = ['population', 'transport', 'temperature']
        self.cityIdx = {}
        self.roadIdx = {}
        self.mapTensor = np.zeros((length, length, len(self.channelNames)))

    def populate(self, cityNum):
        ''' Populates map with cityNum cities '''
        # x and y locs give lower right corner
        xLocs = np.random.randint(0, self.length, size=cityNum)
        yLocs = np.random.randint(0, self.length, size=cityNum)
        kernelSizes = np.random.randint(3, np.ceil(self.length/10),
                                        size=cityNum)
        populations = np.random.randint(0, 255, size=cityNum)
        routeNums = np.random.randint(0, cityNum, size=cityNum)
        # set populations and generate city idx
        for id, loc in enumerate(zip(xLocs, yLocs)):
            x, y = loc[0], loc[1]
            curLen, curPop = kernelSizes[id], populations[id]
            cityCenter = curLen / 2
            cityKernel = np.zeros(shape=(curLen, curLen))
            for i in range(curLen):
                for j in range(curLen):
                    curDist = np.sqrt((cityCenter-i)**2 + (cityCenter-j)**2)
                    locPop = curPop/norm.cdf(curDist)
                    cityKernel[i, j] = locPop
            curCity = City(id, x, y, cityKernel, routeNums[id])
            print(cityKernel.shape, self.mapTensor[x:(x+curLen), y:(y+curLen), 0].shape)
            self.mapTensor[x:(x+curLen), y:(y+curLen), 0] += cityKernel[0]

        plt.imshow(self.mapTensor)
        plt.show()

x = Map('NuckTown', 100)
x.populate(10)

# def gen_city(mapLen):
#     """ Generates city object on map of mapLen**2 """
#     # decide location of city
#     x, y = np.random.randint(0, mapLen), np.random.randint(0, mapLen)
#     # decide population of city
#     pop = np.random.randint(10000, 10**6)
#     # decide kernel size of city
#     kernelSize = np.random.randint(1, int(mapLen/10))
#
#
#
#
#
# def gen_data(dLen, cityNum):
#     # assert and init data matrix
#     assert mapLen >= 10, 'mapLen must be geq 10'
#     assert (dLen**2) >= cityNum, 'dLen squared should be geq than cityNum'
#     dataMatrix = np.zeros(shape=(dLen, dLen))
#     # city loc assignment
#     cityIdx = dict()
#     skipNum = 0
#     curId =
#
#
#     for i in range(cityNum + skipNum):
#         x, y = np.random.randint(0, dLen), np.random.randint(0, dLen)
#         if (x, y) in cityDict:
#             skipNum += 1
#             continue
#         # suburbLocs = np.random.choice()
#         connectionNum = np.random.randint(0, cityNum)
#         cityDict.update({(x, y): connectionNum})
#     # route hubs
#     cityIds = list(range(len(cityDict.keys())))
#     routeList = list()
#     for fromLoc, connectionNum in cityDict.items():
#         toIds = np.random.choice(cityIds, size=connectionNum, replace=False)
#         for
#
#
#
#     dataMatrix[finalX, finalY] = 10
#     return dataMatrix
#
# for _ in range(5):
#     plt.imshow(gen_data(10, 4))
#     plt.show()
