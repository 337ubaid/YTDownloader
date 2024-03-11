from pytube import YouTube
from sys import argv

link = argv[1] # Get the link from the 1st command line
yt = YouTube(link)

print(f"Title: {yt.title}")

yd = yt.streams.get_highest_resolution()
yd.download('D:/Downloads/Videos')

