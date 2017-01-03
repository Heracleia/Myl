import csv
import numpy as np
from sklearn import svm
from sklearn.externals import joblib

filename = 'imu_reduced'
clf = joblib.load(filename + '.pkl')
result = [0, 0]
with open(filename + '.csv', 'rb') as f:
	reader = csv.reader(f)
	next(f)
	for row in reader:
		prediction = clf.predict(np.array(row[1:]).reshape(1, -1))[0]
		if prediction == -1:
			result[0] += 1
		else:
			result[1] += 1
print(result)
		