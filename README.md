# py-aasp-casa
Simple framework to work with the IEEE AASP CASA Challenge dataset in Python

## Installation
Download the scripts and run the setup:

	python setup.py

This will download the database from the official website of the challenge, reorganize with different folders for each class and downsample everything to mono / 8kHz

## Usage
With this all you need to do is to define two functions:

The first that will extract a descriptor for each file of the dataset

The second that will fit a classifier on a train set and return predicted results on a test set

Everything else (iterating over the files in the dataset and 5-fold cross-validation according to the specifications so you can compare with published results) is handled by the auxiliary functions

See example.py for more details

[Detection and Classification of Acoustic Scenes and Events]: http://c4dm.eecs.qmul.ac.uk/sceneseventschallenge/

[Public Dataset for Scene Classification Task]: http://c4dm.eecs.qmul.ac.uk/rdr/handle/123456789/29
