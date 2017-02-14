import csv
from matplotlib import pyplot as plt
from sklearn import svm
from sklearn.externals import joblib
from Tkinter import Tk
from tkFileDialog import askopenfilename
import numpy as np

data = []
Tk().withdraw()
filename = askopenfilename(title='Choose file to train')
with open(filename, 'r') as f:
	reader = csv.reader(f)
	for line in reader:
		data.append([float(line[0]), float(line[1])]);
data = np.asarray(data)
		
print('Training...')
clf = svm.OneClassSVM(nu=0.5, gamma=0.1)
clf.fit(data[0:1000])

joblib.dump(clf, filename.replace('.csv', '.pkl'))