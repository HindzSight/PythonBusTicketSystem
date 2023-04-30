from tkinter import *
from tkinter.messagebox import *

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\bus.png')
img1=PhotoImage(file='.\\home.png')
bus=Label(root,image=img)
bus.grid(row=0,column=0,columnspan=12,padx=w//3)
t1=Label(root,text='Online Bus Booking System',bg='light blue',fg='Red',font='Arial 32 bold')
t1.grid(row=1,column=0,columnspan=12,padx=w//3)
detailtxt=Label(root,text='Enter Journey Details',fg='green4',bg='light green',font='Arial 16 bold')
detailtxt.grid(row=2,column=0,columnspan=12,padx=w//3,pady=20)

frame1=Frame(root)
frame1.grid(row=3,column=0,columnspan=12)

frame2=Frame(root)
frame2.grid(row=8,column=0,columnspan=20,pady=20)

import sqlite3
con=sqlite3.connect('pythonbus.db')
cur=con.cursor()

bus_select=IntVar()
tof=Entry(frame1)
fromf=Entry(frame1)
datef=Entry(frame1)



def confirmamt():
    if(checkerrordetails()==False):
        cur.execute("""select fare,name from bus,operator where busid={} and bus_opid=opid""".format(bus_select.get(),bus_select.get()))
        price=cur.fetchall()
        amt=price[0][0]
        opname=price[0][1]
        with open(".//mobile.txt","r+") as f:
            f.write("{}".format(int(mobilef.get())))
            print(f.read())
        ans=askquestion('Fare Confirmation','Total amount to be paid is Rs {}'.format(amt*int(seatsf.get())))
        if ans=='yes':
            cur.execute("""select DATE('now')""")
            date=cur.fetchall()
            curdate=date[0][0]
            dated=dater()
            cur.execute("""insert into bookinghistory (pname,mobile,age,seats,from_station,to_station,date_booked,gender,boarding_date,fare,op_name)values("{}",{},{},{},"{}","{}","{}","{}","{}",{},"{}")""".format(namef.get(),mobilef.get(),agef.get(),seatsf.get(),fromf.get(),tof.get(),curdate,sex_mf.get(),dated,amt,opname))
            cur.execute("""update runs set seat_available=seat_available-{} where runs_busid={}""".format(int(seatsf.get()),bus_select.get()))
            con.commit()
            root.destroy()            
            import ticketbooked
        else:
            return


def dater():
    olddate=datef.get()
    newdate=olddate[6:]+'-'+olddate[3:5]+'-'+olddate[:2]
    return newdate


def showbuses():
    if(checkerrortofromdate()==False):
        frame=Frame(root)
        frame.grid(row=5,column=0,columnspan=12)
        dated=dater()
        cur.execute("""select op.name,b.bus_type,r.seat_available,b.capacity,b.fare,b.bus_opid,st.stid as start_st,ed.stid as end_st from operator as op,bus as b,route as st,route as ed,runs as r where r.runs_date='{}' and st.station_name="{}" and ed.station_name="{}" and st.stid< ed.stid and st.rid=ed.rid and b.bus_rid=st.rid and b.bus_opid=op.opid and r.runs_busid=b.busid""".format(dated,fromf.get(),tof.get()))
        res=cur.fetchall()
        buses_count=len(res)
        
        select_bus=Label(frame,text='Select Bus',fg='green3',font='Arial 14 bold')
        op=Label(frame,text='Operator',fg='green3',font='Arial 14')
        bus_type=Label(frame,text='Bus Type',fg='green3',font='Arial 14')
        avail=Label(frame,text='Available/Capacity',fg='green3',font='Arial 14')
        fare=Label(frame,text='Fare',fg='green3',font='Arial 14')
        bookproceed=Button(frame,text='Proceed to book',bg='light green',font='Arial 14',command=proceedtobook)
        
        if buses_count==0:
            showerror('No BUS','NO BUSES FOUND')
            return
        i=0
        for i in range(0,buses_count):
            Radiobutton(frame,text='Bus'+str(i+1),variable=bus_select, value=res[i][5]).grid(row=5+i,column=1)
            Label(frame,text=res[i][0],font='Arial 12',fg='blue').grid(row=5+i,column=2)
            Label(frame,text=res[i][1],font='Arial 12',fg='blue').grid(row=5+i,column=3)
            Label(frame,text=str(res[i][2])+'/'+str(res[i][3]),font='Arial 12',fg='blue').grid(row=5+i,column=4)
            Label(frame,text=res[i][4],font='Arial 12',fg='blue').grid(row=5+i,column=5)
            
        select_bus.grid(row=4,column=1,padx=5)
        op.grid(row=4,column=2,padx=5)
        bus_type.grid(row=4,column=3,padx=5)
        avail.grid(row=4,column=4,padx=5)
        fare.grid(row=4,column=5,padx=5)
        bookproceed.grid(row=6+i,column=7)

filldetail=Label(frame2,text='Fill Passenger Details to book the bus ticket',bg='light blue',fg='Red',font='Arial 24 bold')
name=Label(frame2,text='Name',font='Arial 14 bold')
sex=Label(frame2,text='Gender',font='Arial 14 bold')
sex_mf=StringVar()
sex_mf.set('--M/F--')
option=['Male','Female','Other']
s_menu=OptionMenu(frame2,sex_mf,*option)
seats=Label(frame2,text='No of Seats',font='Arial 14 bold')
mobile=Label(frame2,text='Mobile No',font='Arial 14 bold')
age=Label(frame2,text='Age',font='Arial 14 bold')
namef=Entry(frame2)
seatsf=Entry(frame2)
mobilef=Entry(frame2)
agef=Entry(frame2)


def proceedtobook():
    if bus_select.get()==0:
        showerror('SELECT ERROR','NO BUS SELECTED')
    else:
        bookseat=Button(frame2,text='Book Seat',bg='light green',font='Arial 14',command=confirmamt)
        dated=dater()
        cur.execute("""select b.fare,b.bus_opid,st.stid as start_st,ed.stid as end_st from bus as b,route as st,route as ed,runs as r where r.runs_date='{}' and st.station_name="{}" and ed.station_name="{}" and st.stid< ed.stid and st.rid=ed.rid and b.busid={}""".format(dated,fromf.get(),tof.get(),bus_select.get()))
        bus_detail=cur.fetchall()
        filldetail.grid(row=7,column=0,columnspan=20,pady=15)
        name.grid(row=8,column=1)
        namef.grid(row=8,column=2)
        sex.grid(row=8,column=3)
        s_menu.grid(row=8,column=4)
        seats.grid(row=8,column=5)
        seatsf.grid(row=8,column=6)
        mobile.grid(row=8,column=7)
        mobilef.grid(row=8,column=8)
        age.grid(row=8,column=9)
        agef.grid(row=8,column=10)
        bookseat.grid(row=8,column=11)

def checkerrortofromdate():
    if fromf.get()=='':
        showerror('Error','Source Empty')
        return True
    elif tof.get()=='':
        showerror('Error','Destination Empty')
        return True
    elif datef.get()=='':
        showerror('Error','Date Empty')
        return True
    else:
        return False

def checkerrordetails():
    if namef.get()=='':
        showerror('Error','Name Empty')
        return True
    elif sex_mf=='':
        showerror('Error','No Gender Selected')
        return True
    elif mobilef.get()=='':
        showerror('Error','No Mobile No Entered')
        return True
    elif agef.get()=='':
        showerror('Error','No Age Entered')
        return True
    elif seatsf.get()=='':
        showerror('Error','No Seats Entered')
        return True
    else:
        return False

def takehome():
    root.destroy()
    import BuyAdd


to=Label(frame1,text='To',font='Arial 12')
From=Label(frame1,text='From',font='Arial 12')
date=Label(frame1,text='Journey Date',font='Arial 12')
show=Button(frame1,text='Show Bus',command=showbuses,bg='SeaGreen1',font='Arial 16 bold')
home=Button(frame1,image=img1,bg='light green',command=takehome)

to.grid(row=3,column=1,sticky=E,padx=10)
tof.grid(row=3,column=2,sticky=W,padx=10)
From.grid(row=3,column=3,sticky=E,padx=10)
fromf.grid(row=3,column=4,sticky=W,padx=10)
date.grid(row=3,column=5,sticky=E,padx=10)
datef.grid(row=3,column=6,sticky=W,padx=10)
show.grid(row=3,column=7,padx=10)
home.grid(row=3,column=8,padx=10)

root.title('Booking Window')
root.mainloop()