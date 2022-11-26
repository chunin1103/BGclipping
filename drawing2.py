import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

def line(event):
    global click_number
    global x1,y1
    if click_number == 0:
        x1 = event.x
        y1 = event.y
        click_number = 1

    else:
        x2 = event.x
        y2 = event.y
        canvas.create_line(x1,y1,x2,y2, fill = "black", width = 10)
        click_number = 0

click_number = 0

root.bind("<Button-1>", line)
root.bind()
        
root.mainloop()