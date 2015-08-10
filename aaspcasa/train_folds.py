import sys

from numpy import concatenate
from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import classification_report, recall_score

from . import target_names

def sub_list(X, index):

	return [X[i] for i in list(index)]

def train_folds(fit_predict, X, Y, args, n_combs=1, random_fold=False, get_train_acc=False):

	# Splits the data into k folds, calls the trainer function (fit_predict)
	# and displays results

	Y_test_true_all = []
	Y_test_pred_all = []
	if get_train_acc:
		Y_train_true_all = []
		Y_train_pred_all = []

	for i in range(n_combs):

		print('Cross-validating combination n ' + str(i+1))
		sys.stdout.flush()

		if random_fold:
			state = None
		else:
			state = i

		skf = StratifiedKFold(Y, n_folds=5, random_state=state, shuffle=True)

		for train_index, test_index in skf:

			X_train = sub_list(X, train_index)
			X_test = sub_list(X, test_index)
			Y_train = sub_list(Y, train_index)
			Y_test = sub_list(Y, test_index)

			if get_train_acc:
				(Y_train_pred, Y_test_pred) = fit_predict(X_train, Y_train, X_test, args)
			else:
				Y_test_pred = fit_predict(X_train, Y_train, X_test, args)

			if get_train_acc:
				Y_train_true_all.append(Y_train)
				Y_train_pred_all.append(Y_train_pred)

			Y_test_true_all.append(Y_test)
			Y_test_pred_all.append(Y_test_pred)

	if get_train_acc:
		Y_train_true_all = concatenate(Y_train_true_all)
		Y_train_pred_all = concatenate(Y_train_pred_all)

	Y_test_true_all = concatenate(Y_test_true_all)
	Y_test_pred_all = concatenate(Y_test_pred_all)

	print('\n')
	print(classification_report(Y_test_true_all, Y_test_pred_all, target_names=target_names))

	if get_train_acc:
		return (1 - recall_score(Y_train_true_all, Y_train_pred_all, average='micro'),
				1 - recall_score(Y_test_true_all, Y_test_pred_all, average='micro'))
	else:
		return  1 - recall_score(Y_test_true_all, Y_test_pred_all, average='micro')
