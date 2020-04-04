from tkinter import Tk, Button, Label, Entry, CENTER

#module1
#contains tkinter configs

def newInstance():

    root1 = Tk()
    root1.title("New Employee")
    root1.geometry('700x600')
    root1.configure(background ='#0084FF')

    user_entry = Entry(root1, width=20, bg="white")
    user_entry.place(x =350, y = 200, anchor = CENTER)
    Label (root1, text ="New Entry", bg = '#0084FF' ,fg="white", font="Futura 20 bold").place(x =350, y = 100, anchor = CENTER)
    Button (root1, text="NEW ENTRY", width=60).place(x =350, y = 300, anchor = CENTER)

    return root1.mainloop()

#To add an event to the button follow the format below and add a function after the width parameter
#Button (root1, text="NEW ENTRY", width=60, command = {Function}).place(x =350, y = 300, anchor = CENTER)

#below is what the code could look like

#def click(): 
    #gets textbox text
    #user_entry=text_entry.get()
    #clears textbox
    #text_output.delete(0.0, END)
    #try:
        #definition = my_dictionary[user_entry]
    #except:
        #definition = "sorry there is no word like that please try again"
    #text_output.insert(END, definition)