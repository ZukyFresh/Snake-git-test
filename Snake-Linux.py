#!/usr/bin/python

import random
import tkinter
from tkinter import *
tk = Tk()
'''while True:
    event=wait_for_event()
    event.process()
    if main_window_has_been_destroyed(): 
        break'''
canvas=Canvas(tk,width=700,height=700,bg="lightskyblue")
canvas.pack()

def had():
    global x,x2,y,y2
    canvas.create_oval(x,y,x2,y2,fill="red",outline="red",tags="h1")
    canvas.create_rectangle(x+10,y,x2+10,y2,fill="red",outline="red",tags="h2")
    canvas.create_oval(x+35,y,x2+35,y2,fill="red",outline="red",tags="h3")
    canvas.create_oval(x+60,y,x2+60,y2,fill="red",outline="red",tags="h4")

def bod():
    gen=random.randint(70,630)
    gen2=random.randint(70,630)
    canvas.create_oval(gen,gen2,gen+20,gen2+20,fill="gold",outline="gold")

def okraj():
    canvas.create_rectangle(0,0,50,700,fill="black",outline="black")
    canvas.create_rectangle(0,0,700,50,fill="black",outline="black")
    canvas.create_rectangle(650,0,700,700,fill="black",outline="black")
    canvas.create_rectangle(0,650,700,700,fill="black",outline="black")

def pohybhada():
    global x,x2,y,y2,h,h2,j,k,kouskyhada
    canvas.delete("hj")
    x+=j
    x2+=j
    y+=k
    y2+=k
    canvas.create_oval(x+h2,y+h,x2+h2,y2+h,fill="red",outline="red",tags="hj")
    for i in range(0,kouskyhada):
        if p1==1:
            canvas.create_oval(x+h2,y+h,x2+h2,y2+h,fill="red",outline="red",tags="hj")
            canvas.create_oval(x+h2,y+h-25,x2+h2,y2+h-25,fill="red",outline="red",tags="hj")
        if p2==1:
            canvas.create_oval(x+h2,y+h,x2+h2,y2+h,fill="red",outline="red",tags="hj")
            canvas.create_oval(x+h2,y+h+25,x2+h2,y2+h+25,fill="red",outline="red",tags="hj")
        if p3==1:
            canvas.create_oval(x+h2,y+h,x2+h2,y2+h,fill="red",outline="red",tags="hj")
            canvas.create_oval(x+h2-25,y+h,x2+h2-25,y2+h,fill="red",outline="red",tags="hj")
        if p4==1:
            canvas.create_oval(x+h2,y+h,x2+h2,y2+h,fill="red",outline="red",tags="hj")
            canvas.create_oval(x+h2+25,y+h,x2+h2+25,y2+h,fill="red",outline="red",tags="hj")     
    canvas.after(100,pohybhada)
    
def dolu(sour):
    global h,j,k,ac,av,ax,ab,p1,p2,p3,p4
    if ac==1:
        j=0
        k=5
        h=h*h-20
        av=0
        ax=1
        ab=1
        p1=1
        p2=0
        p3=0
        p4=0
def nahoru(sour):
    global j,h,k,ac,av,ax,ab,p1,p2,p3,p4
    if av==1:
        j=0
        k=-5
        h=h*-1
        ac=0
        ab=1
        ax=1
        p1=0
        p2=1
        p3=0
        p4=0
def doleva(sour):
    global h2,k,j,ac,av,ax,ab,p1,p2,p3,p4
    if ax==1:
        k=0
        j=-5
        h2=h2*-1
        ac=1
        av=1
        ab=0
        p1=0
        p2=0
        p3=1
        p4=0
def doprava(sour):
    global h2,k,j,ac,av,ax,ab,p1,p2,p3,p4
    if ab==1:
        k=0
        j=5
        h2=h2*h2-20
        av=1
        ac=1
        ax=0
        p1=0
        p2=0
        p3=0
        p4=1
#===============================================================================
canvas.bind_all("w",nahoru)
canvas.bind_all("a",doleva)
canvas.bind_all("s",dolu)
canvas.bind_all("d",doprava)
k=0
ac=1
av=1
ab=1
ax=1
kouskyhada=1
j=0
x=70
p1=1
p2=1
p3=1
p4=1
y=60
x2=90
y2=80
h=5
h2=5
had()
bod()
okraj()
pohybhada()
mainloop()