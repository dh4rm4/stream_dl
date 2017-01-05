#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from ttk import *
import os
from PIL import ImageTk, Image

# WINDOWS MANAGEMENT
win = Tk()
win.resizable(width=False, height=False)
win.geometry('{}x{}'.format(550, 420))


def get_infos():
    url = (url_input.get())

    format_dl = format_choice.get()
    if (format_dl == "MP3"):
        format_dl = "--extract-audio --audio-format mp3 "
    elif (format_dl == "MP4"):
        format_dl = "-f mp4 "
    elif (format_dl == "Best audio"):
        format_dl = "--extract-audio --audio-format best "
    else:
        format_dl = "-f bestvideo+bestaudio/best "

    dl_pl = pl_choice.get()
    if (dl_pl == "YES"):
        dl_pl = "--yes-playlist "
    else:
        dl_pl = "--no-playlist "

    cmd = ('youtube-dl ' + dl_pl + format_dl + url)
    os.system(cmd)

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
form_choice = ['Download Format :', 'MP4', 'MP3', "Best audio", "Best video"]
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
