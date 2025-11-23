# Here we are fabricating Registration From Challenge Solution in TKinter

# Imports
from tkinter import Tk
from tkinter.ttk import Frame
from Components.entry_comp import EntrySection
from Components.gender_comp import GenderSection
from Components.country_comp import CountrySection
from Components.terms_comp import TermSection
from Components.boss_btn_comp import ResetButton, SubmitButton
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
        self.terms = TermSection(self.topLevel, termsArr=terms, row=3)

        # Boss-Button-Frame
        self.BossFrame = Frame(self.topLevel, padding=(30, 15))
        self.BossFrame.grid(row=4, column=0, sticky="we")

        ResetButton(self.BossFrame, resetFields=(self.entries, self.genders, self.country, self.terms))             # Reset-Button within BossFrame
        SubmitButton(self.BossFrame, submitFields=(self.entries, self.genders, self.country, self.terms))           # Submit-Button within BossFrame


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

