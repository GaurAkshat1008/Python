import tkinter
from pytube import YouTube

root = tkinter.Tk()
root.geometry('750x500')
root.configure(bg='lightpink')
root.resizable(0,0)
root.title('YouTube video downloader')

tkinter.Label(root, text = 'Video Downloader', font = 'calibre 20 italic', bg='lightpink').pack()

link = tkinter.StringVar()
tkinter.Label(root, text ='Paste Link Here:', font ='arial 15 bold', bg='lightpink').place(x = 290, y = 50)
link_enter = tkinter.Entry(root, width = 60, textvariable = link, bd=3, bg='white', font=('calibre', 12, 'bold'), fg='red').place(x=100, y=100)

def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tkinter.Label(root, text ='Downloaded', font ='calibre 15').place(x= 300, y = 210)
def search():
    url = YouTube(str(link.get()))
    title = url.title
    tkinter.Label(root, text = title, font ='calibre 10').place(x= 100, y = 210)

tkinter.Button(root, text ='Search', font ='arial 18 bold', bg ='cyan', padx = 2, command = search, fg='crimson').place(x=220, y = 150)
tkinter.Button(root, text ='Download', font ='arial 18 bold', bg ='cyan', padx = 2, command = downloader, fg='crimson').place(x=380, y = 150)
root.mainloop()