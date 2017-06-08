# -*- coding: utf-8 -*-

import librosa
import numpy as np
import os.path
import time


def create_chromagram_sum(title):
    y, sr = librosa.load('songs/' + title)
    S = np.abs(librosa.stft(y)**2)
    chroma = librosa.feature.chroma_stft(S=S, sr=sr)

    return [sum(x) for x in chroma]


def display_top_three(chroma_sum, scale):
    chroma_sorted = [x for x in chroma_sum]
    chroma_sorted.sort()
    print("Top three keys are")
    for k in [11, 10, 9]:
        top_sum = chroma_sorted[k]
        print(scale[chroma_sum.index(top_sum)] + ": " + str(top_sum))


def analyze_songs():
    path = './songs'
    file_names = [f for f in os.listdir(path) if f != '.DS_Store' and f != '.gitkeep' and os.path.isfile(os.path.join(path, f))]

    for title in file_names:
        print ("Starting analysis of " + title + " at " + time.strftime('%I:%M:%S'))

        chroma_sum = create_chromagram_sum(title)
        scale = ["C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯", "A", "A♯", "B"]

        for j in range(12):
            print(scale[j] + ": " + str(chroma_sum[j]))

        display_top_three(chroma_sum, scale)

        print ("Finished analysis of " + title + " at " + time.strftime('%I:%M:%S'))


analyze_songs()
