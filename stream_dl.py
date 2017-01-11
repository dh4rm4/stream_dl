#!/usr/bin/env python2.7.9
# -*- coding: utf-8 -*-

#from __future__ import unicode_literals
from Tkinter import *
from ttk import *
from PIL import ImageTk, Image
import youtube_dl

def get_infos():
    url = (url_input.get())

    dl_pl = pl_choice.get()
    if (dl_pl == "YES"):
        dl_pl = False
    else:
        dl_pl = True

    format_dl = format_choice.get()
    if (format_dl == "MP3"):
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': dl_pl,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                    }]}
        format_dl = 'bestvideo+bestaudio/best'
    else:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'noplaylist': dl_pl,}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        meta = ydl.extract_info(url, download=False)
    print 'duration    : %s' %(meta['duration'])
    print 'title       : %s' %(meta['title'])


# WINDOWS MANAGEMENT
win = Tk()
win.resizable(width=False, height=False)
win.geometry('{}x{}'.format(550, 420))

# BACKHROUND IMAGE
bk_img = ImageTk.PhotoImage(Image.open("bg.jpg"))
bk_label = Label(image=bk_img)
bk_label.place(x=-1, y=-1)#, relwidth=1, relheight=1)

# COPY URL OF THE VIDEO :
url_value = StringVar()
url_value.set("URL de votre video")
url_input = Entry(win, textvariable=url_value, width=60)
url_input.place(x=25, y=25, width=500, height=25)

# MANAGE THE FORMAT :
form_choice = ['Download Format :', 'MP4', 'MP3']
variable = StringVar(win)
variable.set('Download Format')
format_choice = Combobox(win, values = form_choice)
format_choice.current(0)
format_choice.place(x=75, y=65)

# MANAGE THE Playlist :
choice_pl = ['Download the playlist :', 'YES', 'NOPE']
pl_var = StringVar(win)
pl_var.set('Download playlist')
pl_choice = Combobox(win, values = choice_pl)
pl_choice.current(0)
pl_choice.place(x=75, y=95)

validation = Button(win, text="Validate", command=get_infos)
validation.place(x=75, y=125)

win.mainloop()
