from sklearn import tree

s1 = []
#s1 is a collection of confused people's expressions, a listof dict of dict. Example below:
#[{"faceRectangle": {"width": 109, "top": 46, "left": 33, "height": 109}, "scores": {"sadness": 2.90334774e-05, "neutral": 0.00651574042, "contempt": 0.523489058, "disgust": 0.09046922, "anger": 0.379367054, "surprise": 4.37496565e-05, "fear": 1.00170464e-05, "happiness": 7.611594e-05}},
#{"faceRectangle": {"width": 62, "top": 45, "left": 129, "height": 62}, "scores": {"sadness": 0.113303773, "neutral": 0.853158, "contempt": 0.01196574, "disgust": 0.000523155148, "anger": 0.000127134219, "surprise": 0.0093042925, "fear": 0.0115389889, "happiness": 7.892302e-05}},
s2 = []
#s2 is like s1 but with the non-confused data sets
#[{"faceRectangle": {"width": 80, "top": 100, "left": 60, "height": 80}, "scores": {"sadness": 0.04439014, "neutral": 0.0269380286, "contempt": 0.0003618349, "disgust": 0.00420662528, "anger": 0.0133874584, "surprise": 0.008364636, "fear": 0.000818703556, "happiness": 0.9015326}},
#{"faceRectangle": {"width": 83, "top": 53, "left": 129, "height": 83}, "scores": {"sadness": 0.0149835153, "neutral": 0.204278871, "contempt": 0.00396447768, "disgust": 0.004335659, "anger": 0.007595688, "surprise": 0.003997222, "fear": 0.00222551054, "happiness": 0.75861907}}]

X = []
Y = []

for i in s1:
    ListofScores = [i["scores"]["sadness"], i["scores"]["neutral"], i["scores"]["contempt"], i["scores"]["disgust"], i["scores"]["anger"], i["scores"]["surprise"], i["scores"]["fear"], i["scores"]["happiness"]]
    X.append(ListofScores)

# for confused faces
for k in X:
    Y.append(1)

for j in s2:
    ListofScores = [j["scores"]["sadness"], j["scores"]["neutral"], j["scores"]["contempt"], j["scores"]["disgust"], j["scores"]["anger"], j["scores"]["surprise"], j["scores"]["fear"], j["scores"]["happiness"]]
    X.append(ListofScores)

count = len(s1)

# for non-confused faces
while count < len(X):
    Y.append(0)
    count += 1

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# read test input MS cognitivie services json results
q = []
testarray = [[q["scores"]["sadness"], q["scores"]["neutral"], q["scores"]["contempt"], q["scores"]["disgust"], q["scores"]["anger"], q["scores"]["surprise"], q["scores"]["fear"], q["scores"]["happiness"]]]
#sample test array: [0.00000190023718,0.0000281295361,0.0000101891646,0.0002911696,0.09596056,0.00334733119,0.00000427461237,.9003565]

#output
retval = clf.predict_proba([[]])
# sample test array as input
# sample retval: [[ 0.  1.]]
# [[confidence lvl, 1 being confused, 0 being non-confused]]
return retval
