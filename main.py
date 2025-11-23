# Here we are fabricating Registration From Challenge Solution in TKinter

# Imports
from tkinter import Tk
from tkinter.ttk import Frame, Button
from Components.entry_comp import EntrySection
from Components.gender_comp import GenderSection
from Components.country_comp import CountrySection
from Components.terms_comp import TermSection
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
        self.genders = GenderSection(self.topLevel, "Gender", genderArr=genders, row=1)

        # Country
        self.country = CountrySection(self.topLevel, "Country", countryArr=getCountries(), row=2)

        # Subscription
        self.sub = TermSection(self.topLevel, termsArr=terms, row=3)


# Literals
genders = ("male", "female", "other")
terms = [
("Subscribe to newsletter", True),
("Subscribe to YouTube", False),
("Follow On Twitter", False)
]


# Main
def main():
    root = Tk()
    root.title("Registration Form")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    Form(root)
    root.mainloop()
main()

