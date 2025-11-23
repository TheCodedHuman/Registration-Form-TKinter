# Here we are fabricating Registration From Challenge Solution in TKinter

# Imports
from tkinter import Tk
from tkinter import ttk
from Utils.entry_util import EntrySection
from Utils.gender_util import GenderSection

# Classed
class Form:
    def __init__(self, root):

        # frame consisting all frames
        self.topLevel = ttk.Frame(root, padding=15)
        self.topLevel.grid(row=0, sticky="news")
        self.topLevel.columnconfigure(0, weight=1)

        # Entries
        self.entries = EntrySection(self.topLevel, row=0)

        # Genders
        self.genders = GenderSection(self.topLevel, "Gender", ("male", "female", "other"), row=1)

# Main
def main():
    root = Tk()
    root.title("Registration Form")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    Form(root)
    root.mainloop()
main()

