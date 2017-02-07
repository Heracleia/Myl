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
		data.append([float(line[0]), float(line[1])]);
data = np.asarray(data)
		
prediction = clf.predict(data)
print(np.mean(prediction))