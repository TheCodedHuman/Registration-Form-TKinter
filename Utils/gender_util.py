from tkinter import StringVar
from tkinter.ttk import Label, Frame, Radiobutton

class GenderSection:
    def __init__(self, parent, fieldName, genderArr, row=1, column=0):
        self.genderFrame = Frame(parent)
        self.genderFrame.grid(row=row, column=column, sticky="we", padx=5, pady=5)
        self.genderFrame.columnconfigure(1, weight=1)

        # Manipu-Label
        Label(self.genderFrame, text=(fieldName+ ":")).grid(row=0, column=0, sticky="w")

        # Putting all choices in a separate frame
        self.radioFrame = Frame(self.genderFrame)
        self.radioFrame.grid(row=0, column=1, sticky="w", padx=10)
        self.genderVar = StringVar()            # value of chosen RadioButton | can give default value by value parameter

        # Scales to as many genders required (yeah, not necessary tho >:-) )
        for col, gender in enumerate(genderArr, start=1):
            choice = Radiobutton(self.radioFrame, text=(gender.capitalize()), value=(gender.lower()), variable=self.genderVar)
            choice.grid(row=0, column=col, sticky="w", padx=5)

