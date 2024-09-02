# music_genre_classifier

The dataset used: https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification
This model is only trained on .wav files as opposed to the more popular .mp3 files. I need to ethically source .mp3 files to retrain the model and classify the songs myself.

## audio_splice.py
Used to cut audio files into 30 second chunks to have a consistent length between songs.
However the current model is only trained on .wav files because I need to discover a way to train this
model on .mp3 files ethically.

## getToken and get_audio
These files are to aquire and access token to use spotify's api. In order to use these yourself you must go to spotify's api, go to the dashboard, and create your own app. Inside the application that you created you will be provided with a client_id and client_secret. You also need to add this link to the redirect uri section: http://localhost:8080. Then create a .env file and set

CLIENT_ID = '{your client id}'

CLIENT_SECRET = '{your client secret}'

REDIRECT_URI = '{http://localhost:8080}'

## music_genre_classifier.ipynb
Used to visualize, preprocess, train, test, analyze the model

## test_classifier.ipynb
Used to test the model by importing your model and inputing in a 30second audio file that is spliced using *audio_splice.py*
