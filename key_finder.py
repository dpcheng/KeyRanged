# -*- coding: utf-8 -*-

import librosa
import numpy as np
import os.path
import time

path = './songs'
file_names = [f for f in os.listdir(path) if f != '.DS_Store' and f != '.gitkeep' and os.path.isfile(os.path.join(path, f))]

for title in file_names:
    print ("Starting analysis of " + title + " at " + time.strftime('%I:%M:%S'))
    y, sr = librosa.load('songs/' + title)
    S = np.abs(librosa.stft(y)**2)
    chroma = librosa.feature.chroma_stft(S=S, sr=sr)
    scale = ["C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯", "A", "A♯", "B"]
    for j in range(12):
        print(scale[j] + ": " + str(sum(chroma[j])))
    print ("Finished analysis of " + title + " at " + time.strftime('%I:%M:%S'))
