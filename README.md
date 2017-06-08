# KeyRanged

KeyRanged is a Python script that computes chromagrams for a folder of songs. For each song, the top 3 musical keys are written to a csv file.

## Required packages
* [numpy][numpy]
* [librosa][librosa]

## How to Run
1. Drop songs into the `songs` folder
2. From root folder, run `python key_finder.py` in the terminal
3. Results are stored in `song_chromas.csv`

[numpy]: http://www.numpy.org/
[librosa]: https://github.com/librosa/librosa
