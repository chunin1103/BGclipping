import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

click_number = 0


def line(event):
    global click_number, x1, y1
    if click_number == 0:
        x1 = x2 = event.x
        y1 = y2 = event.y 
        canvas.create_line(x1,y1,x2,y2, fill = "black", width = 10)
        click_number += 1
    
    else:
        x2 = event.x
        y2 = event.y 
        canvas.create_line(x1,y1,x2,y2, fill = "black", width = 10)
        x1 = x2
        y1 = y2 


    

root.bind("<Button-1>", line)
        
root.mainloop()