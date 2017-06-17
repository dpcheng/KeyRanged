# -*- coding: utf-8 -*-

import librosa
import numpy as np
import os.path
import time
import csv


def create_chromagram_sum(title):
    y, sr = librosa.load('songs/' + title)
    S = np.abs(librosa.stft(y))
    chroma = librosa.feature.chroma_stft(S=S, sr=sr)

    return [sum(x) for x in chroma]


def get_scale_at_sum(scale, chroma_sums, value):
    sum_index = chroma_sums.index(value)
    return scale[sum_index]


def sort_chroma_sums(chroma_sums, scale):
    chroma_sorted = [x for x in chroma_sums]
    chroma_sorted.sort(reverse=True)
    return chroma_sorted


def analyze_songs():
    path = './songs'
    file_names = [f for f in os.listdir(path) if f != '.DS_Store' and f != '.gitkeep' and os.path.isfile(os.path.join(path, f))]
    csvfile = open('song_chromas.csv', 'wb')
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(["title", "first_key", "second_key", "third_key", "chroma_sums"])

    for title in file_names:
        print ("Starting analysis of " + title + " at " + time.strftime('%I:%M:%S'))

        chroma_sums = create_chromagram_sum(title)
        scale = ["C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯", "A", "A♯", "B"]

        for j in range(12):
            print(scale[j] + ": " + str(chroma_sums[j]))

        chroma_sorted = sort_chroma_sums(chroma_sums, scale)

        top_keys = [get_scale_at_sum(scale, chroma_sums, chroma_sorted[x]) for x in range(3)]
        print("Top three keys are: " + top_keys[0] + ", " + top_keys[1] + ", " + top_keys[2])

        writer.writerow([title, top_keys[0], top_keys[1], top_keys[2], chroma_sums])

        print ("Finished analysis of " + title + " at " + time.strftime('%I:%M:%S'))


analyze_songs()
