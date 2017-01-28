import csv
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from Tkinter import Tk
from tkFileDialog import askopenfilenames
import os

#Read IMU data from csv
feature_dict = ['emg1', 'emg2', 'emg3', 'emg4', 'emg5', 'emg6', 'emg7', 'emg8']
labels = []
X_data = []
y_data = []
Tk().withdraw()
filenames = askopenfilenames(title='Choose files')
for filename in filenames:
	with open(filename, 'r') as f:
		reader = csv.reader(f)
		f.next()
		dataclass = os.path.basename(filename).replace('_emg.csv','')
		labels.append(dataclass)
		for row in reader:
			X_data.append([float(i) for i in row[1:]])
			y_data.append(dataclass)
X = np.array(X_data)
y = np.array(y_data)
		
#Exploratory visualization
'''with plt.style.context('seaborn-whitegrid'):
	plt.figure(figsize=(8, 4))
	for cnt in range(8):
		plt.subplot(2, 4, cnt + 1)
		for lab in labels:
			plt.hist(X[y == lab, cnt], label = lab, bins = 10, alpha = 0.3,)
		plt.xlabel(feature_dict[cnt])
		plt.legend(loc = 'upper right', fancybox = True, fontsize = 8)
	plt.tight_layout()
	plt.show()'''
	
#Data normalization
X_std = StandardScaler().fit_transform(X)
	
#PCA
pca = PCA(n_components = 2)
Y_sklearn = pca.fit_transform(X_std)
cols = ['blue', 'red', 'green']
with plt.style.context('seaborn-whitegrid'):
	plt.figure(figsize=(8, 4))
	for lab, col in zip(labels, cols[0:len(labels)]):
		plt.scatter(Y_sklearn[y == lab, 0], Y_sklearn[y == lab, 1], label = lab, alpha = 0.3, c = col,)
	plt.legend(loc = 'lower center', fancybox = True)
	plt.xlabel('PC1')
	plt.ylabel('PC2')
	plt.tight_layout()
	plt.show()