from tkinter.ttk import Button
import json


# Reset Button
class ResetButton(Button):
    def __init__(self, parent, resetFields, row=0, column=0):
        super().__init__(parent, text="Reset", command=lambda: self.reset(resetFields))
        self.grid(row=row, column=column, padx=10)
    
    def reset(self, fields):

        for section in fields:
            section.clear()

        print(f"Resetting fields: {fields}\n")


# Submit Button
class SubmitButton(Button):
    def __init__(self, parent, submitFields, row=0, column=1):
        super().__init__(parent, text="Submit", command=lambda: self.submit(submitFields))
        self.grid(row=row, column=column, padx=10)

    
    def submit(self, fields):
        data = {}

        for section in fields:
            data.update(section.get_values())

        print(f"Submitting fields: {fields}\n")
        print(json.dumps(data, indent=2))

