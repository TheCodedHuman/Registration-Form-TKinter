# Here we are fabricating Registration From Challenge Solution in TKinter

# Imports
from tkinter import Tk
from tkinter.ttk import Frame
from Components.entry_comp import EntrySection
from Components.gender_comp import GenderSection
from Components.country_comp import CountrySection
from Utils.country_util import getCountries

# Classed
class Form:
    def __init__(self, root):

        # frame consisting all frames
        self.topLevel = Frame(root, padding=15)
        self.topLevel.grid(row=0, sticky="news")
        self.topLevel.columnconfigure(0, weight=1)

        # Entries
        self.entries = EntrySection(self.topLevel, row=0)

        # Genders
        self.genders = GenderSection(self.topLevel, "Gender", ("male", "female", "other"), row=1)

        # Country
        self.country = CountrySection(self.topLevel, "Country", countryArr=getCountries(), row=2)


# Main
def main():
    root = Tk()
    root.title("Registration Form")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    Form(root)
    root.mainloop()
main()

