import cv2
import numpy as np
import matplotlilb.pyplot as plt

# get MS Cognitive Services data in JSON form for confused faces
# parse data into array of seven elements

a = [] #array of 8 diff emotional scores

n_neighbors = 10

p1 = []
p2 = []
p3 = []
p4 = []

for i in a:
    p1.append([i[0], i[1]], 1)
    p2.append([i[2], i[3]], 1)
    p3.append([i[4], i[5]], 1)
    p4.append([i[6], i[7]], 1)

# get MS data for non-confused faces

b = [] #array of 8 diff emotional scores

for j in b:
    p1.append([j[0], j[1]], 0)
    p2.append([j[1], j[2]], 0)
    p3.append([j[4], j[5]], 0)
    p4.append([j[6], j[7]], 0)

# p1, p2, p3, and p4 are arrays of [trainingData, responses] where trainingData is a listof [x,y]
#    and responses is either 0 or 1

newcomer = [] #[[t11, t12], [t21, t22], [t31, t32], [t41, t42]]
knn = cv2.KNearest()
knn.train(list(map(lambda x: x[0], p1)), list(map(lambda x: x[1], p1)))
ret, results, neighbours, dist = knn.find_nearest(newcomer, n_neighbors)
