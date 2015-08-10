from glob import glob
from os.path import exists
from sys import exit

from scipy.io.wavfile import read

def file_feats(extract_feats, audio_dir, args):

	if not exists(audio_dir):
		raise Exception('Audio directory not found')

	data_x = []
	data_y = []
	
	class_id = 0

	for sub_dir in sorted(glob(audio_dir + '*')):

		for filename in sorted(glob(sub_dir + '/*.wav')):

			[fs, sig] = read(filename)
			feats = extract_feats(fs, sig, args)

			data_x.append(feats)
			data_y.append(class_id)
			
		class_id += 1
	
	return (data_x, data_y)
	
