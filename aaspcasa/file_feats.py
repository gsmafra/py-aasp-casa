from glob import glob
from scipy.io.wavfile import read

def file_feats(extract_feats, args):

	data_x = []
	data_y = []

	audio_folder = '/scenes_stereo_8k/'
	class_id = 0

	for sub_folder in glob(audio_folder + '*'):

		for filename in glob(sub_folder + '/*.wav'):

			[fs, sig] = read(filename)
			feats = extract_feats(fs, sig, args)

			data_x.append(feats)
			data_y.append(class_id)
			
		class_id += 1
	
	return (data_x, data_y)
	
