import sys
import os
import urllib

file = open('1029384710239847', 'r')
count = len(os.listdir('notConfusedImgs'))
for line in file:
  count += 1
  print "notConfusedImgs/%s.jpg" % count
  try:
    urllib.urlretrieve(line, os.path.basename("./notConfusedImgs/%s.jpg" % count))
  except IOError:
    print "IOError"