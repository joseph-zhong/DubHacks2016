# DubHacks2016

Student Sentiment analysis for feedback to teachers

## General

- [Devpost Competition Submission](https://devpost.com/software/dubhacks2016-yvzcfb)
- *Qualtrics Best Data Visualization Award Winner!*

### Workflow

0. `learning/classification.py`, `learning/scilearn.py`, `learning/clarifai.js`, `learning/KNearest.py` and `learning/scrape.py` will not be helpful
1. `learning/Gscrape.js`: From simple Google Image searches in browser, capture the image srcs
    - `learning/1029384710239847` and `learning/listOfImgs` are examples of images to be downloaded 
2. `learning/download[NotConfused]imgs.py`: Download images
3. `learning/[notConfused]cognitiveService.py`: Generate dataset of sentiments per image
    - Generates `tree/confused.json` and `tree/non_confused.json` for building the decision tree later on
4. `learning/plot.py`: Plot sentiment values 
5. `tree/decisionTree.py`: Run server to begin reading inputs from Hololens and providing sentiment feedback!    
    - Hosted on MSFT Azure VM since Heroku did not support Scikit Learn

### Roadmap

- [learning](learning) Primarily experiment/data-mining code
    - [`Gscrape.js`](learning/Gscrape.js): Outputs image sources in current webpage (Google Images) 
    - [`test.py`](learning/test.py): Initial file to test the MSFT Cognitive API
    - [`ConfusedCognitiveService.py`](learning/ConfusedCognitiveService.py): Script to build dataset of confused samples into `tree/confused.json` and `tree/non_confused.json`
        - Simple Visualization for eye-balling whether there exists a pattern between "Confused" and "Non-confused"
            - Confused [Visualized](learning/confused.png)
            - Non-Confused [Visualized](learning/non_confused.png)
                - See [`plot.py`](learning/plot.py)
                - Each plot on the y-axis is an emotion from the Cognitive API
                    - anger, contempt, disgust, fear, happiness, neutral, sadness, surprise
                - x-axis represents value from 0 to 1
- [tree](tree) Code built off of experiments and put into the server for demoing
    - [`decisionTree.py`](tree/decisionTree.py): Server to build Sci-kit Learn decision tree
        - [`confused.json`](tree/confused.json): Confused dataset
        - [`non_confused.json`](tree/non_confused.json): Non Confused dataset

### Context

Teachers care about teaching. They want the best for the students

It can sometimes be difficult for teachers to best achieve this, and with increasing classroom sizes with more students attending college than ever before, the pressure and responsibility has never been greater. 
When students are having difficulting understanding lecture concepts, it can be difficult for teachers to consistently identify this, especially as they're focusing on the lecture concepts. At the intersection of image feature recognition as well as the revolution in Augmented and Virtual reality, we can leverage the Hololens' headset to capture student's and audience sentiment, and provide realtime feedback for the lecturer.


### Strengths

- Realtime sentiment feedback for teachers are feeling
- Database for student "Learning" Profile



## Tech

- Hololens Headset (Input)
- OpenCV API (Face Detection)
- [MSFT Cognitive API](https://www.microsoft.com/cognitive-services/en-us/emotion-api)
  - Face Recognition
  - Emotion Analysis
- [Scikit Learn](http://scikit-learn.org/)
- ~~MongoDB~~ Firebase
  - Student Profile
- UI
  - Webapp
  - Hololens AR livestream
    - (Different repository)

### MVP 

1. Detect # of faces
2. Read sentiment analysis on faces
3. Compute "Confusion Score" on faces
4. Upstream student profile and attribute confusion score
5. Render UI in HL

### Future Features

1. ~Student Profile Webapp~ Implemented!
2. Student Profile HL interaction

### Trade Off Analysis

Tech Core Problems

#### Network versus Computation 

##### Face Detection

- LBP Cascades is an extremely efficient system for feature recognition and with very little CPU time can recognize objects of interest.
- Outsourcing CPU time through MSFT Cogniitive API will then consume significant network time 

##### Face Recognition

- Implementing using OpenCV or TensorFlow 
  - Plus Training time
  - would only require several hundreds of sample images or 30fps * 10 seconds of detected frames

##### Sentiment Analysis

- Implementing ourselves from scratch is a research problem

### Pressing Concerns

- How to scale
- Why would anybody want this
  - Do Teachers really want this?
  - Do Students really want this?
- At n < 15 Teacher could out-perform the system 100% of the time
