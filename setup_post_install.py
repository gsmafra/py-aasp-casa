import urllib2
import zipfile
import re
import sys
from glob import glob
from os import chdir, mkdir, rename, getcwd
from os.path import exists

from resample_all import resample_all

def run_post_install():

	# Double check modules

	modules = set(['numpy', 'scipy', 'librosa', 'sklearn'])
	for module in modules:
		try:
			__import__(module)
		except ImportError:
			print('module \'' + str(module) + '\' is not installed')
			sys.exit()

	# Download dataset

	url = 'http://c4dm.eecs.qmul.ac.uk/rdr/bitstream/handle/123456789/29/scenes_stereo.zip'

	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print 'Downloading: %s Bytes: %s' % (file_name, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
		buffer = u.read(block_sz)
		if not buffer:
			break

		file_size_dl += len(buffer)
		f.write(buffer)
		status = r'%10d  [%3.2f%%]' % (file_size_dl, file_size_dl * 100. / file_size)
		status = status + chr(8)*(len(status)+1)
		print status,

	f.close()

	# Extract zip

	print('\nExtracting zip file')
	with zipfile.ZipFile('scenes_stereo.zip', "r") as z:
		z.extractall('./')

	# Reorganize folders
	
	print('Moving files to class folders')
	audio_folder = 'scenes_stereo/'
	home_folder = getcwd()
	chdir(audio_folder)

	for filename in glob('*'):

		y = re.split('0|1', filename)[0]
		if not exists(y):
			mkdir(y)
		rename(filename, y + '/' + filename)


	# Resample

	print('Resampling all files to 8kHz')
	chdir(home_folder)
	resample_all()

	print('Setup finished with no errors')
