import tkinter as tk

root = tk.Tk()
root.title("Pink Calculator")
root.geometry("350x480")
root.configure(bg="#F8DCE8")
root.resizable(False, False)

# Calculator display
expression = ""

display = tk.Entry(
root,
font=("Arial", 25),
bg="#FFF5F9",
fg="#8E315C",
justify="right",
bd=0
)
display.pack(padx=20, pady=25, ipady=20, fill="x")


# Button functions
def click(value):
    global expression

    if value == "C":
       expression = ""

    elif value == "⌫":
        expression = expression[:-1]

    elif value == "=":
       try:
         result = eval(expression, {"__builtins__": {}})
         expression = str(result)
       except:
        expression = "Error"

    else:
      expression += value

    display.delete(0, tk.END)
    display.insert(0, expression)


buttons = [
["C", "⌫", "%", "/"],
["7", "8", "9", "*"],
["4", "5", "6", "-"],
["1", "2", "3", "+"],
["00", "0", ".", "="]
]

# Button colours
pink = "#E88BAF"
light_pink = "#FCEAF2"
dark_pink = "#B84D79"

# Create button layout
frame = tk.Frame(root, bg="#F8DCE8")
frame.pack(expand=True, fill="both", padx=15, pady=5)

for row, line in enumerate(buttons):
 for col, text in enumerate(line):

    color = pink if text in ["C", "⌫", "%", "/", "*", "-", "+", "="] else light_pink

    button = tk.Button(
       frame,
       text=text,
       font=("Arial", 17, "bold"),
       bg=color,
       fg=dark_pink,
       activebackground="#F4B6D0",
       bd=0,
       command=lambda t=text: click(t)
    )

    button.grid(
        row=row,
        column=col,
        padx=5,
        pady=5,
        sticky="nsew"
)


for i in range(4):
 frame.columnconfigure(i, weight=1)

for i in range(5):
 frame.rowconfigure(i, weight=1)

# Run calculator
root.mainloop()

