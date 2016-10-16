from __future__ import print_function
import os
import time
import requests
import cv2
import operator
import numpy as np


# Import library to display results
import matplotlib.pyplot as plt


# Variables

_url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'
keys = ['b17d6992258e498d9de73f7425f4a230', 'c122cf34ec4e4a689c9a7ddd64863161']
_key = 'b17d6992258e498d9de73f7425f4a230'
_key = 'c122cf34ec4e4a689c9a7ddd64863161'
_maxNumRetries = 10

def processRequest( json, data, headers, params ):

  """
  Helper function to process the request to Project Oxford

  Parameters:
  json: Used when processing images from its URL. See API Documentation
  data: Used when processing image read from disk. See API Documentation
  headers: Used to pass the key information and the data type request
  """

  retries = 0
  result = None

  while True:

    response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )

    if response.status_code == 429:

      print( "Message: %s" % ( response.json()['error']['message'] ) )

      if retries <= _maxNumRetries:
          time.sleep(1)
          retries += 1
          continue
      else:
          print( 'Error: failed after retrying!' )
          break

    elif response.status_code == 200 or response.status_code == 201:

      if 'content-length' in response.headers and int(response.headers['content-length']) == 0:
        result = None
      elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str):
        if 'application/json' in response.headers['content-type'].lower():
          result = response.json() if response.content else None
        elif 'image' in response.headers['content-type'].lower():
          result = response.content
    else:
      print( "Error code: %d" % ( response.status_code ) )
      print( "Message: %s" % ( response.json()['error']['message'] ) )

    break

  return result

def renderResultOnImage( result, img ):

  """Display the obtained results onto the input image"""

  for currFace in result:
    faceRectangle = currFace['faceRectangle']
    cv2.rectangle( img,(faceRectangle['left'],faceRectangle['top']),
                       (faceRectangle['left']+faceRectangle['width'], faceRectangle['top'] + faceRectangle['height']),
                   color = (255,0,0), thickness = 5 )


  for currFace in result:
    faceRectangle = currFace['faceRectangle']
    currEmotion = max(currFace['scores'].items(), key=operator.itemgetter(1))[0]


    textToWrite = "%s" % ( currEmotion )
    cv2.putText( img, textToWrite, (faceRectangle['left'],faceRectangle['top']-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1 )

# img = os.path.expanduser('~/Development/sentiEdu/learning/imgs/4.jpg')
folder = 'imgs'
count = 0
data_file = open('data.json', 'w')
for img in os.listdir(folder):
  count += 1
  if count < 20:
    if img.endswith('.jpg'):
      with open( os.path.join(folder, img), 'rb' ) as f:
        data = f.read()

        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = _key
        headers['Content-Type'] = 'application/octet-stream'

        json = None
        params = None
        start = time.time()
        print(start)
        # result = processRequest( json, data, headers, params )
        print('-------------')
        print('request time: %s', time.time() - start)
        print(os.path.join(folder, img))
        # if result is not None:
        #   print(result)
        #   data_file.write(result)
        print('-------------')
        # Load the original image from disk
        # data8uint = np.fromstring( data, np.uint8 ) # Convert string to an unsigned int array
        # img = cv2.cvtColor( cv2.imdecode( data8uint, cv2.IMREAD_COLOR ), cv2.COLOR_BGR2RGB )

        # renderResultOnImage( result, img )

        # ig, ax = plt.subplots(figsize=(15, 20))
        # ax.imshow( img )
  else:
    time.sleep(3)
    count = 0
