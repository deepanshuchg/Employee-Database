from tkinter import Tk, Button, Label, Entry, CENTER
from module3 import newInstance
from module4 import searchInstance
from module5 import deleteInstance
#module2--Main Screen
#contains main screen ui




def mainInstance():

    root = Tk()
    root.title("Employee Database")
    root.geometry('700x600')
    root.configure(background ='#0084FF')
    
    Label (root, text ="Welcome to Employee DataBase!", bg = '#0084FF' ,fg="white", font="Futura 20 bold").place(x =350, y = 100, anchor = CENTER)

    Button(root, text="NEW ENTRY", width=10,command = newInstance).place(x =200, y =200, anchor = "e") 

    Button(root, text="DELETE", width=10, command=deleteInstance).place(x =350, y =200, anchor = CENTER) 

    Button(root, text="SEARCH", width=10, command=searchInstance).place(x =600, y =200, anchor = "e") 

    return root.mainloop()

#To add an event to the button follow the format below and add a function after the width parameter
#Button (root1, text="NEW ENTRY", width=60, command = {Function}).place(x =350, y = 300, anchor = CENTER)




