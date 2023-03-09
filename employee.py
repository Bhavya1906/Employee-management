from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')

        lbl_title = Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='red',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)


if __name__=="__main__":
    root=Tk()
    obj= Employee(root)
    root.mainloop()