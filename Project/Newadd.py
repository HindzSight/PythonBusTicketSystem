from tkinter import *

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\bus.png')
bus=Label(root,image=img)
bus.grid(row=0,column=0,columnspan=5,padx=w//3)
t1=Label(root,text='Online Bus Booking System',bg='light blue',fg='Red',font='Arial 32 bold')
t1.grid(row=1,column=0,columnspan=5,padx=w//3)
t2=Label(root,text='Add New Details to DataBase',bg='seashell2',fg='green3',font='Arial 22 bold')
t2.grid(row=2,column=0,columnspan=5,padx=w//3,pady=20)

def nextop():
    root.destroy()
    import operator
    
def nextbus():
    root.destroy()
    import newbus
    
def nextroute():
    root.destroy()
    import busroute

def nextrun():
    root.destroy()
    import busrunning


op=Button(root,text='New Operator',bg='light green',font='Arial 16',command=nextop)
busnew=Button(root,text='New Bus',bg='orange red',font='Arial 16',command=nextbus)
route=Button(root,text='New Route',bg='steel blue1',font='Arial 16',command=nextroute)
newrun=Button(root,text='New Run',bg='light coral',font='Arial 16',command=nextrun)

op.grid(row=3,column=0,pady=20)
busnew.grid(row=3,column=1,pady=20)
route.grid(row=3,column=2,pady=20)
newrun.grid(row=3,column=3,pady=20)
root.title('Python Bus Service')
root.mainloop()
