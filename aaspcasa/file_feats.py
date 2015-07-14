from glob import glob
from scipy.io.wavfile import read
from os.path import exists
from sys import exit

def file_feats(extract_feats, args):

	audio_folder = 'scenes_mono_8k/'

	if not exists(audio_folder):
		print('Please move to the folder containing the /scenes_mono_8k/ subfolder')
		exit()
	
	data_x = []
	data_y = []
	
	class_id = 0

	for sub_folder in glob(audio_folder + '*'):

		for filename in glob(sub_folder + '/*.wav'):

			[fs, sig] = read(filename)
			feats = extract_feats(fs, sig, args)

			data_x.append(feats)
			data_y.append(class_id)
			
		class_id += 1
	
	return (data_x, data_y)
	
