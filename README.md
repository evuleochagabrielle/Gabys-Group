    except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator_app = CalculatorApp(root)
    root.mainloop()


