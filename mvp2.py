from rembg import remove
import pyscreenshot
import tkinter as tk 
from tkinter import *
from PIL import Image, ImageTk

# Create a fullscreen canvas
root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
canvas = tk.Canvas(root, width = w, height =h)
canvas.pack(fill='both', expand = 1, pady=20) 

# Grab the initial fullscreen screenshot
ini_im = pyscreenshot.grab()
ini_im.thumbnail((1200,1200), Image.ANTIALIAS)

# Save the screenshot
ini_im.save("Testing.png")

# open the screenshot
input_path ='Testing.png'
im = Image.open(input_path)
image = ImageTk.PhotoImage(im)

# create image as background of screenshot and anchor it to 0,0 cordination (important!)
canvas.create_image(0,0, image = image, anchor ='nw')

# Show it so that after, we can draw on it
im.show()


# open the canvas and start drawing

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
        print(x2)
        print(y2) 
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
print(bboxy2)
print(bboxx2)

# Specify a location of that image
im=pyscreenshot.grab(bbox=(bboxx2,bboxy2,bboxx,bboxy))
im.show()
# im = pyscreenshot.grab(bbox=(100, 50, 1000, 1000)) 

# im = remove(im)
# To view the screenshot