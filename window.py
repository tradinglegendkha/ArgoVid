from tkinter import *
from tkinter import filedialog
from YoutubeVid import ytdownload

#functions
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text="@ "+path)

window = Tk()
title = window.title("ArgoVid")
canvas = Canvas(window, width=600, height=600)
canvas.pack()


logo = PhotoImage(file='icon.png')
logo = logo.subsample(2, 2)
canvas.create_image(300, 90, image=logo)

#link
link_field = Entry(window, width=50)
link_label = Label(window, text="Enter the link: ")
canvas.create_window(300, 170, window=link_label)
canvas.create_window(300, 220, window=link_field)

#download path
path_label = Label = Label(window, text="Select path for the Download")
select_button = Button(window, text="Select", command=select_path, bg='gray')
canvas.create_window(300, 530, window=path_label)
canvas.create_window(300, 570, window=select_button)

download_button = Button(window, text="Download", command=ytdownload) 

canvas.create_window(300, 350, window=download_button)

window.mainloop()