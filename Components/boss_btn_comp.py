from tkinter.ttk import Button

# Reset Button
class ResetButton(Button):
    def __init__(self, parent, resetFields, row=0, column=0):
        super().__init__(parent, text="Reset", command=self.reset(resetFields))
        self.grid(row=row, column=column, padx=10)

    
    def reset(self, fields):
        print("Resetting fields:", fields)


# Submit Button
class SubmitButton(Button):
    def __init__(self, parent, submitFields, row=0, column=1):
        super().__init__(parent, text="Submit", command=self.submit(submitFields))
        self.grid(row=row, column=column, padx=10)

    
    def submit(self, fields):
        print("Submitting fields:", fields)