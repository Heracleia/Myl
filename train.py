import csv
import numpy as np
from sklearn import svm
from sklearn.externals import joblib

data = []
filename = 'imu_reduced'
with open(filename + '.csv', 'rb') as f:
	reader = csv.reader(f)
	next(f)
	for row in reader:
		data.append([float(i) for i in row[1:]])
clf = svm.OneClassSVM()
clf.fit(np.array(data))
joblib.dump(clf, filename + '.pkl')