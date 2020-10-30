from pydub import AudioSegment
from pydub.playback import play
from glob import glob



dot_time = 100
dash_time = 300

print("converting .wav files to dot and dashes!")

playlist_songs = [AudioSegment.from_wav(wav) for wav in glob("/Users/tanmay.ghai/usc/csci566/audios/*")]

audio_mediums = glob("/Users/tanmay.ghai/usc/csci566/audios/*")

print(audio_mediums)

idx = 0

for song in playlist_songs:
	dot = song[0:dot_time]
	dash = song[0:dash_time]

	play(dot)
	play(dash)

	name = audio_mediums[idx].split("/")[-1].split(".")[0]

	dot.export(name + "-dot.wav", format="wav")
	dash.export(name + "-dash.wav", format="wav")

	idx+=1