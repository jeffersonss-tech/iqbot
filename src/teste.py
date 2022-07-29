'''from os import path

from main import inicia

if path.exists('file') is False:
    with open('file', 'w') as file:
        file.write('48738203')
    inicia()
'''
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("pause.wav")
play(song)
