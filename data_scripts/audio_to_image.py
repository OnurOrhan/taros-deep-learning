import librosa
import matplotlib.pyplot as plt
from librosa import display
import os
import json
root_dir = "./../data/morse_text_audio_files_train"

training_data = {}




for root, dirs, files in os.walk(root_dir):

    for name in files:
        try:
            new_file_path = os.path.join(root, name)
            samples, sampling_rate = librosa.load(new_file_path, sr=5500, mono=True, offset=0.0
                                              , duration=None)

            training_data[name.split('.')[0]] = samples.tolist()

        except:
            print(new_file_path)


with open('./../data/training_data.json', 'w') as fp:
    json.dump(training_data, fp)




# print(samples.shape)
# print(samples.size*samples.itemsize)
# print(len(samples))
#
# duration_of_sound = len(samples)/sampling_rate
# #
# print(duration_of_sound)
#
#
#
# plt.figure(figsize=(15, 5))
# librosa.display.waveplot(samples, sampling_rate, alpha=0.8)
# plt.show()
# #
#
# librosa.display.specshow(samples, sampling_rate)
#
# # import librosa
# # import numpy
# # import skimage
# #
# # def scale_minmax(X, min=0.0, max=1.0):
# #     X_std = (X - X.min()) / (X.max() - X.min())
# #     X_scaled = X_std * (max - min) + min
# #     return X_scaled
# #
# # def spectrogram_image(y, sr, out, hop_length, n_mels):
# #     # use log-melspectrogram
# #     mels = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels,
# #                                             n_fft=hop_length*2, hop_length=hop_length)
# #     mels = numpy.log(mels + 1e-9) # add small number to avoid log(0)
# #
# #     # min-max scale to fit inside 8-bit range
# #     img = scale_minmax(mels, 0, 255).astype(numpy.uint8)
# #     img = numpy.flip(img, axis=0) # put low frequencies at the bottom in image
# #     img = 255-img # invert. make black==more energy
# #
# #     # save as PNG
# #     skimage.io.imsave(out, img)
# #
# #
# # if __name__ == '__main__':
# #     # settings
# #     hop_length = 512 # number of samples per time-step in spectrogram
# #     n_mels = 128 # number of bins in spectrogram. Height of image
# #     time_steps = 384 # number of time-steps. Width of image
# #
# #     # load audio. Using example from librosa
# #     path = librosa.util.example_audio_file()
# #     y, sr = librosa.load(path, offset=1.0, duration=10.0, sr=22050)
# #     out = 'out.png'
# #
# #     # extract a fixed length window
# #     start_sample = 0 # starting at beginning
# #     length_samples = time_steps*hop_length
# #     window = y[start_sample:start_sample+length_samples]
# #
# #     # convert to PNG
# #     spectrogram_image(window, sr=sr, out=out, hop_length=hop_length, n_mels=n_mels)
# #     print('wrote file', out)
