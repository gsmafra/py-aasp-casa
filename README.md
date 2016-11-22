# py-aasp-casa
Simple library to work with the IEEE AASP CASA Challenge 2013 dataset in Python

## Dependencies

This package requires:

* [Numpy](http://www.numpy.org/)

* [Scipy](http://www.scipy.org/)

* [Scikit-learn](http://scikit-learn.org/)

* [Librosa](https://github.com/bmcfee/librosa)

## Installation
Download and run the setup:

	python setup.py install
	python setup_post_install.py

This will download the database from the official website of the challenge, reorganize with different folders for each class and downsample everything to mono / 8kHz

## Usage
With this all you need to do is to define two functions:

The first that will extract a descriptor for each file of the dataset

The second that will fit a classifier on a train set and return predicted results on a test set

Everything else (iterating over the files in the dataset and 5-fold cross-validation according to the specifications so you can compare with published results) is handled by the auxiliary functions

See example.py for more details

## Links and references

Giannoulis, Dimitrios, et al.
**"Detection and classification of acoustic scenes and events: An ieee aasp challenge."**
Applications of Signal Processing to Audio and Acoustics (WASPAA), 2013 IEEE Workshop on. IEEE, 2013.

Giannoulis, Dimitrios, et al.
**"A database and challenge for acoustic scene classification and event detection."**
Signal Processing Conference (EUSIPCO), 2013 Proceedings of the 21st European. IEEE, 2013.

[Detection and Classification of Acoustic Scenes and Events][]

[Public Dataset for Scene Classification Task][]

[Detection and Classification of Acoustic Scenes and Events]: http://c4dm.eecs.qmul.ac.uk/sceneseventschallenge/

[Public Dataset for Scene Classification Task]: http://c4dm.eecs.qmul.ac.uk/rdr/handle/123456789/29

