#Internship Task-3
#MP3 MUSIC PLAYER
#The MP3 Player is a device for playing MP3s and other
#digital audio files. This MP3 Player GUI project idea
#attempts to emulate the physical MP3 Player.
#You can build software that allows you play an MP3 files
#on your desktop or laptop computer.
#When you are done building the MP3 Player project, users
#can play their MP3 files and other digital audio files
#without having to purchase a physical MP3 Player.
#They’ll be able to play the MP3 files using their computers

import pygame
from pygame import mixer
from PIL import  Image
import tkinter
from tkinter import *
import tkinter.font as tkFont
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()    

root=Tk()
root.title('My Music player project')
root.geometry("960x960")
root.configure(bg="#ADD8E6")

mixer.init()
songstatus=StringVar()
songstatus.set("Choosing")

#playlist---------------
#heading=tkinter.StringVar();
#heading.set("Select the song you want to listen!")
#music=PhotoImage(file=r"C:\Users\DELL\Downloads\musicc.PNG")
#play_lab=Label(image=music)
#playbtn=Button(root,image=music,command=music)
playlist=Listbox(root,selectmode=SINGLE,font = "Roboto 20 bold",bg="#FFC0CB",fg="white",width=120,height=10)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\DELL\Music\music')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)
heading=tkinter.StringVar();
heading.set("Select the song you want to listen!")
music=PhotoImage(file=r"C:\Users\DELL\Downloads\musicc.PNG")
play_lab=Label(image=music)
musicbtn=Button(root,image=music,command=music)
musicbtn.config(padx=27,pady=3)
musicbtn.grid(row=0,column=1)
click_play=PhotoImage(file=r"C:\Users\DELL\Downloads\playy.PNG")
play_label=Label(image=click_play)
playbtn=Button(root,image=click_play,command=playsong)
playbtn.config(padx=7,pady=7)
playbtn.grid(row=1,column=0)


click_pause=PhotoImage(file=r"C:\Users\DELL\Downloads\pausee.PNG")
play_label=Label(image=click_pause)
pausebtn=Button(root,image=click_pause,command=pausesong)
pausebtn.config(padx=7,pady=7)
pausebtn.grid(row=1,column=1)


click_stop=PhotoImage(file=r"C:\Users\DELL\Downloads\stopp.PNG")
play_label=Label(image=click_stop)
stopbtn=Button(root,image=click_stop,command=stopsong)
stopbtn.config(padx=7,pady=7)
stopbtn.grid(row=2,column=0)


click_resume=PhotoImage(file=r"C:\Users\DELL\Downloads\resume1.PNG")
play_label=Label(image=click_resume)
Resumebtn=Button(root,image=click_resume,command=resumesong)
Resumebtn.config(padx=7,pady=7)
Resumebtn.grid(row=2,column=1)

mainloop()
