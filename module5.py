from tkinter import Tk, Button, Label, Entry, CENTER

#module1
#contains tkinter configs

def deleteInstance():

    root1 = Tk()
    root1.title("Search Employee")
    root1.geometry('700x600')
    root1.configure(background ='#0084FF')
    
    Entry (root1, width=20, bg="white").place(x =350, y = 200, anchor = CENTER)
    Label (root1, text ="Delete Entry", bg = '#0084FF' ,fg="white", font="Futura 20 bold").place(x =350, y = 100, anchor = CENTER)
    Button (root1, text="DELETE", width=60).place(x =350, y = 300, anchor = CENTER)
    return root1.mainloop()