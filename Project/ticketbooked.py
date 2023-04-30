from tkinter import *
from tkinter.messagebox import *


mob=0
f=open(".//mobile.txt","r")
mob=f.read()

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\bus.png')
img1=PhotoImage(file='.\\home.png')
bus=Label(root,image=img)
bus.grid(row=0,column=0,columnspan=20,padx=w//3)
t1=Label(root,text='Online Bus Booking System',bg='light blue',fg='Red',font='Arial 32 bold')
t1.grid(row=1,column=0,columnspan=20,padx=w//3)
t2=Label(root,text='Bus Ticket',font='Arial 16 bold')
t2.grid(row=2,column=0,columnspan=20,padx=w//3,pady=20)

frame1=Frame(root,relief='groove',bd=5)
frame1.grid(row=4,column=0,columnspan=8,rowspan=10,padx=w//3)

import sqlite3
con=sqlite3.connect('pythonbus.db')
cur=con.cursor()
cur.execute("""select max(ref_number) from bookinghistory""")
temp=cur.fetchone()
cur.execute("""select * from bookinghistory where ref_number={}""".format(temp[0]))
res=cur.fetchall()
pname='Passengers:'+res[0][0]
mobile='Phone:'+str(int(res[0][1]))
age='Age:'+str(int(res[0][2]))
seats='No of Seats:'+str(res[0][3])
from_st='Boarding Point:'+str(res[0][4])
to_st='Destination Point:'+str(res[0][5])
date_booked='Booked On:'+str(res[0][6])
ref_number='Booking Ref.'+str(res[0][7])
sex='Gender:'+str(res[0][8])
date_bus='Travel On:'+str(res[0][9])
fare='Fare Rs. :'+str(res[0][10])+'*'
op_name='Bus Detail:'+str(res[0][11])
term='*Total amount of Rs'+str(res[0][3]*res[0][10])+'/- to be paid at the time of boarding the bus'
Label(frame1,text=pname,font='Arial 12 bold').grid(row=4,column=1,padx=5)
Label(frame1,text=mobile,font='Arial 12 bold').grid(row=4,column=2,padx=5)
Label(frame1,text=age,font='Arial 12 bold').grid(row=5,column=1,padx=5)
Label(frame1,text=ref_number,font='Arial 12 bold').grid(row=5,column=2,padx=5)
Label(frame1,text=from_st,font='Arial 12 bold').grid(row=6,column=1,padx=5)
Label(frame1,text=to_st,font='Arial 12 bold').grid(row=6,column=2,padx=5)
Label(frame1,text=date_booked,font='Arial 12 bold').grid(row=7,column=1,padx=5)
Label(frame1,text=date_bus,font='Arial 12 bold').grid(row=7,column=2,padx=5)
Label(frame1,text=sex,font='Arial 12 bold').grid(row=8,column=1,padx=5)
Label(frame1,text=seats,font='Arial 12 bold').grid(row=8,column=2,padx=5)
Label(frame1,text=op_name,font='Arial 12 bold').grid(row=9,column=1,padx=5)
Label(frame1,text=fare,font='Arial 12 bold').grid(row=9,column=2,padx=5)
Label(frame1,text=term,font='Arial 8 italic').grid(row=10,column=1,columnspan=2)
showinfo('Success','Seat Booked!')
choice=0
def on_closing():
    choice=askyesnocancel('Closing','For Closing: Click Yes\nGoto to home page:Click No')
    if choice==True :
        showinfo('Thanks','Thank you for using Python Bus Service')
        root.destroy()
    elif choice==False:
        root.destroy()
        import BuyAdd

root.title('Ticket Booked')
root.protocol("WM_DELETE_WINDOW",on_closing)
root.mainloop()