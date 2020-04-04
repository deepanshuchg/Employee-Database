from tkinter import Tk, Button, Label, Entry, CENTER
import openpyxl
#module4--Search Employee
#contains search Entry GUI

wb = openpyxl.load_workbook('employee_data_2.xlsx')               #This connected with the excel file
sheet = wb.active                                               #Connects with the active sheet

#to add a button

def search_data(search_emp_id):                                 #Function to search for an entry
    flag=False
    for i in range(2,sheet.max_row+1):
        if(sheet.cell(row=i,column=1).value==int(search_emp_id)):                       
            message = ("Employee ID: " + search_emp_id +"\nFirst Name: " + sheet.cell(row=i,column=2).value+ "\nLast Name: " + sheet.cell(row=i,column=3).value +
            "\nCity: " + sheet.cell(row=i,column=4).value + "\nZip: " + str(sheet.cell(row=i,column=5).value) + "\nPhone number: " + sheet.cell(row=i,column=6).value ) 
            #These above statement returns all the value in a single string- This can be done better but I couldn't find how.
            flag = True
            return message
            

    if (flag == False):                               #If no entry is found with that employee ID
        return("Sorry, No data found with that employee ID.")

def searchInstance():

    root1 = Tk()
    root1.title("Search Employee")
    root1.geometry('700x600')
    root1.configure(background ='#0084FF')

    lb2= Label(root1,text="", bg = '#0084FF' ,fg="white", font="Futura 12 bold")            #This label will display confirmation message
    lb2.place(x=280,y=420)
    
    Label (root1, text ="Search Entry", bg = '#0084FF' ,fg="white", font="Futura 20 bold").place(x =350, y = 100, anchor = CENTER)
    Label(root1,text="Enter employee ID:",bg = '#0084FF' ,fg="white", font="Futura 12 bold").place(x=200,y=200,anchor=CENTER)
    user_entry = Entry (root1, width=20, bg="white")
    user_entry.place(x =350, y = 200, anchor = CENTER)

    def clicked():
        emp_id = user_entry.get()
        message = search_data(emp_id)
        lb2.configure(text=message)
    Button (root1, text="SEARCH", width=60, command= clicked).place(x =350, y = 300, anchor = CENTER)

    return root1.mainloop()

#To add an event to the button follow the format below and add a function after the width parameter
#Button (root1, text="SEARCH", width=60, command = {Function}).place(x =350, y = 300, anchor = CENTER)
