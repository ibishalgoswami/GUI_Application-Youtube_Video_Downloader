import tkinter as tk
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk
from tkinter import messagebox
from pytube import YouTube
from PIL import ImageTk, Image
import requests
import urllib.parse
import io
import time
from tkinter import filedialog
import os
import threading


root = ThemedTk(theme="radiance")
root.title("Youtbe video downloader")
root.geometry('670x340')
root.maxsize(670, 340)
root.minsize(670, 340)
root.iconbitmap('youtube-downloader.ico')


text = tk.Label(root, text="Download Video and Audio from YouTube",
                font='Helvetica 15 bold')
text.pack()

status = tk.Label(root, text="Status bar", font='Helvetica 10',
                  relief='sunken', anchor="w")
status.pack(side="bottom", fill='x')

# Creating threads


def threadButtonOne():
    threading.Thread(target=download_yt_file).start()


def threadButtonTwo():
    threading.Thread(target=download_file).start()


def download_yt_file():
    global image, monthchoosen, get_url, yt
    get_url = inp_url.get()

    if get_url:
        yt = YouTube(get_url)
        image_url = yt.thumbnail_url
        raw_data = urllib.request.urlopen(image_url).read()
        im = Image.open(io.BytesIO(raw_data))
        image_resize = im.resize((210, 110), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image_resize)
        img_label = tk.Label(root, image=image)
        img_label.place(x=10, y=150)
        title_label = tk.Label(root, text=yt.title)
        title_label.place(x=10, y=260)
        # status['text']=yt.title
        lis = []
        stream = yt.streams.filter(progressive=True)
        for i in stream:
            lis.append(i.resolution)  # getting all the resolution.
        lis_tup = tuple(lis)

        monthchoosen = ttk.Combobox(root, width=27)
        # Adding combobox drop down list
        monthchoosen['values'] = (lis_tup)
        monthchoosen.set("Select preferred resolution")
        monthchoosen.place(x=420, y=160)
        btn_proceed = ttk.Button(root, text="Proceed", command=threadButtonTwo)
        btn_proceed.place(x=450, y=200)

    else:
        tk.messagebox.showerror("Error Message", "Oops ! URL not Found")


def download_file():
    res = monthchoosen.get()

    if res == '144p' or res == '144':
        save_file = filedialog.askdirectory()
        if save_file:
            status['text'] = "File downloading in progress......"
            stream = yt.streams.get_by_itag(160)
            stream.download(save_file)
            status['text'] = "File downloaded......"

    elif res == '240p' or res == '240':
        save_file = filedialog.askdirectory()
        if save_file:
            status['text'] = "File downloading in progress......"
            stream = yt.streams.get_by_itag(133)
            stream.download(save_file)
            status['text'] = "File downloaded......"

    elif res == '360p' or res == '360':
        save_file = filedialog.askdirectory()
        if save_file:
            status['text'] = "File downloading in progress......"
            stream = yt.streams.get_by_itag(18)
            stream.download(save_file)
            status['text'] = "File downloaded......"

    elif res == '480p' or res == '480':
        if save_file:
            save_file = filedialog.askdirectory()
            status['text'] = "File downloading in progress......"
            stream = yt.streams.get_by_itag(135)
            stream.download(save_file)
            status['text'] = "File downloaded......"

    elif res == '720p' or res == '720':
        if save_file:
            save_file = filedialog.askdirectory()
            status['text'] = "File downloading in progress......"
            stream = yt.streams.get_by_itag(22)
            stream.download(save_file)
            status['text'] = "File downloaded......"

    elif res == '1080p' or res == '1080':
        if save_file:
            save_file = filedialog.askdirectory()
            status['text'] = "File downloading in progress......"
            stream = yt.streams.get_by_itag(137)
            stream.download(save_file)
            status['text'] = "File downloaded......"

    else:
        tk.messagebox.showerror("Error", "Resolution not selected")


text_url = ttk.Label(root, text="URL:", font=('courier', 18, 'bold'))
text_url.place(x=110, y=50)

inp_url = tk.StringVar()
entry = ttk.Entry(root, textvariable=inp_url, width=31, font=('Helvetica', 14))
entry.focus_force()
entry.place(x=180, y=50)

download_btn = ttk.Button(root, text="Download", command=threadButtonOne)
download_btn.place(x=270, y=90)

root.mainloop()
