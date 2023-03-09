from django.db import models
from easygui import *
import random


Leave_type = (
    ('CL', 'Casual Leave'),
   ('SL', 'Sick Leave'),
   ('ML', 'Medical Leave'),
    ('Comp Off', 'Compensation'),
    ('L.O.P', 'Loss of Pay')
 )


Leave_Choice = (
    ('Full Day', 'Full Day Leave'),
    ('Half Day', 'Half Day Only'),
)

Status_choices = (
     ('Approved', 'approved'),
     ('Rejected', 'Rejected'),
    ('Pending', 'Pending'),
 )

leave_type = models.CharField(max_length=50, choices=Leave_type)
status = models.CharField(max_length=50, choices=Status_choices, default='Pending')
leave_choice = models.CharField(max_length=50, choices=Leave_Choice, default='Full Day')

if leave_type == 'CL':
    total_leave_per_year = 24
    monthly_leave_applicable = 2
    carry_forawrd_monthly_leave = 3

elif leave_type == 'SL':
    Quarterly_days_applicable = 2
    annual_leave_applicable = 8


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

    con.execute("INSERT INTO employee(leave_id,employee_id,leave,Date1,Date2,days,status) VALUES (?,?,?,?,?,?,?)",
                 (leaveid, fieldValues[0], choice, fieldValues[1], fieldValues[2], fieldValues[3], "Pending"))
    con.commit()