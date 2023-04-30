from tkinter import *
from tkinter.messagebox import *
import sqlite3

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\bus.png')
img1=PhotoImage(file='.\\home.png')
bus=Label(root,image=img)
bus.grid(row=0,column=0,columnspan=20,padx=w//3)
t1=Label(root,text='Online Bus Booking System',bg='light blue',fg='Red',font='Arial 32 bold')
t1.grid(row=1,column=0,columnspan=20,padx=w//3)
t2=Label(root,text='Add Bus Operator Details',bg='seashell2',fg='green3',font='Arial 22 bold')
t2.grid(row=2,column=0,columnspan=20,padx=w//3,pady=20)

opid=Label(root,text='Operator ID',font='Arial 14')
name=Label(root,text='Name',font='Arial 14')
add=Label(root,text='Address',font='Arial 14')
ph=Label(root,text='Phone',font='Arial 14')
mail=Label(root,text='Email',font='Arial 14')

con=sqlite3.Connection('pythonbus.db')
cur=con.cursor()

opf=Entry(root)
nf=Entry(root)
addf=Entry(root)
phf=Entry(root)
mf=Entry(root)

frame1=Frame(root)
frame1.grid(row=4,column=0,columnspan=13)

def checkblank():
    if opf.get()=='':
        showerror('Operator ID Error','Operator ID Empty')
        return True
    elif nf.get()=='':
        showerror('Name Error','Name Empty')
        return True
    elif addf.get()=='':
        showerror('Address Error','Address Empty')
        return True
    elif phf.get()=='':
        showerror('Phone Error','Phone Empty')
        return True
    elif mf.get()=='':
        showerror('Mail Error','Email Empty')
        return True
    else:
        return False


def addnew():
    if checkblank()==False:
        cur.execute("""insert into operator (opid,name,phone,address,email)values({},"{}",{},"{}","{}")""".format(int(opf.get()),nf.get(),int(phf.get()),addf.get(),mf.get()))
        con.commit()
        op1=Label(frame1,text='{} {} {} {} {}'.format(opf.get(),nf.get(),addf.get(),phf.get(),mf.get()),font='Arial 12')
        op1.grid(row=4)
        showinfo('Operator Entry Updated','Operator Record updated successfully')
    
def editnew():
    if checkblank()==False:
        cur=con.cursor()
        cur.execute("""delete from operator where opid={}""".format(int(opf.get())))
        cur.execute("""insert into operator (opid,name,phone,address,email)values({},"{}",{},"{}","{}")""".format(int(opf.get()),nf.get(),int(phf.get()),addf.get(),mf.get()))
        con.commit()
        op1=Label(frame1,text='{} {} {} {} {}'.format(opf.get(),nf.get(),addf.get(),phf.get(),mf.get()),font='Arial 12')
        op1.grid(row=4)
        showinfo('Operator Entry Updated','Operator Record updated successfully')
        
        
    
addb=Button(root,text='Add',bg='SpringGreen2',font='Arial 14',command=addnew)   
eb=Button(root,text='Edit',bg='SpringGreen2',font='Arial 14',command=editnew)

def takehome():
    con.close()
    root.destroy()
    import BuyAdd

home=Button(root,image=img1,bg='light green',command=takehome)

opid.grid(row=3,column=1)  #stick=W or E 
opf.grid(row=3,column=2)
name.grid(row=3,column=3)
nf.grid(row=3,column=4)
add.grid(row=3,column=5)
addf.grid(row=3,column=6)
ph.grid(row=3,column=7)
phf.grid(row=3,column=8)
mail.grid(row=3,column=9)
mf.grid(row=3,column=10)
addb.grid(row=3,column=11)
eb.grid(row=3,column=12)

home.grid(row=5,column=9)
root.title('Python Bus Service')
root.mainloop()