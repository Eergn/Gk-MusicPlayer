import tkinter as tkr
from tkinter import filedialog
import pygame
import os

"""Setting Volume Function"""
def volset(idk):
    pygame.mixer.music.set_volume(volumelevel.get())
    print("Volume is set to --> "+idk)
"""Creating Player Window"""
player = tkr.Tk()
player.iconbitmap(r"./icons/window.ico")
"""Console Commands"""
os.chdir("./playlist")
songlist = os.listdir()
print(os.listdir())

"""Playlist"""
def plap(id):
    print("was selected")
    opop.set("0")
playlist = tkr.Listbox(player, highlightcolor = "blue",selectmode = tkr.SINGLE)
playlist.bind('<<ListboxSelect>>', plap)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos += 1

"""Volume Input"""
volumelabel = tkr.LabelFrame(player, text="Volume")
volumelevel = tkr.Scale(volumelabel,from_=0.0,to_=1.0, orient = tkr.HORIZONTAL,command=volset, resolution=0.001)

"""Customizing Player Window"""
player.title("Gk-Music Player Version-1.beta")
player.geometry("340x340")

"""Getting Song"""
file = playlist.get(tkr.ACTIVE)

"""Pygame Inits"""
pygame.init()
pygame.mixer.init()

"""Functions"""
def play():
    value = opop.get()
    if value == "0":
        pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(volumelevel.get())
        print("Playing --> "+playlist.get(tkr.ACTIVE))
        var.set(playlist.get(tkr.ACTIVE))
        pygame.mixer.music.set_volume(1)
    else:
        mum = fif.get()
        pygame.mixer.music.load(mum)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(volumelevel.get())
        l = mum.split("/")
        xop = len(l)
        plp = l[xop-1]
        print("Playing --> " + plp)
        var.set(plp)
        pygame.mixer.music.set_volume(1)
oror = tkr.StringVar()
oror.set("0")
def pause():
    if oror.get() == "0":
        oror.set("1")
        print("paused")
        pygame.mixer.music.set_volume(volumelevel.get())
        pygame.mixer.music.pause()
    elif oror.get() == "1":
        oror.set("0")
        print("resumed")
        pygame.mixer.music.unpause()
        pygame.mixer.music.set_volume(volumelevel.get())

def ExitPlayer():
    pygame.mixer.music.stop()
    print("Stopped")
def addtop():
    player.fileadd = filedialog.askopenfilename(initialdir="Music", title="Select file", filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
    if player.fileadd !="":
        s = player.fileadd.split("/")
        apapap = len(s)-1
        hdsu = s[apapap]
        lolipopok = os.getcwd()+"/"+hdsu
        os.rename(player.fileadd, lolipopok)
        os.chdir("../")
        print("")
        player.destroy()
        os.system("python ./tool.py")

def rmplay():
    print("hi")
    os.remove("./"+playlist.get(tkr.ACTIVE))
    os.chdir("../")
    print("")
    player.destroy()
    os.system("python ./tool.py")

"""external opening"""
opop = tkr.StringVar()
opop.set("0")
fif = tkr.StringVar()
def plot():
    player.filename = filedialog.askopenfilename(initialdir="Music", title="Select file",filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
    if player.filename != "":
        opop.set("1")
        fif.set(player.filename)
        print("hi")
        mum = fif.get()
        l = mum.split("/")
        xop = len(l)
        plp = l[xop - 1]
        print("Opend --> " + plp)
        var.set(plp)
"""Buttons"""

#play button
playbutton = tkr.Button(player, width=3, height=2, text="Play", command=play)

#pause Button
pausebutton = tkr.Button(player, width=3, height=2, text="Pause", command=pause)

#stop button
stopbutton = tkr.Button(player, width=3, height=2, text="Stop", command=ExitPlayer)

#open music from computer
omfc = tkr.Button(player, width=3, height=2, text="Open Music From Computer", command=plot)

#add music to playlist
addtoplay = tkr.Button(player, width=1, height=1, text="+", command= addtop)

#decrement music from playlist
rmfromplay = tkr.Button(player, width=1, height=1, text="-", command= rmplay)
"""Song Name"""
songlabel = tkr.LabelFrame(player, text="Song Name")
var = tkr.StringVar()
songContest = tkr.Label(songlabel, textvariable=var)



"""Packing"""
songlabel.pack(fill="both", expand="no")
songContest.pack()
volumelabel.pack(fill="x")
volumelevel.pack(fill="x")
playbutton.pack(fill="x")
pausebutton.pack(fill="x")
stopbutton.pack(fill="x")
omfc.pack(fill="x")
addtoplay.pack(fill="none",expand="no", side=tkr.LEFT, ipadx=0, ipady=0)
rmfromplay.pack(fill="none", side=tkr.LEFT)

playlist.pack(fill="both",expand="yes")
"""Running or Activating Window"""
player.mainloop()