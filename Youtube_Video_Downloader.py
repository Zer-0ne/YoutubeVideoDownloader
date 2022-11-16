from tkinter import *
import pytube
from pytube import *
# from pytube import streams
from pytube import YouTube

root = Tk()
root.geometry('600x300')
root.title("SahilKhan - Youtube Video Downloader")
root.configure(bg='black')
root.resizable(False,False)
Label(root,text='Youtube Video downloader',font='arial 22 bold', bg='red',fg='black',width='20').pack(side='top',ipady=3,fill='x')

link = StringVar()
Label(root,text="Paste Link here",bg='black',fg='red',font='arial 18').pack(anchor='center',ipady=10)
link = Entry(root,textvariable=link,bg='black',highlightcolor='red',fg='red', font='arial 15',highlightbackground='black',width='50',insertbackground='red')
link.pack(anchor='center')
def Downloader():
    url = YouTube((str(link.get())))
    video = url.streams.first()
    video.download()
    Label(root,text='Downloaded!!',bg='red',fg='black',width='20').pack(side='center',ipady=3,fill='x')
Label(root,text="  ",bg='black',fg='red',font='arial 18').pack(anchor='center',ipady=5)
Button(root,text = "Download",fg="red",bg='black',width = 5,command = Downloader,highlightcolor='green', font='arial 15 bold',highlightbackground='black').pack(ipadx=130,anchor='center')
Label(root,text='Sahil Khan',font='arial 22 bold', bg='red',fg='black',width='20').pack(side='bottom',ipady=3,fill='x')
root.mainloop()