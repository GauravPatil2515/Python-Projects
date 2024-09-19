import tkinter
from tkinter import *
import base64

root = Tk()

def action(canvas):
    canvas.bind("<Button-1>", xaxis)
    canvas.bind("<ButtonRelease-1>", yaxis)
    canvas.bind("<ButtonRelease-1>", box)

def xaxis(event):
    global x1, y1
    x1, y1 = (event.x - 1), (event.y - 1)
    print (x1, y1)

def yaxis(event):
    global x2, y2
    x2, y2 = (event.x + 1), (event.y + 1)
    print (x2, y2)

def box(event):
    photo = PhotoImage(file="picture.gif")
    yaxis(event)
    canvas.create_rectangle(x1,y1,x2,y2)
    for x in range(x1, x2):
        for y in range(y1, y2):
            r,g,b = getRGB(photo, x, y)
            newImage(r, g, b, x, y)

def getRGB(photo, x, y):
    value = photo.get(x, y)
    return tuple(map(int, value.split(" ")))

def newImage(r, g, b, x, y):
    picture = PhotoImage(width=x, height=y)
    picture.put("#%02x%02x%02x" % (r,g,b), (x,y))
    picture.write('new_image.gif', format='gif')

canvas = Canvas(width=500, height=250)
canvas.pack(expand=YES, fill=BOTH)
photo = PhotoImage(file="picture.gif")
canvas.create_image(0, 0, image=photo, anchor=NW)
canvas.config(cursor='cross')
action(canvas)

root.mainloop()

