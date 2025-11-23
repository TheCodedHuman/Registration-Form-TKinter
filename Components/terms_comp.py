from tkinter import BooleanVar
from tkinter.ttk import Frame, Checkbutton

class TermSection:
    def __init__(self, parent, termsArr, row=3, column=0):
        self.termFrame = Frame(parent, padding=(0, 5))
        self.termFrame.grid(row=row, column=column, sticky="w")
        self.termFrame.columnconfigure(0, weight=1)

        # term-variables containing flags for chosen terms
        self.termVars = []

        # scalable terms and conditions
        for row, (label, flag) in enumerate(termsArr):
            var = BooleanVar(value=flag)

            check_btn = Checkbutton(self.termFrame, 
                                    text=label, 
                                    variable=var)
            check_btn.grid(row=row, column=0, sticky="we")

            self.termVars.append((label, var))

    # getter
    def get_values(self): 
        return {
            "terms": {
                label: flag.get() for label, flag in self.termVars
            }
        }

    # clear/reset
    def clear(self):
        for (_, flag) in self.termVars:
            flag.set(False)

