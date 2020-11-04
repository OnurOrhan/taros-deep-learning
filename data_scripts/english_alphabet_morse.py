import json
import os
from pydub import AudioSegment
from pydub.playback import play

one_unit = 0.5
time_per_unit = 100
sleep_time_symbols = time_per_unit * one_unit #sleep time between symbols(dots and dashes) in a character

path_store = "./data/morse_character_audio_files/"  #path to store generated audio files
path_get = "./data/dots_and_dashes/" #path to get dot and dash audio files

def main():
    with open('./morse_code.json', "r", encoding='utf-8') as file:
        morse_code = json.load(file)
    #read audio files
    audio_mediums = []
    for _,_,files in os.walk("./data/processed audios"):
        audio_mediums = [file.split('.')[0] for file in files]
    #audio mediums
    print(audio_mediums)
    #generate alphabet audio files
    one_unit_sleep = AudioSegment.silent(duration=sleep_time_symbols)
    for medium in audio_mediums:
        print("Generating audio file for medium:", medium)
        dot =  AudioSegment.from_wav(path_get + medium + "-dot.wav")
        dash = AudioSegment.from_wav(path_get + medium + '-dash.wav')
        for character, code in morse_code.items():
            print("character: ", character)
            character_audio = AudioSegment.silent(duration=0)
            for c in code:
                if c == '.':
                    character_audio += dot + one_unit_sleep
                elif c == '-':
                    character_audio += dash + one_unit_sleep
            #save character audio file
            character_audio.export(path_store + medium + "/" + character + ".wav", format="wav")
            #play(character_audio)


if __name__ == "__main__":
    main()