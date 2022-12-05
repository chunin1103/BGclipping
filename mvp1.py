from rembg import remove
import pyscreenshot
import tkinter as tk 
from tkinter import *
from PIL import Image

root = tk.Tk()
# root.attributes("-fullscreen", True)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

# root.geometry("500x500")
# Tk.attributes("-fullscreen", True)
# Grab the initial screenshot 
ini_im = pyscreenshot.grab()

# To save the screenshot
ini_im.save("Testing.png")

# open the screenshot
bg = PhotoImage(file = "Testing.png")

input_path ='Testing.png'
im = Image.open(input_path)

label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)
label2 = Label( root, text = "Welcome",
               bg = "#88cffa")
  
# Specify a location of that image
# im=pyscreenshot.grab(bbox=(X1,Y1,X2,Y2))
# im = pyscreenshot.grab(bbox=(100, 50, 1000, 1000)) 

# im = remove(im)
# To view the screenshot
im.show()
root.mainloop()
