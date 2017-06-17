import librosa
import numpy as np
import os.path
import time
import csv


def create_spectrogram(title):
    y, sr = librosa.loa('songs/' + title)
    S = np.abs(librosa.stft(y))
    comps, acts = librosa.decompose.decompose(S, n_components=8)


def analyze_songs():
    path = './songs'
    file_names = [f for f in os.listdir(path) if f != '.DS_Store' and f != '.gitkeep' and os.path.isfile(os.path.join(path, f))]
    csvfile = open('song_frequencies.csv', 'wb')
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(["title", "frequencies"])

    for title in file_names:
        print("Starting analysis of " + title + " at " + time.strftime('%I:%M:%S'))

        spectrogram = create_spectrogram(title)
