from tkinter import StringVar
from tkinter.ttk import Label, Frame, Combobox

class CountrySection:
    def __init__(self, parent, fieldName, countryArr, row=2, column=0):
        self.countryFrame = Frame(parent, padding=(0, 5))
        self.countryFrame.grid(row=row, column=column, sticky="we")
        self.countryFrame.columnconfigure(1, weight=1)

        # Country Label
        Label(self.countryFrame, text=f"{fieldName}:").grid(row=0, column=0, sticky="w", padx=5, pady=5)

        # Extract Country_Names
        self.countryVar = StringVar()
        self.countryArr = ["Select Country"] + countryArr

        # create as normal first, set values/current, then switch to readonly
        self.countryDropdown = Combobox(self.countryFrame,
                                        textvariable=self.countryVar,
                                        width=30,
                                        state="normal",
                                        values=self.countryArr)
        self.countryDropdown.current(0)             # default first country
        self.countryDropdown.grid(row=0, column=1, sticky="w", padx=10)      
        self.countryDropdown.bind('<Return>', self.on_enter)


    # getter
    def get_values(self): return { "country": self.countryVar.get()}

    # clear/reset
    def clear(self): self.countryVar.set("Select Country")

    # serach country by key-taps
    def on_enter(self, event):
        value = self.countryVar.get().strip().lower()

        if value == '':
            data = self.countryArr
        else:
            data = [item for item in self.countryArr if item.lower().startswith(value)]

        # update dropdown list
        self.countryDropdown['values'] = data

        # open dropdown if matches exist
        if data:
            self.countryDropdown.event_generate('<Down>')

