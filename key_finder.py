import librosa
import numpy as np
import time

print (time.strftime('%I %M %S'))
y, sr = librosa.load('songs/faded.mp3')
S = np.abs(librosa.stft(y)**2)
chroma = librosa.feature.chroma_stft(S=S, sr=sr)

for i in range(len(chroma)):
    print(sum(chroma[i]))
print(time.strftime('%I %M %S'))
