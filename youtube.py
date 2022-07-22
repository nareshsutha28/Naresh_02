from io import BytesIO
from pytube.cli import on_progress
from tkinter import *
from tkinter import ttk
from pytube import YouTube
import requests
import os
import base64,os,threading

# from tkinter.ttk import *
root = Tk()
root.geometry('500x300')
root.resizable(1,1)
root.title("DataFlair-youtube video downloader")

link = StringVar()
Label(root, text = 'Youtube Video Downloader', font ='arial 20 bold').pack()# root, 

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').pack()#place(x= 160 , y = 60)root, 
link_enter = Entry(root, width = 70,textvariable = link).pack()#place(x = 32, y = 90)root, 
l=[]

my_progress=ttk.Progressbar(root,orient=HORIZONTAL,length=400,mode="determinate")
    
label1=Label(text="")

options = StringVar()
def on_progress(stream, chunk, bytes_remaining):
        global inc,my_progress,label2
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        inc=int(percentage_of_completion)
        print(inc)
        my_progress["value"]+=inc-my_progress["value"]
        label1.config(text=f"{inc}%")
        
        # label2.config(text=f"{inc}%")
        if my_progress["value"]==100:
            my_progress.grid_forget()
            # label2.grid_forget()
            # label2["text"]="0%"
def Downloader():

        global my_progress
        my_progress.config(mode="determinate")
        my_progress.pack(pady=20)
        my_progress.stop()
        url = YouTube(str(link.get()))   
        label1.pack()
        os.chdir("C:/Yotube Downloader By Coder Community/Video")
        url.register_on_progress_callback(on_progress) 
        video = url.streams.filter(res=str(options.get())).first()
        video.download()
      
       
        l1=Label(root, text = 'DOWNLOADED', font = 'arial 15').pack()  
def Click():

    for stream in (YouTube(str(link.get())).streams.filter(progressive=True)):
        l.append(str(stream.resolution))
    om1 = OptionMenu(root, options, *l)
    om1.pack()
    Button(root, text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red',  command = Downloader).pack()

Button(root, text = 'Search', font = 'arial 15 bold' ,bg = 'pale violet red',  command = Click).pack()




root.mainloop()

# Label(root,  text='Resolution:', font = 'arial 15' )  
# l3.pack() 
    # l1.after(2000, l1.destroy)

