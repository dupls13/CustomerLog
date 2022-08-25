from tkinter import *

"""         Start               """
root = Tk()
root.title("Customer Log")

"""         Functions           """


# Empty dictionary to store entries
clients = {}


# Gets phone input and turns to string 
def numberGrab():
    global currentClient
    currentClient = phoneEntry.get()
    currentClient = str(currentClient)

# Gets reason input and turns to string 
def reasonGrab():
    global currentReason
    currentReason = reasonEntry.get()
    currentReason = str(currentReason)
 
# Organizes inputs into dictionary    
def collectInfo():
    clients[currentClient] = currentReason

# Inserts entries and displays dictionary in text area. Also clears input boxes
def insertData():
    clientDisplay.delete("1.0", "end")
    for currentClient, currentReason in clients.items():
        clientDisplay.insert(END, "Client = {}, Reason = {}\n".format(currentClient, currentReason))
    reasonEntry.delete(0, 'end')
    phoneEntry.delete(0, 'end')


# Runs all functions when Submit button is pressed  
def runGrabs():
    numberGrab()
    reasonGrab()
    collectInfo()
    insertData()
    


"""         Display         """


""" ------ Left Side -------- """

#Phone number area
phoneNumber = Label(root, text = "Client's Phone Number: ")
phoneNumber.grid(row = 0, column = 0)

phoneEntry = Entry(root, width = 30, borderwidth = 5)
phoneEntry.grid(row=1, column = 0)

# Reason Area
reason = Label(root, text= "Problem: ")
reason.grid(row=2 , column = 0)

reasonEntry = Entry(root, width = 30, borderwidth = 5)
reasonEntry.grid(row = 3, column = 0)

#Submit Button 
submitButton = Button(root, text = "Submit", command= runGrabs)
submitButton.grid(row = 4, column = 0)



""" ----- Middle Gab -----"""
blankText = Label(root,text = "                  ")
blankText.grid(row=0, column=1)


""" ----- Right Side -----"""

#Right Title 
clientlist = Label(root, text="Client list")
clientlist.grid(row= 0, column = 2, padx = 20)

#Left Display List 
clientDisplay = Text(root)
clientDisplay.grid(row =1, column = 2, rowspan=8, ipady = 50)




"""      Finish             """
root.mainloop()