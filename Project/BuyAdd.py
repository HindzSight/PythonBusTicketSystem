from tkinter import *

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\bus.png')
bus=Label(root,image=img)
bus.grid(row=0,column=0,columnspan=3,padx=w//3)
t1=Label(root,text='Online Bus Booking System',bg='light blue',fg='Red',font='Arial 32 bold')
t1.grid(row=1,column=0,columnspan=3,padx=w//3)

def nextseat():
    root.destroy()
    import bookwindow

def nextbooked():
    root.destroy()
    import checkbooking
    
def nextbus():
    root.destroy()
    import Newadd
    
seat=Button(root,text='Seat Booking',bg='light green',font='Arial 20 bold',command=nextseat)
booked=Button(root,text='Check Booked Seat',bg='green3',font='Arial 20 bold',command=nextbooked)
buses=Button(root,text='Add Bus Details',bg='dark green',font='Arial 20 bold',command=nextbus)
admin=Label(root,text='For Admin Only',fg='Red',font='TimesNewRoman 14 bold')
seat.grid(row=2,column=0,pady=60)
booked.grid(row=2,column=1,pady=60)
buses.grid(row=2,column=2,pady=60)
admin.grid(row=3,column=2)

root.title('Python Bus Service')
root.mainloop()

