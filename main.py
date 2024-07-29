import pytube

url = input("Enter video url: ")
path = "Enter your file location "

#You can download high quality videos if you want.
pytube.YouTube(url).streams.get_highest_resolution().download(path)
#If you want, you can download the audio of the video.
pytube.YouTube(url).streams.get_audio_only().download(path)
#It will be enough to run one of 7 or 9 lines