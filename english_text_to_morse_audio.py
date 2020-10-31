"""
Please install the following:
1. pydub : library to manipulate audio data (Used for creating silent audio files and for concatenating audio file)
   pip install pydub

2. ffmpeg : provides command line based processing for audio and video files (dependency for pydub)
   sudo apt install ffmpeg

"""

import os
import sys
import json
from pydub import AudioSegment
from pydub.playback import play
# import soundfile as sf
# import pygame

one_unit = 0.5
three_units = 3 * one_unit
seven_units = 7 * one_unit
time_per_unit = 100 #in milli seconds
path_get = './morse_character_audio_files/'
path_store = './morse_text_audio_files/'
label_dict = {}

def get_json_files():
    with open('./morse_code.json', "r", encoding='utf-8') as file:
        morse_code = json.load(file)
    with open('./special_character.json', 'r', encoding='utf-8') as file:
        special_characters = json.load(file)
    return morse_code, special_characters


def get_text_data(morse_code, special_characters):
    texts = []
    keys = list(morse_code.keys())
    keys += list(special_characters.keys())
    with open('./text_data.txt', 'r', encoding='utf-8') as text_file:
        lines = text_file.readlines()
        for line in lines:
            line = line.strip('\n')
            verify(line, keys)
            texts.append(line)
    return texts


def get_audio_mediums():
    audio_mediums = []
    for _, _, files in os.walk("./processed audios"):
        audio_mediums = [file.split('.')[0] for file in files]
    audio_mediums += ['beeps']
    return audio_mediums


def preload_audio(audio_mediums):
    audio_files = {}
    for medium in audio_mediums:
        medium_path = path_get + medium + '/'
        audio_files[medium] = {}

        for root,dirs,files in os.walk(medium_path):

            for name in files:
                file_path = os.path.join(root, name)

                audio_files[medium][name.split('.')[0]] = AudioSegment.from_wav(file_path)

    return audio_files


def verify(string, keys):
    keys += ['/','"']
    for char in string:
        if char.upper() not in keys and char != ' ':
            print(char)
            sys.exit('Error the charcter ' + char + ' cannot be translated to Morse Code')


def main():
    morse_code, special_characters = get_json_files()
    #get text data
    texts = get_text_data(morse_code, special_characters)
    print(texts)

    # audio mediums
    audio_mediums = get_audio_mediums()
    print(audio_mediums)
    three_units_sleep = AudioSegment.silent(duration=(time_per_unit * three_units))  # duration in milliseconds
    seven_units_sleep = AudioSegment.silent(duration=(time_per_unit * seven_units))


    #preloading the audio
    audio_files = preload_audio(audio_mediums)
    print(audio_files)

    for medium in audio_mediums:
        print("Generating audio file for medium: ",medium )
        path = path_get + medium + '/'
        for i,text in enumerate(texts):
            file_name = str(i)+'_'+medium
            label_dict[file_name] = {}
            print("text: ", text)
            text_audio = AudioSegment.silent(duration = 0)
            for character in text:
                if character.isalpha():
                    character=character.upper()
                if character == " ":
                    text_audio += seven_units_sleep
                else:
                    if special_characters.get(character):
                        character_audio = audio_files[medium][special_characters[character]]
                    elif character == '/':
                        character_audio = audio_files[medium]['slash']
                    elif character == '"':
                        character_audio = audio_files[medium]['quotation']
                    else:
                        character_audio = audio_files[medium][character]

                    text_audio += character_audio + three_units_sleep
            # save and play text audio file
            text_audio.export(path_store + medium + '/' + file_name+ ".wav", format="wav")

            label_dict[file_name] = text
            #play(text_audio)

    with open('./labels.json', 'w') as fp:
        json.dump(label_dict, fp)


if __name__ == "__main__":
    main()



 # CODE TO CONVERT .ogg FILES TO .wav
# if special_characters.get(character):
#     character = special_characters[character]
#     data, samplerate = sf.read(PATH + 'beeps_ogg/Morse_Code_-_' + character + ".ogg")
#     sf.write(PATH + 'beeps/' + character + ".wav", data, samplerate)
# elif character == '/':
#     data, samplerate = sf.read(PATH + 'beeps_ogg/Morse_Code_-_slash' + ".ogg")
#     sf.write(PATH + "beeps/slash.wav", data, samplerate)
# elif character == '"':
#     data, samplerate = sf.read(PATH + 'beeps_ogg/Morse_Code_-_quotation' + ".ogg")
#     sf.write(PATH + "beeps/quotation.wav", data, samplerate)
# else:
#     data, samplerate =  sf.read(PATH + 'beeps_ogg/Morse-'+ character+".ogg")
#     sf.write(PATH + 'beeps/' + character+ ".wav", data, samplerate)

# PLAY OGG FILES USING PYGAME
# pygame.mixer.music.load(PATH +'Morse-'+char.upper()+".ogg")
# pygame.mixer.music.play()

# PLAY WAV FILES USING PYGAME
# pygame.mixer.music.load(PATH + 'Morse-' + char.upper() + ".wav")
# pygame.mixer.music.play()