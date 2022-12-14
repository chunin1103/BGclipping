from rembg import remove
import pyscreenshot
import tkinter as tk 
from tkinter import *
from PIL import Image

# dig this one: https://www.youtube.com/watch?v=4ehHuDDH-uc

root = tk.Tk()
# root.attributes("-fullscreen", True)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
canvas = tk.Canvas(root, width=400, height=400)
root.geometry("%dx%d+0+0" % (w, h))

# root.geometry("500x500")
# Tk.attributes("-fullscreen", True)
# Grab the initial screenshot 
ini_im = pyscreenshot.grab()
ini_im.thumbnail((1200,1200), Image.ANTIALIAS)

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
canvas = tk.Canvas(root, width = 400, height =400)
canvas.pack(pady=20, fill=None)
# Specify a location of that image
# im=pyscreenshot.grab(bbox=(X1,Y1,X2,Y2))
# im = pyscreenshot.grab(bbox=(100, 50, 1000, 1000)) 

# im = remove(im)
# To view the screenshot
im.show()

click_number = 0

capturex = []
capturey = []
def line(event):
    global click_number, x1, y1, x2, y2, capturex, capturey
    color = 'black'
    if click_number == 0:
        x1 = x2 = event.x
        y1 = y2 = event.y 
        capturex.append(x1)
        capturex.append(x2)
        capturey.append(y1)
        capturey.append(y2)
        
        canvas.create_line(x1,y1,x2,y2, fill = color, width = 50)
        click_number += 1
    
    else:
        x2 = event.x
        y2 = event.y 
        capturex.append(x1)
        capturex.append(x2)
        capturey.append(y1)
        capturey.append(y2)        
        canvas.create_line(x1,y1,x2,y2, fill = "black", width = 10)
        x1 = x2
        y1 = y2

root.bind("<Button-1>", line)
        
root.mainloop()

print(capturex)
print(capturey)

bboxx = max(capturex)
bboxy = max(capturey)
bboxx2 = min(capturex)
bboxy2 = min(capturey)

print(bboxx)
print(bboxy)
