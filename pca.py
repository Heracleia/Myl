import csv
import numpy as np
from sklearn.decomposition import PCA

data = []
filename = 'imu_reduced'
with open(filename + '.csv', 'r') as f:
	reader = csv.reader(f)
	next(f)
	for row in reader:
		data.append([float(i) for i in row[1:]])
pca = PCA(n_components=2)
pca.fit(np.array(data))
print(pca.explained_variance_ratio_)