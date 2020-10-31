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
time_per_unit = 1000 #in milli seconds
path_get = './morse_character_audio_files/'
path_store = './morse_text_audio_files/'


def get_json_files():
    with open('./morse_code.json', "r", encoding='utf-8') as file:
        morse_code = json.load(file)
    with open('./special_character.json', 'r', encoding='utf-8') as file:
        special_characters = json.load(file)
    return morse_code, special_characters


def get_text_data(morse_code, special_characters):
    texts = []
    with open('./text_data.txt', 'r', encoding='utf-8') as text_file:
        lines = text_file.readlines()
        keys = list(morse_code.keys())
        keys += list(special_characters.keys())
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
    for medium in audio_mediums:
        print("Generating audio file for medium: ",medium )
        path = path_get + medium + '/'
        for text in texts:
            print("text: ", text)
            text_audio = AudioSegment.silent(duration = 0)
            for character in text:
                if character == " ":
                    text_audio = seven_units_sleep
                else:
                    if special_characters.get(character):
                        character_audio = AudioSegment.from_wav(path + special_characters[character] + ".wav")
                    elif character =='/':
                        character_audio = AudioSegment.from_wav( path + "slash.wav")
                    elif character =='"':
                        character_audio = AudioSegment.from_wav( path + "quotation.wav")
                    else:
                        character_audio = AudioSegment.from_wav( path + character.upper() + ".wav")
                    text_audio += character_audio + three_units_sleep
            # save and play text audio file
            text_audio.export(path_store + medium + '/' + text + ".wav", format="wav")
            play(text_audio)


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