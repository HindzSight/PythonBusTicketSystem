from tkinter import *

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
#root.geometry('{}x{}'.format(w,h))
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\bus.png')
bus=Label(root,image=img)
bus.grid(row=0,column=0,columnspan=3,padx=w//3)
t1=Label(root,text='Online Bus Booking System',bg='light blue',fg='Red',font='Arial 32 bold')
t1.grid(row=1,column=0,padx=w//3)
name=Label(root,text='Name: Manan Jain',fg='Blue2',font='Arial 16 bold',pady=70)
er=Label(root,text='Er: 211B173',fg='Blue2',font='Arial 16 bold')
mob=Label(root,text='Mobile: 8871113041',fg='Blue2',font='Arial 16 bold',pady=70)
sub=Label(root,text='Submitted to : Dr. Mahesh Kumar',bg='light blue',fg='Red',font='Arial 24 bold')
prj=Label(root,text='Project Based Learning',fg='Red',font='Arial 14')
name.grid(row=2,column=0,padx=w//3)
er.grid(row=3,column=0,padx=w//3)
mob.grid(row=4,column=0,padx=w//3)
sub.grid(row=5,column=0,padx=w//3)
prj.grid(row=6,column=0,padx=w//3)
def fun(e=0):
    root.destroy()
    import BuyAdd

root.bind('<KeyPress>',fun)

root.title('Python Bus Service')
root.mainloop()
