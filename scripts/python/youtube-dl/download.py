import pytube

url = input("Enter the URL of the video: ")
yt = pytube.YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download()