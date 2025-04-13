import random
import subprocess
from yt_dlp import YoutubeDL
import os
import sys

def open_random_video(playlist_url):
    # Options for yt_dlp to extract playlist info
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,  # Extract metadata without downloading
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            # Extract playlist information
            print("Getting playlist information...")
            playlist_info = ydl.extract_info(playlist_url, download=False)

            # Get the video URLs from the playlist entries
            print("Getting videos...")
            video_urls = [entry['url'] for entry in playlist_info['entries']]

            if not video_urls:
                print("No videos found in the playlist.")
                return

            # Pick a random video URL
            print("Finding video...")
            random_video = random.choice(video_urls)

            # Open the video using the web browser
            print("Opening video: ",random_video)
            subprocess.run(["xdg-open" if os.name == "posix" else "start", random_video], shell=True)

    except Exception as e:
        print("An error occurred: ", e)

if __name__ == "__main__":
    playlist_url = sys.argv[1]
    if len(sys.argv) < 2:
        # Replace with your playlist URL
        # playlist_url = "https://www.youtube.com/playlist?list=PLb-MR2Hfk3tlmemTNdCG_K4QiTehgJAr9"
        print("Add the playlist link as the first argument or uncomment the previous line in this script and replace the url with your own")
        sys.exit(1)

    print(f"Fetching video...")
    open_random_video(playlist_url)