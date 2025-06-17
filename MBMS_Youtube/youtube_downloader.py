from pytubefix import YouTube
import customtkinter as ct
from tkinter import ttk
import requests
import datetime
from numerize import numerize 
from PIL import Image


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("MBMS Youtube Downloader")
        self.resizable(False, False)

        # info Label
        self.info_label = ct.CTkLabel(self, text="Enter Your URL Here", anchor="center", width=550, font=("Consolas", 18), fg_color="transparent")
        self.info_label.place(relx=0.05)
        
        # URL Search Bar
        self.URL = ct.StringVar()
        self.url_entry = ct.CTkEntry(self, width=480, height=40, textvariable=self.URL)
        self.url_entry.place(relx=0.05, rely=0.08)
        self.url_search = ct.CTkButton(self, text="Search", width=30, height=40, command=self.url_finder)
        self.url_search.place(relx=0.86, rely=0.08)
        
        # Video Thumbnail Image
        self.thumbnailImg = ct.CTkImage(dark_image=Image.open("assets/noimage.jpeg"), size=(300, 200))
        self.thumbnail = ct.CTkLabel(self, image=self.thumbnailImg, text="", fg_color="#ccc")
        self.thumbnail.place(relx=0.05, rely=0.18)
        
        # Video Title
        self.titleLbl = ct.CTkLabel(self, text="Title", anchor="center", width=540, height=50, font=("Consolas", 18))
        self.titleLbl.place(relx=0.05, rely=0.6)
        
        # Video Channel
        self.channelLbl = ct.CTkLabel(self, text="Channel",fg_color="#ddd", anchor="center", width=240, height=50, font=("Consolas", 18))
        self.channelLbl.place(relx=0.56, rely=0.18)
        
        # Video Date
        self.dateLbl = ct.CTkLabel(self, text="Date",fg_color="#ccc", anchor="center", width=240, height=50, font=("Consolas", 18))
        self.dateLbl.place(relx=0.56, rely=0.28)
        
        # Video Duration
        self.durationLbl = ct.CTkLabel(self, text="Duration",fg_color="#ddd", anchor="center", width=240, height=50, font=("Consolas", 18))
        self.durationLbl.place(relx=0.56, rely=0.38)
        
        # Video Views
        self.viewsLbl = ct.CTkLabel(self, text="Views",fg_color="#ccc", anchor="center", width=240, height=50, font=("Consolas", 18))
        self.viewsLbl.place(relx=0.56, rely=0.48)
        
        # Streams
        self._streams = dict()
        self.streamsMenu = ct.CTkOptionMenu(self, values=[""], width=550, height=40)
        self.streamsMenu.place(relx=0.05, rely=0.7)
        
        # Download Section
        self.download_btn = ct.CTkButton(self, text="Download ▼",width=550, height=40, font=("Consolas", 18), command=self.download_)
        self.download_btn.place(relx=0.05, rely=0.8)
        self.progress_bar = ct.CTkProgressBar(self, width=550, height=20)
        self.progress_bar.set(0)
        self.progress_bar.place(relx=0.05, rely=0.92)
        
    def download_(self):
        if self.streamsMenu.get() == "":
            self.info_label.configure(text="No stream is selected", text_color="green")
        else:
            self.info_label.configure(text="Download started")
            self._streams[self.streamsMenu.get()].download("./downloads")
            self.info_label.configure(text="Video downloaded successfully")
    

    def progress_callback(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size
        self.progress_bar.set(percentage_of_completion)
        self.update_idletasks()

    def url_finder(self):
        url = self.URL.get()
        try:
            yt = YouTube(url, on_progress_callback=self.progress_callback)
            self.info_label.configure(text="Video Found", text_color="green")
            response = requests.get(yt.thumbnail_url)
            if response.status_code == 200:
                with open(f"thumb/{yt.title}_thumbnail.jpg", "wb") as file:
                    file.write(response.content)
                temp = ct.CTkImage(dark_image=Image.open(f"thumb/{yt.title}_thumbnail.jpg"), size=(300, 200))
                self.thumbnail.configure(image=temp)
            else:
                print(f"Request failed with status code: {response.status_code}")
            

            self.titleLbl.configure(text=yt.title)
            self.channelLbl.configure(text=yt.author)
            self.dateLbl.configure(text=f"{yt.publish_date.year}/{yt.publish_date.month}/{yt.publish_date.day}")
            self.durationLbl.configure(text=f"{datetime.timedelta(seconds=yt.length)}")
            self.viewsLbl.configure(text=f"{numerize.numerize(yt.views)}")
            ys = yt.streams.filter(only_video=True)
            for st in ys:
                if st.type == "video":
                    self._streams[f"Quality: {st.resolution} FPS: {st.fps} Type: {st.type}"] = st
                else:
                    self._streams[f"Bitrate: {st.abr}  Type: {st.type}"] = st
                
            self.streamsMenu.configure(values=self._streams.keys())
            
        except:
            self.info_label.configure(text="Error: Invalid URL", text_color="red")
            
        
app = App()
app.mainloop()

