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
t2=Label(root,text='Add Bus Details',bg='seashell2',fg='green3',font='Arial 22 bold')
t2.grid(row=2,column=0,columnspan=20,padx=w//3,pady=20)

bid=Label(root,text='Bus ID',font='Arial 14')
btype=Label(root,text='Bus Type',font='Arial 14')
cap=Label(root,text='Capacity',font='Arial 14')
fare=Label(root,text='Fare Rs',font='Arial 14')
opid=Label(root,text='Operator ID',font='Arial 14')
rid=Label(root,text='Route ID',font='Arial 14')
bus_type=StringVar()
bus_type.set('--select--')
option=['AC 2X2','AC 3X2','Non AC 2X2','Non AC 3X2','AC-Sleeper 2X1','Non-AC Sleeper 2X1']
d_menu=OptionMenu(root,bus_type,*option)

import sqlite3
con=sqlite3.connect('pythonbus.db')
cur=con.cursor()

bidf=Entry(root)
opf=Entry(root)
capf=Entry(root)
faref=Entry(root)
ridf=Entry(root)

def checkblank():
    if bidf.get()=='':
        showerror('Bus ID Error','Bus ID Empty')
        return True
    elif opf.get()=='':
        showerror('Operator Error','ID Empty')
        return True
    elif capf.get()=='':
        showerror('Capacity Error','Capacity Empty')
        return True
    elif faref.get()=='':
        showerror('Fare Error','Fare Empty')
        return True
    elif ridf.get()=='':
        showerror('Route ID Error','RID Empty')
        return True
    elif bus_type.get()=='--select--':
        showerror('Bus Error','Bus type not defined')
        return True
    #elif int(bidf.get())!=int and int(opf.get())!=int and int(capf.get())!=int and int(faref.get())!=int and int(ridf.get())!=int:
    #    showerror('Value Error','Value must be a number')
    #    return True
    else:
        return False

def addnew1():
    if checkblank()==False:
        cur.execute("""select busid from bus where busid={}""".format(int(bidf.get())))
        res=cur.fetchall()
        if len(res)!=0:
            showerror('DB Insertion Error','Record Already Exists')
        else:
            cur.execute("""insert into bus (busid,bus_type,bus_opid,capacity,fare,bus_rid)values({},"{}",{},{},{},{})""".format(int(bidf.get()),bus_type.get(),int(opf.get()),int(capf.get()),int(faref.get()),int(ridf.get())))
            con.commit()
            op1=Label(root,text='{} {} {} {} {} {}'.format(bidf.get(),bus_type.get(),capf.get(),faref.get(),opf.get(),ridf.get()),font='Arial 12')
            op1.grid(row=4,columnspan=13)
            showinfo('Bus Entry','Bus Record added')
    
def takehome():
    root.destroy()
    import BuyAdd

def editnew():
    if checkblank()==False:
        cur.execute("""delete from bus where busid={}""".format(int(bidf.get())))
        cur.execute("""insert into bus (busid,bus_type,bus_opid,capacity,fare,bus_rid)values({},"{}",{},{},{},{})""".format(int(bidf.get()),bus_type.get(),int(opf.get()),int(capf.get()),int(faref.get()),int(ridf.get())))
        con.commit()
        op1=Label(root,text='{} {} {} {} {} {}'.format(bidf.get(),bus_type.get(),capf.get(),faref.get(),opf.get(),ridf.get()),font='Arial 12')
        op1.grid(row=4,columnspan=13)
        showinfo('Bus Entry','Bus Record added')

addb=Button(root,text='Add Bus',bg='SpringGreen2',font='Arial 14',command=addnew1)
eb=Button(root,text='Edit Bus',bg='SpringGreen2',font='Arial 14',command=editnew)

home=Button(root,image=img1,bg='light green',command=takehome)

bid.grid(row=3,column=1)  #stick=W or E 
bidf.grid(row=3,column=2)
btype.grid(row=3,column=3)
d_menu.grid(row=3,column=4)
cap.grid(row=3,column=5)
capf.grid(row=3,column=6)
fare.grid(row=3,column=7)
faref.grid(row=3,column=8)
opid.grid(row=3,column=9)
opf.grid(row=3,column=10)
rid.grid(row=3,column=11)
ridf.grid(row=3,column=12)
addb.grid(row=5,column=7)
eb.grid(row=5,column=8)
home.grid(row=5,column=9)
root.title('Python Bus Service')
root.mainloop()