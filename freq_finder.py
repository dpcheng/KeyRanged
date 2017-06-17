import librosa
import numpy as np
import os.path
import time
import csv


def create_spectrogram(title):
    y, sr = librosa.loa('songs/' + title)
    S = np.abs(librosa.stft(y))
    comps, acts = librosa.decompose.decompose(S, n_components=8)

    
