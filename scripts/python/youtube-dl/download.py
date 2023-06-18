import argparse
import pytube

# Create argument parser
parser = argparse.ArgumentParser(description='Download a YouTube video.')
parser.add_argument('url', help='URL of the video')
args = parser.parse_args()

# Download the video
yt = pytube.YouTube(args.url)
stream = yt.streams.get_highest_resolution()
stream.download()
