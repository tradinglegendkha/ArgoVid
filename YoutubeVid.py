from pytube import YouTube

link = input("Print the video url: ")
url = link
myVid = YouTube(url)

print("-------- Video Title --------")
print(myVid.title)

print("-------- Downloading Video --------")

myVid = myVid.streams.get_highest_resolution()
myVid.download()