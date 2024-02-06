import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg="white")

        # Entry widget to display the calculation
        self.entry = tk.Entry(root, width=20, font=('comic sans', 16), bd=10, insertwidth=4, bg="black",fg ="blue",
                              justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

# Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, width=5, height=2, font=('comic sans', 16), bd=5, bg="black",fg= "sky blue",
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
    def on_button_click(self, text):
        current_text = self.entry.get()

        if text == 'C':
            self.entry.delete(0, tk.END)
        elif text == '=':
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
