from pydub import AudioSegment 
import os
  
location = './genres_original/electronic'
# for file in os.listdir(location):
#     print(file)
# Open an mp3 file 
for i, file in enumerate(os.listdir(location)):
    file = f'./genres_original/electronic/{file}'
    print(file)
    if file == f'./genres_original/electronic/.DS_Store':
        pass
    else:
        song = AudioSegment.from_file(file, 
                                    format="mp3") 
        
        # pydub does things in milliseconds 
        fifteen_seconds = 15 * 1000
        fourfive_seconds = 45 * 999.5
        
        # song clip of 10 seconds from starting 
        thirty_seconds = song[fifteen_seconds:fourfive_seconds] 
        
        # save file 
        thirty_seconds.export(f"./genres_original/electronic/electronic{i}.mp3", 
                                format="mp3") 
        # print("New Audio file is created and saved") 