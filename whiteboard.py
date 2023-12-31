import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import *

#Functions for the code.....

def start_drawing(event):
    global is_drawing,prev_x,prev_y
    is_drawing=True
    prev_x,prev_y=event.x,event.y

def draw(event):
    global is_drawing,current_x,current_y,prev_x,prev_y
    if is_drawing:
        current_x,current_y=event.x,event.y
        canvas.create_line(prev_x,prev_y,current_x,current_y, fill=drawing_color,width=line_width,capstyle=tk.ROUND, smooth=True, )
        prev_x,prev_y=current_x,current_y

def stop_drawing(event):
    global is_drawing
    is_drawing=False
    
def change_pencolor():
    global drawing_color
    color=askcolor()[1]
    if color:
        drawing_color=color
                    
def change_linewidth(value):
    global line_width
    line_width=int(value)
    
#GUI making starts......

root=tk.Tk()
root.title("WhiteBoard App")


canvas=tk.Canvas(root,bg="white")
canvas.pack(fill="both",expand=True)


is_drawing=False
drawing_color="black"
line_width=2
prev_x=0
prev_y=0



root.geometry("800x600")

#now Control frame for app....

controls_frame=tk.Frame(root)
controls_frame.pack(side="top",fill="x")

color_button=tk.Button(controls_frame,text="Change Color",command=change_pencolor)
clear_button=tk.Button(controls_frame,text="Clear Board",command= lambda :canvas.delete("all"))

color_button.pack(side="left",padx=5,pady=5)
clear_button.pack(side="left",padx=5,pady=5)

line_width_selector_label=tk.Label(controls_frame,text="Line Width")
line_width_selector_label.pack(side="left",padx=5,pady=5)

line_width_selector=tk.Scale(controls_frame,from_=1,to=10, orient="horizontal",command=lambda val:change_linewidth(val))
line_width_selector.set(line_width)
line_width_selector.pack(side="left",padx=5,pady=5)

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>",draw)
canvas.bind("<ButtonRelease-1>",stop_drawing)

root.mainloop()
