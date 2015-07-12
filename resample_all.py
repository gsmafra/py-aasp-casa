from librosa import resample, to_mono
from scipy.io.wavfile import read, write
from glob import glob
from os import chdir, mkdir

def resample_all():

	audio_folder = 'scenes_stereo/'
	subsamp_folder = 'scenes_stereo_8k/'

	chdir(audio_folder)
	mkdir(subsamp_folder)

	for sub_folder in glob('*'):

		mkdir(subsamp_folder + sub_folder)

		for filename in glob(sub_folder + '/*.wav'):

			print(filename)

			[fs, sig] = read(filename)

			sig = to_mono(sig.T)
			sig = resample(sig, fs, 8000)
		
			write(subsamp_folder + filename, 8000, sig)
		
