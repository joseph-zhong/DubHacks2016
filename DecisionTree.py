from sklearn import tree

# parse data from MS Cognitive Services API
n = [] # input needs to be a listof float for each pic

X = []
X.append(n)

# for confused faces
Y.append(1)

# for non-confused faces
Y.append(0)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

#output
retval = clf.predict_proba([[test val]])
