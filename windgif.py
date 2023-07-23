from itertools import count, cycle
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import os

def shut_down():
    os.system("shutdown /s /t 0")
    root.destroy()

def restart():
    os.system("shutdown /r /t 1")
    root.destroy()

def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    root.destroy()

class ImageLabel(ctk.CTkLabel):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
        self.place_configure(x=2,y=2,anchor='nw')
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy().resize((996,521), Image.Resampling.LANCZOS)))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.configure(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.configure(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.configure(image=next(self.frames))
            self.after(self.delay, self.next_frame)

#demo :
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("800x420+450+200")
wid = 800
hgt = 420
root.title("Shut Down Windows")
root.iconbitmap(r"C:\Users\ASUS\Win pro\irman.ico")
root.resizable(False,False)
my_can=Canvas(root , width=wid , height=hgt, bg="black", highlightbackground="#cf6c34", highlightthickness=3 )
my_can.pack( fill="both", expand=True)
lbl = ImageLabel(my_can)
lbl.pack()
lbl.load(r"C:\Users\ASUS\Win pro\anima.gif")
shut = ctk.CTkButton(master=root, text="Shut Down", text_font=("Microsoft Sans Serif",15), width=100, height=20, corner_radius=10,
        #  text_color="#132122", fg_color="#cf6c34", hover_color="#ff8e4b", bg_color="#132122", border_width=0,
         text_color="#cf6c34", fg_color="#132122", hover_color="#293637", bg_color="#132122", border_width=2, border_color="#cf6c34",
         command = shut_down)
shut_win = my_can.create_window(830 , 180 , anchor="nw" , window=shut )#720

res = ctk.CTkButton(master=root, text="Restart", text_font=("Microsoft Sans Serif",15), width=100, height=20, corner_radius=10,
         text_color="#cf6c34", fg_color="#132122", hover_color="#293637", bg_color="#132122", border_width=2, border_color="#cf6c34",
         command=restart)
res_win = my_can.create_window(860 , 250 , anchor="nw" , window=res )#750

slp = ctk.CTkButton(master=root, text="Sleep", text_font=("Microsoft Sans Serif",15), width=100, height=20, corner_radius=10,
        #  text_color="#cf6c34", fg_color="#132122", hover_color="#293637", bg_color="#132122", border_width=0,
         text_color="#cf6c34", fg_color="#132122", hover_color="#293637", bg_color="#132122", border_width=2, border_color="#cf6c34",
         command=sleep)
slp_win = my_can.create_window(860 , 320 , anchor="nw" , window=slp )#765

root.mainloop()
