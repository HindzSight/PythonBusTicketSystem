from tkinter import *
from tkinter.messagebox import *

root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()

root.geometry('%dx%d+0+0'%(w,h))
root.state('zoomed')

radio_v=StringVar()
radio_v.set('THIS IS A JOKE')
b1=Radiobutton(root,text='JOKER',variable=radio_v,value=1)
b1.grid(row=0,column=0,padx=w//3,columnspan=10)
b2=Entry(root)
b3=Label(root,text='Enter Name:',font='Arial 16 bold')
b3.grid(row=1,column=0)
b2.grid(row=1,column=1)
