from tkinter.ttk import Button
from Utils.validate_util import validate_values
import json


# Reset Button
class ResetButton(Button):
    def __init__(self, parent, resetFields, row=0, column=0):
        super().__init__(parent, text="Reset", command=lambda: self.reset(resetFields))         # needs anonymous func or it will auto-run
        self.grid(row=row, column=column, padx=10)
    
    def reset(self, fields):

        for section in fields:
            section.clear()

        print(f"Resetting fields: {fields}\n")


# Submit Button
class SubmitButton(Button):
    def __init__(self, parent, submitFields, row=0, column=1):
        super().__init__(parent, text="Submit", command=lambda: self.submit(submitFields))          # needs anonymous func or it will auto-run
        self.grid(row=row, column=column, padx=10)
        self.state(['disabled'])                                    # initiate it being disabled

    def submit(self, fields):
        data = {}

        for section in fields:
            values = section.get_values()               # extracts output of each component

            if validate_values(values=values, exceptions=["terms"]):
                data.update(section.get_values())
            else:
                print(f"Invalid section: {section.__class__.__name__}")
        

        print(f"Submitting fields: {fields}\n")
        print(json.dumps(data, indent=2))

