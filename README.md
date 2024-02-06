@@ -0,0 +1,12 @@
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
if __name__ == "__main__":
    root = tk.Tk()
    calculator_app = CalculatorApp(root)
    root.mainloop()


