from tkinter import Tk, Button, Label, Entry, CENTER

#module4
#contains search Entry GUI

#to add a button

def searchInstance():

    root1 = Tk()
    root1.title("Search Employee")
    root1.geometry('700x600')
    root1.configure(background ='#0084FF')
    
    Entry (root1, width=20, bg="white").place(x =350, y = 200, anchor = CENTER)
    Label (root1, text ="Search Entry", bg = '#0084FF' ,fg="white", font="Futura 20 bold").place(x =350, y = 100, anchor = CENTER)
    Button (root1, text="SEARCH", width=60).place(x =350, y = 300, anchor = CENTER)

    return root1.mainloop()

#To add an event to the button follow the format below and add a function after the width parameter
#Button (root1, text="SEARCH", width=60, command = {Function}).place(x =350, y = 300, anchor = CENTER)
