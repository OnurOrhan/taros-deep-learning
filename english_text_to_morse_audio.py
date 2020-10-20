"""
Please install the following:
1. pydub : library to manipulate audio data (Used for creating silent audio files and for concatenating audio file)
   pip install pydub

2. ffmpeg : provides command line based processing for audio and video files (dependency for pydub)
   sudo apt install ffmpeg

"""


# import pygame
import time
import sys
# import soundfile as sf
from pydub import AudioSegment
from pydub.playback import play


CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }

ONE_UNIT = 0.5
THREE_UNITS = 3 * ONE_UNIT
SEVEN_UNITS = 7 * ONE_UNIT
PATH = './morse_sound_files/'


def verify(string):
    keys = CODE.keys()
    for char in string:
        if char.upper() not in keys and char != ' ':
            sys.exit('Error the charcter ' + char + ' cannot be translated to Morse Code')


def main():
    print('Welcome to Alphabet to Morse Code Translator v.01\n')
    msg = input('Enter Message: ')
    verify(msg)
    # pygame.mixer.init()
    final_audio_output = AudioSegment.silent(duration = 0)
    for char in msg:
        if char == ' ':
            final_audio_output += AudioSegment.silent(duration=(1000*SEVEN_UNITS))
            time.sleep(SEVEN_UNITS)
        else:
            # CODE TO CONVERT .ogg FILES TO .wav
            # data, samplerate =  sf.read(PATH +'Morse-'+char.upper()+".ogg")
            # sf.write(PATH+'Morse-'+char.upper()+".wav", data, samplerate)

            # PLAY OGG FILES USING PYGAME
            # pygame.mixer.music.load(PATH +'Morse-'+char.upper()+".ogg")
            # pygame.mixer.music.play()

            # PLAY WAV FILES USING PYGAME
            # pygame.mixer.music.load(PATH + 'Morse-' + char.upper() + ".wav")
            # pygame.mixer.music.play()

            # READ WAV FILE TO AN AUDIO SEGMENT
            character_sound = AudioSegment.from_wav(PATH + 'Morse-' + char.upper() + ".wav")
            three_units_sleep = AudioSegment.silent(duration=(1000*THREE_UNITS))  # duration in milliseconds

            # ADD THE ABOVE TWO AUDIO SEGMENTS
            final_audio_output += character_sound + three_units_sleep
            time.sleep(THREE_UNITS)

    #SAVE THE AUDIO FILE
    final_audio_output.export(msg+".wav", format = "wav")
    play(final_audio_output)
    # play(AudioSegment.from_wav(msg+".wav"))


if __name__ == "__main__":
    main()