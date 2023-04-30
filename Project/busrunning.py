from tkinter import *
from tkinter.messagebox import *

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\bus.png')
img1=PhotoImage(file='.\\home.png')
bus=Label(root,image=img)
bus.grid(row=0,column=0,columnspan=20,padx=w//3)
t1=Label(root,text='Online Bus Booking System',bg='light blue',fg='Red',font='Arial 32 bold')
t1.grid(row=1,column=0,columnspan=20,padx=w//3)
t2=Label(root,text='Add Bus Running Details',bg='seashell2',fg='green3',font='Arial 22 bold')
t2.grid(row=2,column=0,columnspan=20,padx=w//3,pady=20)

bid=Label(root,text='Bus ID',font='Arial 14')
rdate=Label(root,text='Running Date',font='Arial 14')
sav=Label(root,text='Seat Available',font='Arial 14')

import sqlite3
con=sqlite3.connect('pythonbus.db')
cur=con.cursor()

bidf=Entry(root)
rdatef=Entry(root)
savf=Entry(root)

def takehome():
    con.close()
    root.destroy()
    import BuyAdd

def checkblank():
    if bidf.get()=='':
        showerror('BUS ID Error','Bus ID Empty')
        return True
    elif rdatef.get()=='':
        showerror('Date Error','Date Error Empty')
        return True
    elif savf.get()=='':
        showerror('Seats Error','Seats Empty')
        return True
    else:
        return False
def dater():
    olddate=rdatef.get()
    newdate=olddate[6:]+'-'+olddate[3:5]+'-'+olddate[:2]
    return newdate

def addnew2():
    if checkblank()==False:
        dated=dater()
        cur.execute("""insert into runs(runs_busID,runs_date,seat_available)values({},'{}',{})""".format(int(bidf.get()),dated,int(savf.get())))
        con.commit()
        op1=Label(root,text='{} {} {}'.format(bidf.get(),rdatef.get(),savf.get()),font='Arial 12')
        op1.grid(row=4,columnspan=13)
        showinfo('Bus Running Updated','Bus Running Record updated successfully')

def editnew():
    if checkblank()==False:
        dated=dater()
        cur.execute("""delete from runs where runs_busID={}""".format(int(bidf.get())))
        cur.execute("""insert into runs(runs_busID,runs_date,seat_available)values({},'{}',{})""".format(int(bidf.get()),dated,int(savf.get())))
        con.commit()
        op1=Label(root,text='{} {} {}'.format(bidf.get(),rdatef.get(),savf.get()),font='Arial 12')
        op1.grid(row=4,columnspan=13)
        showinfo('Bus Running Updated','Bus Running Record updated successfully')

addb=Button(root,text='Add Run',bg='SpringGreen2',font='Arial 14',command=addnew2)
eb=Button(root,text='Delete Run',bg='SpringGreen2',fg='Red',font='Arial 14',command=editnew)

home=Button(root,image=img1,bg='light green',command=takehome)

bid.grid(row=3,column=1)  #stick=W or E 
bidf.grid(row=3,column=2)
rdate.grid(row=3,column=3)
rdatef.grid(row=3,column=4)
sav.grid(row=3,column=5)
savf.grid(row=3,column=6)

addb.grid(row=3,column=8)
eb.grid(row=3,column=9)

home.grid(row=5,column=8)
root.title('Python Bus Service')
root.mainloop()