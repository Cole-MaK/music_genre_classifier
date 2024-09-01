# music_genre_classifier

The dataset used: https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification
This model is only trained on .wav files as opposed to the more popular .mp3 files. I need to ethically source .mp3 files to retrain the model and classify the songs myself.

##audio_splice.py
Used to cut audio files into 30 second chunks to have a consistent length between songs.
However the current model is only trained on .wav files because I need to discover a way to train this
model on .mp3 files ethically.
