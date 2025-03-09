import yt_dlp
import json
from tkinter import *

class Download(Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Video downloader")
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.geometry("750x400")
        self.url = ""

        self.title = Label(self, text='Download videos', font = ("Helvetica", 15))
        self.title.grid(row = 0, column = 0, columnspan = 2, pady = 15)

        Label(self, text='URL').grid(row = 1, column = 0, pady = 25)

        self.entry = Entry(self, width = 40)
        self.entry.grid(row = 1, column = 0, columnspan = 2, pady = 25)

        Button(self, text="Download", width=40, command=self.download_video).grid(row=3, column=0, pady=15)
        Button(self, text="Cancel", width=40, ).grid(row=3, column=1, pady=15)

        self.status = Label(self, text = "Waiting to download")
        self.status.grid(row = 4, column = 0, columnspan = 2, pady = 20)


    def get_input(self):
        self.url = self.entry.get()

    def get_info(self):

        self.get_input()
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "noplaylist": True,
            "ignoreerrors": True,
            "merge_output_format": "mp4",
            "outtmpl" : "%(title)s.%(ext)s"
        }

        with yt_dlp.YoutubeDL(ydl_opts) as youtubeDownloader:
            info = youtubeDownloader.extract_info(self.url, download = False)

            if info:
                print(f"Platform detected: {info['extractor']}")
                sanitize = youtubeDownloader.sanitize_info(info)
                fullTitle = json.dumps(sanitize.get("fulltitle"), indent = 4)
                print(f"video title : {fullTitle}")

         
    def download_video(self):
          
        self.get_input()

        self.status.config(text="Fetching video info...", fg="blue")
        self.update()

        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "noplaylist": True, 
            "ignoreerrors": True,
            "merge_output_format": "mp4",
            "outtmpl" : "%(title)s.%(ext)s"
        }
          
        with yt_dlp.YoutubeDL(ydl_opts) as yt:
            info = yt.extract_info(self.url, download = True)

            if info:
                title = info.get("fulltitle")
                print(f"Downloading from: {info['extractor']}")
                self.status.config(text=f"Downloading... {title}", fg="green")
                self.update()

                yt.download([self.url]) 
               
if __name__ == "__main__":
    app = Download()
    app.mainloop()