# install pytube --> pip install pytube
from pytube import Playlist, YouTube

#url de playlist 
playlist = Playlist('url de playlist')
for video in playlist:
    print('Empezando descarga de:')
    print('*********************************************************')
    print(YouTube(video).title)
    #ruta de descarga --> C:/Users/CurrentUser/Desktop/YTDownload
    YouTube(video).streams.get_highest_resolution().download('ruta de descarga')
    print('*************** PROCESO TERMINADO ***********************')