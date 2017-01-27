import csv
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

#Read IMU data from csv
feature_dict = []
data = []
filename = 'imu_reduced'
with open(filename + '.csv', 'r') as f:
	reader = csv.reader(f)
	feature_dict = next(f).replace('\n', '').split(',')[1:]
	for row in reader:
		data.append([float(i) for i in row[1:]])
X = np.array(data)
		
#Exploratory visualization
'''with plt.style.context('seaborn-whitegrid'):
	plt.figure(figsize=(9, 9))
	for cnt in range(9):
		plt.subplot(3, 3, cnt + 1)
		plt.hist(X[:, cnt], bins = 10, alpha = 0.3,)
		plt.xlabel(feature_dict[cnt])
	plt.tight_layout()
	plt.show()'''
	
#Data normalization
X_std = StandardScaler().fit_transform(X)
	
#PCA
pca = PCA(n_components = 2)
Y_sklearn = pca.fit_transform(X_std)
with plt.style.context('seaborn-whitegrid'):
	plt.figure(figsize=(9, 9))
	plt.scatter(Y_sklearn[:, 0], Y_sklearn[:, 1], alpha = 0.3,)
	plt.xlabel('PC1')
	plt.ylabel('PC2')
	plt.tight_layout()
	plt.show()