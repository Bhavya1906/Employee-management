from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or pswrdEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Admin' and pswrdEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import test

    else:
        messagebox.showerror('Error','Please enter correct details')



window = Tk()

window.geometry('1280x855+0+0')
window.title('Login system of Administrative')
window.resizable(False,False)

backgr = ImageTk.PhotoImage(file='image1.jpg')
bgLabel = Label(window,image=backgr)
bgLabel.place(x=0,y=0)

loginframe = Frame(window,bg='snow2')
loginframe.place(x=400,y=150)

logoImage = PhotoImage(file='student.png')
logoLabel = Label(loginframe,image = logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameImage = PhotoImage(file='user.png')
usernameLabel = Label(loginframe,image=usernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'))
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry = Entry(loginframe,font=('times new roman',20,'bold'),bd=5,fg='blue4')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

pswrdImage = PhotoImage(file='locked.png')
passwordLabel = Label(loginframe,image=pswrdImage,text='password',compound=LEFT,font=('times new roman',20,'bold'))
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

pswrdEntry = Entry(loginframe,font=('times new roman',20,'bold'),bd=5,fg='blue4')
pswrdEntry.grid(row=2,column=1,pady=10,padx=20)

loginbutton = Button(loginframe,text='login',font=('times new roman',18,'bold'),width=15,fg='white',bg='cornflower blue'
                     ,activebackground='cornflower blue',activeforeground='white',cursor='hand2',command=login)
loginbutton.grid(row=3,column=1,pady=10)



window.mainloop()