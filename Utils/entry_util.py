from tkinter.ttk import Label, Entry, Frame

class Entries:
    def __init__(self, parent, name, row):
        Label(parent, text=(name + ":")).grid(row=row, column=0, sticky="w", padx=5, pady=5)
        self.entryField = Entry(parent)
        self.entryField.grid(row=row, column=1, sticky="we")
             

class EntrySection:
    def __init__(self, parent, row=0, column=0):
        self.entryFrame = Frame(parent)
        self.entryFrame.grid(row=row, column=column, sticky="we")
        self.entryFrame.columnconfigure(1, weight=1)

        self.nameField = Entries(self.entryFrame, "Name", row=0)
        self.emailField = Entries(self.entryFrame, "Email", row=1)
        self.pwField = Entries(self.entryFrame, "Password", row=2)

