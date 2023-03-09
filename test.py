from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import mysql.connector as conn
import pymysql
import pymongo
import pandas
from easygui import *
import random


def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=employeeTable.get_children()
    newlist=[]
    for index in indexing:
        content=employeeTable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','DOB','Added date','Added time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved successfully')



def toplvel_data(title,button_text,command):
    global idEntry,phoneEntry,nameEntry,emailEntry,addressEntry,dobEntry,genderEntry,screen
    screen=Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(0,0)
    idLabel=Label(screen,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel=Label(screen,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)

    phoneLabel=Label(screen,text='Phone',font=('times new roman',20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    phoneEntry.grid(row=2,column=1,pady=15,padx=10)

    emailLabel=Label(screen,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)

    addressLabel=Label(screen,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,pady=15,padx=10)

    genderLabel=Label(screen,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,pady=15,padx=10)

    dobLabel=Label(screen,text='D.O.B',font=('times new roman',20,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,pady=15,padx=10)

    #numofleavesLabel=Label(screen,text='Num of Leaves',font=('times new roman',20,'bold'))
    #numofleavesLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    #numofleavesEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    #numofleavesEntry.grid(row=6,column=1,pady=15,padx=10)

    employye_button = ttk.Button(screen,text=button_text,command=command)
    employye_button.grid(row=7,columnspan=2,pady=15)

    if title=='Update employee':
        indexing=employeeTable.focus()
        print(indexing)
        content=employeeTable.item(indexing)
        listdata=content['values']
        idEntry.insert(0,listdata[0])
        nameEntry.insert(0,listdata[1])
        phoneEntry.insert(0,listdata[2])
        emailEntry.insert(0,listdata[3])
        addressEntry.insert(0,listdata[4])
        genderEntry.insert(0,listdata[5])
        dobEntry.insert(0,listdata[6])

def update_data():
    query='update employee set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
    cursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),genderEntry.get(),
                          addressEntry.get(),dobEntry.get(),date,cur_time,idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_emp()

def show_emp():
    query = 'select * from employee'
    cursor.execute(query)
    fetched_data = cursor.fetchall()
    employeeTable.delete(*employeeTable.get_children())
    for data in fetched_data:
        employeeTable.insert('', END, values=data)


def delete_employee():
    indexing=employeeTable.focus()
    print(indexing)
    content = employeeTable.item(indexing)
    contentid = content['values'][0]
    query = 'delete from employee where id = %s'
    cursor.execute(query, (contentid,))
    con.commit()
    messagebox.showinfo('Deleted', f'Id {contentid} is deleted successfully')
    query = 'select * from employee'
    cursor.execute(query)
    fetched_data = cursor.fetchall()
    employeeTable.delete(*employeeTable.get_children())
    for data in fetched_data:
        employeeTable.insert('', END, values=data)




def search_data():
    query='select * from employee where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
    cursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
    employeeTable.delete(*employeeTable.get_children())
    fetched_data=cursor.fetchall()
    for data in fetched_data:
        datalist = list(data)
        employeeTable.insert('', END, values=datalist)


def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror('Error','All fields are required',parent=screen)

    else:
        try:
            query='insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get()
                                  ,genderEntry.get(),dobEntry.get(),date,cur_time))
            con.commit()
            result=messagebox.askyesno('Confirm','Data added successfully, Do you want to clean the form?',parent=screen)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0, END)
                phoneEntry.delete(0, END)
                emailEntry.delete(0, END)
                addressEntry.delete(0, END)
                genderEntry.delete(0, END)
                dobEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            return

        query='select * from employee'
        cursor.execute(query)
        fetched_data = cursor.fetchall()
        employeeTable.delete(*employeeTable.get_children())
        for data in fetched_data:
            datalist=list(data)
            employeeTable.insert('',END,values=datalist)


def connect_db():
    def connect():
        global cursor,con
        try:
            con=conn.connect(host='localhost',user='root',password='Ammulu@1906')
            cursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid details',parent=connectWindow)
            return
        try:
            query='create database empsys'
            cursor.execute(query)
            query='use empsys'
            cursor.execute(query)
            query='create table employee(id int not null primary key,name varchar(30),mobile varchar(10),email varchar(30),' \
                    'address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))'
            cursor.execute(query)
        except:
            query='use empsys'
            cursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
        connectWindow.destroy()
        addemployeeButton.config(state=NORMAL)
        searchemployeeButton.config(state=NORMAL)
        deleteemployeeButton.config(state=NORMAL)
        updateemployeeButton.config(state=NORMAL)
        exportemployeeButton.config(state=NORMAL)
        showemployeeButton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x280+730+230')
    connectWindow.title('Database connection')
    connectWindow.resizable(False,False)

    hostnameLabel = Label(connectWindow,text='Host name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=40,pady=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1)

    usernameLabel = Label(connectWindow,text='User name',font=('arial',20,'bold'))
    usernameLabel.grid(row=1,column=0,padx=40,pady=20)

    usernameEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    usernameEntry.grid(row=1,column=1)

    passwordLabel = Label(connectWindow,text='password',font=('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0,padx=40,pady=20)

    passwordEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)


count=0
text=''
def slider():
    global text, count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)



def clock():
    global date,cur_time
    date = time.strftime('%d/%m/%Y')
    cur_time = time.strftime('%H:%M:%S')
    #print(date,cur_time)
    datatimeLabel.config(text=f'   Date: {date}\nTime: {cur_time}')
    datatimeLabel.after(1000,clock)



root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1240x780+0+0')
root.resizable(0,0)
root.title('Employee Management System')

datatimeLabel = Label(root,font=('times new roman',18,'bold'))
datatimeLabel.place(x=5,y=5)

clock()
s='Employee Management System'
sliderLabel = Label(root,text=s,font=('arial',28,'italic bold'),width=30)
#sliderLabel = Label(root,font=('arial',28,'italic bold'),width=30)  #doesn't make any diff
sliderLabel.place(x=250,y=0)
slider()

connectButton = ttk.Button(root,text='Connect database',command=connect_db)
connectButton.place(x=980,y=0)

leftframe = Frame(root)
leftframe.place(x=50,y=80,width=300,height=750)

logo_image = PhotoImage(file='students.png')
logo_Label = Label(leftframe,image=logo_image)
logo_Label.grid(row=0,column=0)

addemployeeButton=ttk.Button(leftframe,text='Add Employee',width=25,state=DISABLED,command=lambda :toplvel_data('Add employee','Add',add_data))
addemployeeButton.grid(row=1,column=0,pady=20)

searchemployeeButton=ttk.Button(leftframe,text='Search Employee',width=25,state=DISABLED,command=lambda :toplvel_data('Search employee','Search',search_data))
searchemployeeButton.grid(row=2,column=0,pady=20)

deleteemployeeButton=ttk.Button(leftframe,text='Delete Employee',width=25,state=DISABLED,command=delete_employee)
deleteemployeeButton.grid(row=3,column=0,pady=20)

updateemployeeButton=ttk.Button(leftframe,text='Update Employee',width=25,state=DISABLED,command=lambda :toplvel_data('Update employee','Update',update_data))
updateemployeeButton.grid(row=4,column=0,pady=20)

showemployeeButton=ttk.Button(leftframe,text='Show Employee',width=25,state=DISABLED,command=show_emp)
showemployeeButton.grid(row=5,column=0,pady=20)

exportemployeeButton=ttk.Button(leftframe,text='Export data',width=25,state=DISABLED,command=export_data)
exportemployeeButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftframe,text='Exit',width=25,command=iexit)
exitButton.grid(row=7,column=0,pady=20)


rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=700)

scrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollbarY=Scrollbar(rightFrame,orient=VERTICAL)


employeeTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile no','Email','Address','Gender','DOB','Added date','Added time')
                           ,xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)

scrollbarX.config(command=employeeTable.xview)
scrollbarY.config(command=employeeTable.yview)

scrollbarX.pack(side=BOTTOM,fill=X)
scrollbarY.pack(side=RIGHT,fill=Y)

employeeTable.pack(fill=BOTH,expand=1)

employeeTable.heading('Id',text='Id')
employeeTable.heading('Name',text='Name')
employeeTable.heading('Mobile no',text='Mobile no')
employeeTable.heading('Email',text='Email')
employeeTable.heading('Address',text='Address')
employeeTable.heading('Gender',text='Gender')
employeeTable.heading('DOB',text='DOB')
employeeTable.heading('Added date',text='Added date')
employeeTable.heading('Added time',text='Added time')

employeeTable.column('Id',width=50,anchor=CENTER)
employeeTable.column('Name',width=200,anchor=CENTER)
employeeTable.column('Email',width=300,anchor=CENTER)
employeeTable.column('Mobile no',width=200,anchor=CENTER)
employeeTable.column('Address',width=200,anchor=CENTER)
employeeTable.column('Gender',width=100,anchor=CENTER)
employeeTable.column('DOB',width=100,anchor=CENTER)
employeeTable.column('Added date',width=150,anchor=CENTER)
employeeTable.column('Added time',width=150,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview',rowheight=30,font=('arial',12,'bold'),fg='red4',fieldbg='white')
style.configure('Treeview.Heading',font=('arial',15,'bold'),fg='blue')

employeeTable.config(show='headings')


root.mainloop()