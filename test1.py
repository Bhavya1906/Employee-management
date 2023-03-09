def delete_employee():
    indexing=employeeTable.focus()
    print(indexing)
    content = employeeTable.item(indexing)
    contentid = content['values'][0]
    query = 'delete from employee where id = %s,'
    cursor.execute(query, contentid)
    con.commit()
    messagebox.showinfo('Deleted', f'Id {contentid} is deleted successfully')
    query = 'select * from employee'
    cursor.execute(query)
    fetched_data = cursor.fetchall()
    employeeTable.delete(*employeeTable.get_children())
    for data in fetched_data:
        employeeTable.insert('', END, values=data)

import mysql.connector


def delete_employee():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ammulu@1906",
            database="empsys"
        )
            # Connect to the database


        cursor = connection.cursor()

            # Get the index of the selected row
        indexing = employeeTable.focus()
        print(indexing)

            # Get the values of the selected row
        content = employeeTable.item(indexing)
        content_id = content['values'][0]

            # Prepare the SQL query to delete the employee
        query = "DELETE FROM employee WHERE id=%s"
        cursor.execute(query, (content_id,))

        # Commit the changes to the database
        connection.commit()

        print("Employee successfully deleted")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the database connection
        cursor.close()
        connection.close()


def leave(title):
    screen=Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(0,0)
    casualleaveLabel=Label(screen,text='Casual Leave',font=('times new roman',20,'bold'))
    casualleaveLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    casualleaveEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    casualleaveEntry.grid(row=0,column=1,pady=15,padx=10)

    sickleaveLabel=Label(screen,text='Sick Leave',font=('times new roman',20,'bold'))
    sickleaveLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    sickleaveEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    sickleaveEntry.grid(row=1,column=1,pady=15,padx=10)

    medicalleaveLabel=Label(screen,text='Medical Leave',font=('times new roman',20,'bold'))
    medicalleaveLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    medicalleaveEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    medicalleaveEntry.grid(row=2,column=1,pady=15,padx=10)

    submitbutton = ttk.Button(screen,text='Submit')
    submitbutton.grid(row=7,columnspan=2,pady=15)

def apply():
    message = "Enter the following details "
    title = "Leave Apply"
    fieldNames = ["Employee ID", "From", "To", "days"]
    fieldValues = []
    fieldValues = multenterbox(message, title, fieldNames)
    message1 = "Select type of leave"
    title1 = "Type of leave"
    choices = ["Sick leave", "Maternity leave", "Emergency leave"]
    choice = choicebox(message1, title1, choices)
    leaveid = random.randint(1, 1000)

    cursor.execute("INSERT INTO employee(leave_id,employee_id,leave,Date1,Date2,days,status) VALUES (?,?,?,?,?,?,?)",
                 (leaveid, fieldValues[0], choice, fieldValues[1], fieldValues[2], fieldValues[3], "Pending"))
    con.commit()

def LeaveApproval():
    def connect():
        global cursor,con
        try:
            con=conn.connect(host='localhost',user='root',password='Ammulu@1906')
            cursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid details',parent=connectWindow)
            return
        try:
            query='create database empleaves'
            cursor.execute(query)
            query='use status'
            cursor.execute(query)
            query='create table status(employee_id int not null primary key,name varchar(30),mobile varchar(10),email varchar(30),' \
                    'address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))'
            cursor.execute(query)
        except:
            query='use empsys'
            cursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
        connectWindow.destroy()
    message = "Enter leave_id"
    title = "leave approval"
    fieldNames = ["Leave_id"]
    fieldValues = []
    fieldValues = multenterbox(message, title, fieldNames)
    message1 = "Approve/Deny"
    title1 = "leave approval"
    choices = ["approve", "deny"]
    choice = choicebox(message1, title1, choices)

    cursor.execute("UPDATE status SET status = ? WHERE leave_id= ?", (choice, fieldValues[0]))
    con.commit()

    if choice == 'approve':
        print(0)
        cursor.execute("SELECT leave FROM status WHERE leave_id=?", (fieldValues[0],))
        row = cursor.fetchall()
        col = row

        for row in cursor.execute("SELECT employee_id FROM status WHERE leave_id=?", (fieldValues[0],)):
            print(2)
            exampleId = row[0]

        for row in cursor.execute("SELECT days FROM status WHERE leave_id=?", (fieldValues[0],)):
            print(2)
            exampleDays = row[0]

        for row in cursor.execute("SELECT sickleave from balance where employee_id=?", (exampleId,)):
            balance = row[0]
            print(balance)

        for row in cursor.execute("SELECT maternityleave from balance where employee_id=?", (exampleId,)):
            balance1 = row[0]
            print(balance1)

        for row in cursor.execute("SELECT emergencyleave from balance where employee_id=?", (exampleId,)):
            balance2 = row[0]
            print(balance2)

        if (col[0] == ('sickleave',)):
            print(3)
            cursor.execute("UPDATE balance SET sickleave =? WHERE employee_id= ?", ((balance - exampleDays), (exampleId)))

        if (col[0] == ('maternityleave',)):
            print(3)
            cursor.execute("UPDATE balance SET maternityleave =? WHERE employee_id= ?", ((balance1 - exampleDays), (exampleId)))

        if (col[0] == ('emergencyleave',)):
            print(3)
            cursor.execute("UPDATE balance SET emergencyleave =? WHERE employee_id= ?", ((balance2 - exampleDays), (exampleId)))

