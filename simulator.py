from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import tkinter.font as tkFont
import pygame
import winsound
import time

root = Tk()
pygame.mixer.init()
root.configure(bg="#000")
root.title("Car Seatbelt Simulator")
root.iconbitmap("img/car.ico")
root.rowconfigure(7,minsize="30")
root.columnconfigure([0,1,2,3,4,5,6],minsize="30")

Title = Label(root,text="",bg="#000")
Title.grid(row=0,column=3)

image = Image.open("img/speedo.gif")
image = image.resize((300, 200), Image.ANTIALIAS)
speedo = ImageTk.PhotoImage(image,format="gif -index 2")
show_img = Label(image=speedo)
show_img.grid(row=1,column=3,padx=10,pady=10)

acc        = Image.open("img/drive.png")
acclr      = acc.resize((200, 100), Image.ANTIALIAS)
accl       = ImageTk.PhotoImage(acclr)

dec        = Image.open("img/brake.png")
declr      = dec.resize((200, 100), Image.ANTIALIAS)
decl       = ImageTk.PhotoImage(declr)


applyBelt  = Image.open("img/apply.png")
apply      = applyBelt.resize((200, 100), Image.ANTIALIAS)
applyBel   = ImageTk.PhotoImage(apply)

removeBelt = Image.open("img/remove.png")
remove     = removeBelt.resize((200, 100), Image.ANTIALIAS)
removeBel  = ImageTk.PhotoImage(remove)


park_img   = Image.open("img/park.png")
park_      = park_img.resize((200, 100), Image.ANTIALIAS)
park_car   = ImageTk.PhotoImage(park_)

exit_img   = Image.open("img/exit.png")
exit_      = exit_img.resize((200, 100), Image.ANTIALIAS)
exeunt     = ImageTk.PhotoImage(exit_)

key_img    = Image.open("img/key.png")
key        = key_img.resize((200, 100), Image.ANTIALIAS)
key_str    = ImageTk.PhotoImage(key)

fontStyle = tkFont.Font(family="Lucida Grande", size=20)

#Function for ignition
def start():
    pygame.mixer.music.load("audio/dodge challenger hellcat.mp3")
    pygame.mixer.music.play(loops=10)

Start = Button(root,image=key_str,command=start)
Start.grid(row=7,column=3,padx=10,pady=10)

global seconds
seconds = 0

#Function for acceleration
def count():
    global seconds
    seconds += 1
    Timer.config(text=seconds)
    if seconds >= 10:
        notify()

Timer = Label(root,width=20,font=fontStyle,bg="#000",fg="#fff")
Timer.grid(row=3,column=3)

#Function for deceleration
def brake():
   global seconds
   seconds -= 1
   Timer.config(text=seconds)
   if seconds <= 9:
       pygame.mixer.music.pause()
       brakes = Label(root,text="working in progress",width=20,font=fontStyle,bg="#000",fg="#000")
       brakes.grid(row=5,column=3,padx=10,pady=10)
decel = Button(root,image=decl,command=brake)
decel.grid(row=1,column=6,padx=10,pady=10)

accel = Button(root,image=accl,command=count)
accel.grid(row=1,column=0,padx=10,pady=10)

#Function for belt application
def apply_belt():
    global bel_alert
    pygame.mixer.music.pause()
    bel_alert = Label(root,text="Belt Applied",width=20,font=fontStyle,bg="#000",fg="green")
    bel_alert.grid(row=5,column=3,padx=10,pady=10)
apply = Button(root,image=applyBel,command=apply_belt)
apply.grid(row=5,column=0,padx=10,pady=10)

#Function for belt removal
def remove_belt():
    global seconds
    pygame.mixer.music.unpause()
    pygame.mixer.music.play(loops=15)
    bel_alert = Label(root,text="Apply your seatbelt",font=fontStyle,bg="#000",fg="red")
    bel_alert.grid(row=5,column=3,padx=10,pady=10)
    if seconds < 10:
        pygame.mixer.music.pause()
        progress = Label(root,text="XXXXX XXXX XXXXXXXX",font=fontStyle,bg="#000",fg="#000")
        progress.grid(row=5,column=3,padx=10,pady=10)
remove = Button(root,image=removeBel,command=remove_belt)
remove.grid(row=5,column=6,padx=10,pady=10)


#Function for sound
def notify():
    alert = Label(root,text="Apply your seatbelt",font=fontStyle,bg="#000",fg="red")
    alert.grid(row=5,column=3,padx=10,pady=10)
    pygame.mixer.music.load("audio/church.mp3")
    pygame.mixer.music.play(loops=15)

#Function for park
def park():
    global seconds
    seconds = 0
    Timer.config(text=seconds)
    pygame.mixer.music.pause()
    car_park = Label(root,text="Car Parked",width=20,font=fontStyle,bg="#000",fg="green")
    car_park.grid(row=5,column=3,padx=10,pady=10)
park = Button(root,image=park_car,command=park)
park.grid(row=7,column=0,padx=10,pady=10,sticky="news")

xit = Button(root,image=exeunt,command=root.destroy)
xit.grid(row=7,column=6,padx=10,pady=10)

root.mainloop()