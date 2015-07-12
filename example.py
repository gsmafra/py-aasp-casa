import numpy as np
from librosa import stft
from sklearn.svm import SVC
from file_feats import file_feats
from train_folds import train_folds

def extract_m_lspectre(fs, sig, args):

	# Extract a descriptor for one file of the database. This function will run
	# only one time for each file in a simulation. You don't want to extract
	# features directly from audio every time you evaluate a new fold, do you?

	# Unpack all the arguments for the classifier
	(n_fft, hop_length, win_length) = args

	# Perform feature extraction
	sig_stft = stft(sig, n_fft=n_fft, hop_length=hop_length, win_length=win_length)
	spectre = np.abs(sig_stft)**2
	mean_spectre = np.mean(spectre, axis=1)
	
	# The return value can be whatever you want, you will treat the data later 
	# on in the classifier function
	return mean_spectre

def svm_train_test(X_train, Y_train, X_test, args):

	# General-purpose classifier function: takes a train set and its labels for
	# training and a test set to return predictions. This function will run 5
	# times for each 

	# Unpack all the arguments for the classifier
	(svm_c, ) = args

	# Here X_train and X_test are a list of descriptors for each file according
	# to the output of the extractor function (each element of the list can be
	# a vector, a matrix or even another list) so you have to format the data
	# to use your classifier
	X_train = np.asarray(X_train)
	Y_train = np.asarray(Y_train)
	X_test = np.asarray(X_test)

	# Declare the classifier, fit for the training data, test and return
	# predictions
	classifier = SVC(kernel='linear', C=svm_c)
	classifier.fit(X_train, Y_train)
	Y_pred = classifier.predict(X_test)

	return Y_pred

def test(n_fft=1700, hop_length=1000, win_length=1700, svm_c=0.01):

	fe_args = (n_fft, hop_length, win_length)
	cl_args = (svm_c,)
	
	(X, Y) = file_feats(extract_m_lspectre, fe_args)
	
	train_folds(svm_train_test, X, Y, cl_args, n_combs=10)

if __name__ == '__main__':

	test()
	
