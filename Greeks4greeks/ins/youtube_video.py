#Youtube Video Downloader

from pytube import Youtube
link = input("Enter the link")
print("Downloading...")
YouTube(link).streams.first().download()
print("Video downloaded successfully")