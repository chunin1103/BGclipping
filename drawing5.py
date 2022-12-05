import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(pady=20, fill="both")

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