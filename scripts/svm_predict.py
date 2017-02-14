import csv
from matplotlib import pyplot as plt
from sklearn import svm
from sklearn.externals import joblib
from Tkinter import Tk
from tkFileDialog import askopenfilenames
import numpy as np

data = []
Tk().withdraw()
filenames = askopenfilenames(title='Choose prediction file(s), then model')
clf = joblib.load(filenames[0])
with open(filenames[1], 'r') as f:
	reader = csv.reader(f)
	for line in reader:
		data.append([float(line[0]), float(line[1])])
data = np.asarray(data)
		
prediction = clf.predict(data)
print(np.mean(prediction))

xx, yy = np.meshgrid(np.linspace(-10, 10, 1000), np.linspace(-10, 10, 1000))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title('Assembly SVM')
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='darkred')
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')
b1 = plt.scatter(data[:, 0], data[:, 1], c='g', alpha=0.1, s=40)
plt.axis('tight')
plt.xlim((-10, 10))
plt.ylim((-10, 10))
plt.show()