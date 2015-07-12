import numpy as np
from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import classification_report

def sub_list(X, index):

	return [X[i] for i in list(index)]

def train_folds(fit_predict, X, Y, args, n_combs):

	# Splits the data into k folds, calls the trainer function (fit_predict)
	# and displays results

	Y_test_true = []
	Y_test_pred = []

	for i in range(n_combs):

		skf = StratifiedKFold(Y, n_folds=5, random_state=i, shuffle=True)

		for train_index, test_index in skf:

			X_train = sub_list(X, train_index)
			X_test = sub_list(X, test_index)
			Y_train = sub_list(Y, train_index)
			Y_test = sub_list(Y, test_index)

			Y_pred = fit_predict(X_train, Y_train, X_test, args)

			Y_test_true.append(Y_test)
			Y_test_pred.append(Y_pred)

	Y_test_true = np.concatenate(Y_test_true)
	Y_test_pred = np.concatenate(Y_test_pred)

	print(classification_report(Y_test_true, Y_test_pred))

