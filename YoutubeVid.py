from pytube import YouTube
from window import link_field

def ytdownload(): 
    link = link_field.get()
    myVid = YouTube(link).streams.get_highest_resolution()

    print("-------- Video Title --------")
    print(myVid.title)

    print("-------- Downloading Video --------")

    myVid.download()