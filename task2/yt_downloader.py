#Unicompiler TASK-2
#YOUTUBE VIDEO DOWNLOADER
#More than a billion people watch YouTube every month.
#Sometimes there are videos we like to download permanently.
#YouTube doesn’t give you that option, but you can create an app with a 
#simple UI and the ability to download YouTube videos in different formats 
#and video quality


#tkinter allows to build gui applications
from tkinter import *
from tkinter import filedialog

#moviepy used for video editing ,processing and composting
from moviepy import *
from moviepy.editor import VideoFileClip

#pytube is used for downloading video from web
from pytube import YouTube

import shutil #used for automating process of copying and removal of files and 
              #directories

#Functions
def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file_highest_resolution():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    #move file to selected directory using shutil module
    shutil.move(mp4_video, user_path)
    screen.title('Downloading is done!Try Downloading Another File...')
def download_file_720p():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.filter(res="720p").first().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    #move file to selected directory using shutil module
    shutil.move(mp4_video, user_path)
    screen.title('Downloading is done!Try Downloading Another File...')
def download_file_240p():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.filter(res="240p").first().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    #move file to selected directory using shutil module
    shutil.move(mp4_video, user_path)
    screen.title('Downloading is done!Try Downloading Another File...')
def download_file_360p():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.filter(res="360p").first().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    #move file to selected directory using shutil module
    shutil.move(mp4_video, user_path)
    screen.title('Downloading is done!Try Downloading Another File...')
def download_file_480p():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.filter(res="480p").first().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    #move file to selected directory using shutil module
    shutil.move(mp4_video, user_path)
    screen.title('Downloading is done!Try Downloading Another File...')
def download_file_144p():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.filter(res="144p").first().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    #move file to selected directory using shutil module
    shutil.move(mp4_video, user_path)
    screen.title('Downloading is done!Try Downloading Another File...')
screen = Tk()
title = screen.title('My Youtube Downloader')
#Canvas comes from tkinter
canvas = Canvas(screen, bg='yellow',width=500, height=1800)
canvas.pack()

#image logo
imgg = PhotoImage(file='yt.png')
#resize
imgg = imgg.subsample(2, 2)
canvas.create_image(250, 80, image=imgg)

#link field
link_field = Entry(screen, width=40, bg='white',font=('Arial', 15) )
link_label = Label(screen, text="Enter The Download Link: ", bg='yellow',font=('Arial', 15))

#Select Path for saving the file
path_label = Label(screen, text="Select Path For Downloading",bg='yellow', font=('Arial', 15))
select_btn =  Button(screen, text="Select Path", bg='red', padx='22', pady='3',font=('Arial', 15), fg='#fff', command=select_path)
#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Add widgets to window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#Download btns
dwnld_bttn_highest_resolution = Button(screen, text="Download File in highest resolution",bg='green', padx='22', pady='3',font=('Arial', 15), fg='#fff', command=download_file_highest_resolution)
dwnld_bttn_720p = Button(screen, text="Download File in 720p resolution",bg='green', padx='25', pady='6',font=('Arial', 15), fg='#fff', command=download_file_720p)
dwnld_bttn_480p = Button(screen, text="Download File in 480p resolution",bg='green', padx='25', pady='9',font=('Arial', 15), fg='#fff', command=download_file_480p)
dwnld_bttn_360p = Button(screen, text="Download File in 360p resolution",bg='green', padx='25', pady='12',font=('Arial', 15), fg='#fff', command=download_file_360p)
dwnld_bttn_240p = Button(screen, text="Download File in 240p resolution",bg='green', padx='25', pady='15',font=('Arial', 15), fg='#fff', command=download_file_240p)
dwnld_bttn_144p = Button(screen, text="Download File in 144p resolution",bg='green', padx='25', pady='18',font=('Arial', 15), fg='#fff', command=download_file_144p)


#add to canvas
canvas.create_window(250, 400, window=dwnld_bttn_highest_resolution)
canvas.create_window(250, 480, window=dwnld_bttn_720p)
canvas.create_window(250, 560, window=dwnld_bttn_480p)
canvas.create_window(250, 640, window=dwnld_bttn_360p)
canvas.create_window(250, 720, window=dwnld_bttn_240p)
canvas.create_window(250, 800, window=dwnld_bttn_144p)

screen.mainloop()#mainloop tells the window for the user to do something
