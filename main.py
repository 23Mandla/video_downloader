import yt_dlp
from customtkinter import *

class Download(CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("Video downloader")
        self._set_appearance_mode("System") 
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.geometry("750x400")
        self.url = ""

        self.title = CTkLabel(self, text='Download videos', font = ("Helvetica", 15))
        self.title.grid(row = 0, column = 0, columnspan = 2, pady = 15)

        CTkLabel(self, text='URL').grid(row = 1, column = 0, pady = 25)

        self.entry = CTkEntry(self, width = 300)
        self.entry.grid(row = 1, column = 0, columnspan = 2, pady = 25)

        CTkButton(self, text="Download", width=200, command = self.download_video).grid(row=3, column=0, pady=15)
        CTkButton(self, text="Cancel", width=200, ).grid(row=3, column=1, pady=15)

        self.status = CTkLabel(self, text = "", font = ("Helvetica", 15))
        self.status.grid(row = 4, column = 0, columnspan = 2, pady = 20)

        self.progress_label = CTkLabel(self, text="", text_color="blue")
        self.progress_label.grid(row=5, column=0, columnspan=2, pady=10)

    def get_input(self):
        self.url = self.entry.get()


    def progress(self, dict):
        if dict['status'] == "downloading":
            percent = dict.get('_percent_str', '').strip()
            self.progress_label.configure(text=f"Progress : {percent}")
            self.update_idletasks()

          
    def download_video(self):
          
        self.get_input()

        self.status.configure(text="Fetching video info...", text_color="blue")
        self.update_idletasks()

        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "noplaylist": True, 
            "ignoreerrors": True,
            "merge_output_format": "mp4",
            "outtmpl" : "%(title)s.%(ext)s",
            "progress_hooks" : [self.progress]
        }
          
        with yt_dlp.YoutubeDL(ydl_opts) as yt:
            info = yt.extract_info(self.url, download = True)

            if info:
                self.status.configure(text=f"Downloading... {info.get('fulltitle')}", text_color="green")
                self.update_idletasks()

                self.status.configure(text= f"Downloaded {info.get('fulltitle')}", text_color="green")
                self.progress_label.configure(text = "Download complete!", text_color="green")
                self.update_idletasks()
   
if __name__ == "__main__":
    app = Download()
    app.mainloop()