import tkinter as tk
from math import sqrt
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)

        self.expression = ""

        self.display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="ridge", justify='right')
        self.display.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=20)

        self.create_buttons()

    def add_to_expression(self, value):
        self.expression += str(value)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def calculate(self):
        try:
            # Secure eval environment
            allowed_names = {
                "sqrt": sqrt,
                "__builtins__": None,
            }
            result = eval(self.expression, {"__builtins__": None}, allowed_names)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear()

    def create_buttons(self):
        buttons = [
            ['7', '8', '9', '/', 'sqrt'],
            ['4', '5', '6', '*', '('],
            ['1', '2', '3', '-', ')'],
            ['0', '.', '%', '+', '**'],
            ['C', '=', '←', '', '']
        ]

        for row_index, row in enumerate(buttons):
            frame = tk.Frame(self.root)
            frame.pack(expand=True, fill="both")

            for col_index, btn_text in enumerate(row):
                if btn_text == '':
                    tk.Label(frame, text='').pack(side="left", expand=True, fill="both")
                    continue

                if btn_text == '←':
                    btn = tk.Button(frame, text='←', font=("Arial", 18), relief="ridge", borderwidth=1,
                                    command=self.backspace)
                elif btn_text == 'C':
                    btn = tk.Button(frame, text='C', font=("Arial", 18), relief="ridge", borderwidth=1,
                                    command=self.clear)
                elif btn_text == '=':
                    btn = tk.Button(frame, text='=', font=("Arial", 18), relief="ridge", borderwidth=1,
                                    command=self.calculate)
                elif btn_text == 'sqrt':
                    btn = tk.Button(frame, text='√', font=("Arial", 18), relief="ridge", borderwidth=1,
                                    command=lambda: self.add_to_expression('sqrt('))
                else:
                    btn = tk.Button(frame, text=btn_text, font=("Arial", 18), relief="ridge", borderwidth=1,
                                    command=lambda txt=btn_text: self.add_to_expression(txt))

                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

# Main
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
