# Here we are fabricating Registration From Challenge Solution in TKinter

# Imports
from tkinter import Tk
from tkinter.ttk import Frame
from functools import partial
from Components.entry_comp import EntrySection
from Components.gender_comp import GenderSection
from Components.country_comp import CountrySection
from Components.terms_comp import TermSection
from Components.boss_btn_comp import ResetButton, SubmitButton
from Utils.country_util import getCountries
from Utils.validate_util import validate_values



# Classed
class Form:
    def __init__(self, root):

        # frame consisting all frames
        self.topLevel = Frame(root, padding=15)
        self.topLevel.grid(row=0, sticky="news")
        self.topLevel.columnconfigure(0, weight=1)

        # Sections
        self.entries = EntrySection(self.topLevel, row=0)                                               # Entries
        self.genders = GenderSection(self.topLevel, "Gender", genderArr=genders, row=1)                 # Genders
        self.country = CountrySection(self.topLevel, "Country", countryArr=getCountries(), row=2)       # Country
        self.terms = TermSection(self.topLevel, termsArr=terms, row=3)                                  # Subscription

        # Sections-List
        self.sections = [self.entries, self.genders, self.country, self.terms]

        # Boss-Button-Frame
        self.BossFrame = Frame(self.topLevel, padding=(30, 15))
        self.BossFrame.grid(row=4, column=0, sticky="we")

            # Reset-Button
        ResetButton(self.BossFrame, resetFields=self.sections)                     # within BossFrame

            # Submit-Button
        self.submitBtn = SubmitButton(self.BossFrame, submitFields=self.sections)  # within BossFrame



        # Entries
        for entry in [self.entries.nameField.entryField,
                    self.entries.emailField.entryField,
                    self.entries.pwField.entryField]:
            entry.bind("<KeyRelease>", partial(self.is_form_valid))

        # Gender
        self.genders.genderVar.trace_add("write", lambda *args: self.is_form_valid())

        # Country
        self.country.countryVar.trace_add("write", lambda *args: self.is_form_valid())

        # Terms (checkboxes)
        for cb in self.terms.checkButtons:
            cb.config(command=self.is_form_valid)


    def is_form_valid(self, *args) -> None:         # args nullify extra stuff like events or more
        """
        Checks all sections with validate_values()
        Disable submitBtn: if any required field is emmtpy
        Enables it only when all required fields are valid
        """
        for section in self.sections:
            values = section.get_values()

            if not validate_values(values, exceptions=["terms"]):
                self.submitBtn.state(["disabled"])
                return

        self.submitBtn.state(["!disabled"])
        

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



