import tkinter as tk

root = tk.Tk()

def line(event):
    canvas.create_line(0,0, event.x,event.y)

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

root.bind("<Button-1>", line)

root.mainloop()