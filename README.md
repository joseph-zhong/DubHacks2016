# DubHacks2016

Face Sentiment Analysis to Improve Education



## General

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
- MSFT Cognitive API
  - Face Recognition
  - Emotion Analysis
- MongoDB
  - Student Profile
- UI
  - Webapp
  - Hololens AR livestream

### MVP 

1. Detect # of faces
2. Read sentiment analysis on faces
3. Compute "Confusion Score" on faces
4. Upstream student profile and attribute confusion score
5. Render UI in HL

### Future Features

1. Student Profile Webapp
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
