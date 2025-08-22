# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


# # A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
import yt_dlp
# import logging

app = Flask(__name__)

@app.route('/')
def hello_world():
    # yt_opts = {
    #     'verbose': True
    # }

    ## ydl = yt_dlp.YoutubeDL(yt_opts)
    ## return ydl.download(["https://vkvideo.ru/video-222409194_456239177"])
    # logging.warning("get_video_info")
    target_url = request.args.get('target_url')
    return get_video_info(target_url)
    # print("get_video_info")
    # return get_video_info("https://www.youtube.com/watch?v=Jf2vDlgDAoc")

def get_video_info(url):
    ydl_opts = {
        'quiet': True,  # Suppress console output from yt-dlp
        'extract_flat': True, # For playlists, extract only basic info without processing individual entries
    }

    ydl = yt_dlp.YoutubeDL(ydl_opts)
    info_dict = ydl.extract_info(url, download=False)

    # Access specific information from the info_dict
    if info_dict:
        print(f"Title: {info_dict.get('title')}")
        print(f"Uploader: {info_dict.get('uploader')}")
        print(f"Duration: {info_dict.get('duration')} seconds")
        print(f"View Count: {info_dict.get('view_count')}")
        print(f"Webpage URL: {info_dict.get('url')}")
        print(f"Headers: {info_dict.get('http_headers')}")

        # If it's a playlist, access entries
        if 'entries' in info_dict:
            print("\nPlaylist Entries:")
            for entry in info_dict['entries']:
                print(f"- {entry.get('title')} ({entry.get('webpage_url')})")
    else:
        print("Could not retrieve information.")

    return info_dict
