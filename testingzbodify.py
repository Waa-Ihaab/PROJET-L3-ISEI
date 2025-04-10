from youtubesearchpython import VideosSearch
import yt_dlp
import os


# Folder
download_folder = r'C:\'

#Geting the song
def get_youtube_link(song_name):
    search = VideosSearch(song_name, limit=1)
    result = search.result()
    
    if result['result']:
        video = result['result'][0]
        return video['title'], video['link']
    else:
        return None, None


#Downloading it
def download_audio(link, download_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])



#OPS
song = input("Nom de la chanson : ")
title, link = get_youtube_link(song)

if link:
    print(f"Téléchargement de : {link}")
    download_audio(link, download_folder)
    print(" Téléchargement terminé !")
else:
    print(" Aucune vidéo trouvée.")