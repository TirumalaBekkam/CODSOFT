import tkinter as tk
from tkinter import messagebox

def perform_operation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation selected.")
            return

        label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

def clear_inputs():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    operation_var.set("+")
    label_result.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place widgets
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

label_operation = tk.Label(root, text="Select operation:")
label_operation.grid(row=2, column=0, padx=10, pady=10)

operation_var = tk.StringVar(value="+")
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1, padx=10, pady=10)

button_calculate = tk.Button(root, text="Calculate", command=perform_operation)
button_calculate.grid(row=3, column=0, padx=10, pady=10)

button_clear = tk.Button(root, text="Clear", command=clear_inputs)
button_clear.grid(row=3, column=1, padx=10, pady=10)

label_result = tk.Label(root, text="Result: ", font=("Arial", 12))
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()