import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

click_number = 0

n = 0
x = 20
y = 20
def line(event):
    global click_number
    global n, x, y
    canvas.create_line(0,0,x,y, fill = "black", width = 10)
    x = x + 20
    y = y + 20
    print('yes')
    print(n)
    n += 1

    
print(click_number)
click_number += 1
root.bind("<Button-1>", line)
        
root.mainloop()