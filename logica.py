import os
import yt_dlp

directorio = "/home/bsap-vga/Downloads"

def download_mp3(link):
    yt_dlps = {
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192"
                }],
            "outtmpl": os.path.join(directorio, "%(title)s.%(ext)s"),
            }

    with yt_dlp.YoutubeDL(yt_dlps) as ytl:
        ytl.download([link])

def download_mp4(link):
    yt_dlps = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": os.path.join(directorio, "%(title)s.%(ext)s")
            }

    with yt_dlp.YoutubeDL(yt_dlps) as ytl:
        ytl.download([link])
