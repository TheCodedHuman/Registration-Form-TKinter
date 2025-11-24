from tkinter.ttk import Label, Entry, Frame

class Entries:
    def __init__(self, parent, name, row, is_password=False, focused=False):
        Label(parent, text=f"{name}:").grid(row=row, column=0, sticky="w", pady=5)


        self.entryField = Entry(parent, show="*" if is_password else None)
        self.entryField.grid(row=row, column=1, sticky="we")
        if focused: self.entryField.focus()
    
    def get(self): return self.entryField.get()
    def reset(self): return self.entryField.delete(0, "end")
             

class EntrySection:
    def __init__(self, parent, row=0, column=0):
        self.entryFrame = Frame(parent, padding=(0, 5))
        self.entryFrame.grid(row=row, column=column, sticky="we")
        self.entryFrame.columnconfigure(1, weight=1)

        self.nameField = Entries(self.entryFrame, "Name", row=0, focused=True)
        self.emailField = Entries(self.entryFrame, "Email", row=1)
        self.pwField = Entries(self.entryFrame, "Password", row=2, is_password=True)


    # getter
    def get_values(self):
        return {                                    # json ready dict
            "name": self.nameField.get(),
            "email": self.emailField.get(),
            "password": self.pwField.get()
        }
    
    # reset/clear
    def clear(self):
        self.nameField.reset()
        self.emailField.reset()
        self.pwField.reset()

