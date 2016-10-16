import sys
import os
import urllib

file = open('listOfImgs', 'r')
count = len(os.listdir('confusedImgs'))
for line in file:
  count += 1
  print "confusedImgs/%s.jpg" % count
  try:
    urllib.urlretrieve(line, os.path.basename("./confusedImgs/%s.jpg" % count))
  except IOError:
    print "IOError"