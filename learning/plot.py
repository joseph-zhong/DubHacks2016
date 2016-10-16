import numpy as np
import matplotlib.pyplot as pp
import os
import json

data_file = open('./data.json', 'r')
for line in data_file:
  print line
  d = json.loads(line)
  print d
#
# val = 0. # this is the value where you want the data to appear on the y-axis.
# ar = np.arange(10) # just as an example array
# pp.plot(ar, np.zeros_like(ar) + val, 'x')
# pp.show()