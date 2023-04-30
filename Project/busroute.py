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
t2=Label(root,text='Add Bus Route Details',bg='seashell2',fg='green3',font='Arial 22 bold')
t2.grid(row=2,column=0,columnspan=20,padx=w//3,pady=20)

rid=Label(root,text='Route ID',font='Arial 14')
stname=Label(root,text='Station Name',font='Arial 14')
stid=Label(root,text='Station ID',font='Arial 14')

ridf=Entry(root)
stnamef=Entry(root)
stidf=Entry(root)

import sqlite3
con=sqlite3.connect('pythonbus.db')
cur=con.cursor()

def checkblank():
    if ridf.get()=='':
        showerror('Route ID Error','Route ID Empty')
        return True
    elif stnamef.get()=='':
        showerror('Station Error','Station Name Empty')
        return True
    elif stidf.get()=='':
        showerror('Station Error','Station ID Empty')
        return True
    else:
        return False

def takehome():
    con.close()
    root.destroy()
    import BuyAdd

def addnew():
    if checkblank()==False:
        cur.execute("""insert into route (rid,stid,station_name)values({},{},"{}")""".format(int(ridf.get()),int(stidf.get()),stnamef.get()))
        con.commit()
        op1=Label(root,text='{} {} {}'.format(ridf.get(),stnamef.get(),stidf.get()),font='Arial 12')
        op1.grid(row=4,columnspan=13)
        showinfo('Route Entry Updated','Bus Route Record updated successfully')
    
def editnew():
    if checkblank()==False:
        cur.execute("""select * from route where rid={} and stid={}""".format(int(ridf.get()),int(stidf.get())))
        res=cur.fetchall()
        if(len(res)==0):
            showerror('No Route','No Route Found with specified Details to delete')
            return
        else:
            cur.execute("""delete from route where rid={} and stid={}""".format(int(ridf.get()),int(stidf.get())))
            con.commit()
        op1=Label(root,text='{} {} {}'.format(ridf.get(),stnamef.get(),stidf.get()),font='Arial 12')
        op1.grid(row=4,columnspan=13)
        showinfo('Route Entry Updated','Bus Route Record updated successfully')

addb=Button(root,text='Add Route',bg='SpringGreen2',font='Arial 14',command=addnew)
eb=Button(root,text='Delete Route',bg='SpringGreen2',fg='Red',font='Arial 14',command=editnew)

home=Button(root,image=img1,bg='light green',command=takehome)

rid.grid(row=3,column=1)  #stick=W or E 
ridf.grid(row=3,column=2)
stname.grid(row=3,column=3)
stnamef.grid(row=3,column=4)
stid.grid(row=3,column=5)
stidf.grid(row=3,column=6)

addb.grid(row=3,column=8)
eb.grid(row=3,column=9)

home.grid(row=5,column=7)
root.title('Python Bus Service')
root.mainloop() 