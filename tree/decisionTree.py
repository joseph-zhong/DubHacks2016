from firebase import Firebase
import os
import sys
import json

import datetime
from sklearn import tree
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify

#### Decision Tree initialization steps
global _clf

def init_tree():
  confused_json_file = open('confused.json')
  confused_json = json.load(confused_json_file)
  # confused_json = []
  #s1 is a collection of confused people's expressions, a listof dict of dict. Example below:
  #[{'faceRectangle': {'width': 109, 'top': 46, 'left': 33, 'height': 109}, 'scores': {'sadness': 2.90334774e-05, 'neutral': 0.00651574042, 'contempt': 0.523489058, 'disgust': 0.09046922, 'anger': 0.379367054, 'surprise': 4.37496565e-05, 'fear': 1.00170464e-05, 'happiness': 7.611594e-05}},
  #{'faceRectangle': {'width': 62, 'top': 45, 'left': 129, 'height': 62}, 'scores': {'sadness': 0.113303773, 'neutral': 0.853158, 'contempt': 0.01196574, 'disgust': 0.000523155148, 'anger': 0.000127134219, 'surprise': 0.0093042925, 'fear': 0.0115389889, 'happiness': 7.892302e-05}},

  non_confused_json_file = open('non_confused.json')
  non_confused_json = json.load(non_confused_json_file)
  # non_confused_json = json.loads("[{\"faceRectangle\": {\"width\": 80, \"top\": 100, \"left\": 60, \"height\": 80}, \"scores\": {\"sadness\": 0.04439014, \"neutral\": 0.0269380286, \"contempt\": 0.0003618349, \"disgust\": 0.00420662528, \"anger\": 0.0133874584, \"surprise\": 0.008364636, \"fear\": 0.000818703556, \"happiness\": 0.9015326}},{\"faceRectangle\": {\"width\": 83, \"top\": 53, \"left\": 129, \"height\": 83}, \"scores\": {\"sadness\": 0.0149835153, \"neutral\": 0.204278871, \"contempt\": 0.00396447768, \"disgust\": 0.004335659, \"anger\": 0.007595688, \"surprise\": 0.003997222, \"fear\": 0.00222551054, \"happiness\": 0.75861907}}]")

  #s2 is like s1 but with the non-confused data sets
  #[{'faceRectangle': {'width': 80, 'top': 100, 'left': 60, 'height': 80}, 'scores': {'sadness': 0.04439014, 'neutral': 0.0269380286, 'contempt': 0.0003618349, 'disgust': 0.00420662528, 'anger': 0.0133874584, 'surprise': 0.008364636, 'fear': 0.000818703556, 'happiness': 0.9015326}},
  #{'faceRectangle': {'width': 83, 'top': 53, 'left': 129, 'height': 83}, 'scores': {'sadness': 0.0149835153, 'neutral': 0.204278871, 'contempt': 0.00396447768, 'disgust': 0.004335659, 'anger': 0.007595688, 'surprise': 0.003997222, 'fear': 0.00222551054, 'happiness': 0.75861907}}]

  list_of_scores = []
  list_of_labels = []

  for i in confused_json:
      score_list = [i['scores']['sadness'], i['scores']['neutral'], i['scores']['contempt'], i['scores']['disgust'], i['scores']['anger'], i['scores']['surprise'], i['scores']['fear'], i['scores']['happiness']]
      list_of_scores.append(score_list)
      list_of_labels.append(1)
  # # for confused faces
  # for k in list_of_scores:
  #     list_of_labels.append(1)

  for j in non_confused_json:
      score_list = [j['scores']['sadness'], j['scores']['neutral'], j['scores']['contempt'], j['scores']['disgust'], j['scores']['anger'], j['scores']['surprise'], j['scores']['fear'], j['scores']['happiness']]
      list_of_scores.append(score_list)
      list_of_labels.append(0)

  global _clf
  _clf = tree.DecisionTreeClassifier()
  _clf = _clf.fit(list_of_scores, list_of_labels)


def run_inference(in_meta):
  firebase = firebase.FirebaseApplication('https://dubhacks2016-e1d3e.firebaseio.com', None)
  """

  :param in_meta: single face metadata dict with 'scores' with
        'sadness'
        'neutral'
        'contempt'
        'disgust'
        'anger'
        'surprise'
        'fear'
        'happiness'
  :return: [[non_confused_confidence, confused_confidence]]
  """
  # read test input MS cognitivie services json results
  # in_meta = []
  # in_meta = [[in_meta['scores']['sadness'], in_meta['scores']['neutral'], in_meta['scores']['contempt'], in_meta['scores']['disgust'], in_meta['scores']['anger'], in_meta['scores']['surprise'], in_meta['scores']['fear'], in_meta['scores']['happiness']]]
  # in_meta = [0.00000190023718,0.0000281295361,0.0000101891646,0.0002911696,0.09596056,0.00334733119,0.00000427461237,.9003565]
  # in_meta = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
  # in_meta = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
  #sample test array: [0.00000190023718,0.0000281295361,0.0000101891646,0.0002911696,0.09596056,0.00334733119,0.00000427461237,.9003565]

  #output
  global _clf

  out_meta = []
  for face in in_meta:
    score = [
              face['scores']['sadness'],
              face['scores']['neutral'],
              face['scores']['contempt'],
              face['scores']['disgust'],
              face['scores']['anger'],
              face['scores']['surprise'],
              face['scores']['fear'],
              face['scores']['happiness']
            ]



    retval = _clf.predict_proba(score)
    face['isConfused'] = bool(retval[0][1])
    face['timeStamp'] = datetime.datetime.now().isoformat()
    result = firebase.post('/algoRetVal', [face['isConfused'], face['timeStamp']])
    out_meta.append(face)
    

    
  print out_meta
  try:
    ret = jsonify(results=out_meta)
    return ret
  except AssertionError:
    return jsonify(results=in_meta)



init_tree()
# run_inference([0.00011789846, 0.0000228391418, 0.0180042554, 4.828176e-7, 0.9683092, 0.0117861256, 0.000459061179, 0.00130010839])

# initialize the Flask app
app = Flask(__name__)
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/', methods=['GET'])
def qwer():
  return 'hello'


@app.route('/predictConfusion', methods=['POST'])
def predictConfusion():
  in_meta = json.loads(request.data.decode())
  print in_meta
  return run_inference(in_meta)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)

