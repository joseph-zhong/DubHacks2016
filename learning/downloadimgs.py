import sys
import os
import urllib

file = open('listOfImgs', 'r')
count = len(os.listdir('imgs'))
for line in file:
  count += 1
  print "imgs/%s.jpg" % count
  try:
    urllib.urlretrieve(line, os.path.basename("./imgs/%s.jpg" % count))
  except IOError:
    print "IOError"