'''file that implement YouTube video downloader'''
from sys import argv
from pytube import YouTube

LINK = argv[1]
YT = YouTube(LINK)

print("Title: ", YT.title)
print(f"View: {YT.views}")

YD = YT.streams.get_highest_resolution()
YD.download('./youtube videos')
