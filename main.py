from tkinter import *
from pytube import YouTube

# Create Display window
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Raven YouTube video Downloader")

Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

# Create field to enter link
link = StringVar()

Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


# Download function
def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red',
       padx=2, command=downloader).place(x=180, y=150)

# Executes when we run the main program
root.mainloop()
