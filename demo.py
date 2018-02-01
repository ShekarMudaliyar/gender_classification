from sklearn import tree

x = [[100,80,20],[200,40,30],[120,50,22],[130,40,23],[250,10,40],[220,20,11],[122,40,33]]
y = ['female','male','female','female','male','male','female']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
prediction = clf.predict([[300,40,10]])
print(prediction)