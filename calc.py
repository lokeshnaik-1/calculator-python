import tkinter as tk
import math

# Calculator state
current_expression = ""

def add_to_expression(value):
    """Append a value (number/operator) to the expression."""
    global current_expression
    current_expression += str(value)
    display_text.set(current_expression)

def clear_expression():
    """Reset the expression and clear display."""
    global current_expression
    current_expression = ""
    display_text.set("")

def calculate_result():
    """Evaluate the current mathematical expression."""
    global current_expression
    try:
        result = str(eval(current_expression))
        display_text.set(result)
        current_expression = result
    except Exception:
        display_text.set("Error")
        current_expression = ""

def remove_last_char():
    """Delete the last character from expression."""
    global current_expression
    current_expression = current_expression[:-1]
    display_text.set(current_expression)

def toggle_sign():
    """Toggle the sign of the current expression."""
    global current_expression
    if current_expression:
        if current_expression.startswith("-"):
            current_expression = current_expression[1:]
        else:
            current_expression = "-" + current_expression
        display_text.set(current_expression)

# Scientific functions
def calc_sqrt():
    global current_expression
    try:
        current_expression = str(math.sqrt(float(current_expression)))
        display_text.set(current_expression)
    except Exception:
        display_text.set("Error")
        current_expression = ""

def calc_square():
    global current_expression
    try:
        current_expression = str(float(current_expression) ** 2)
        display_text.set(current_expression)
    except Exception:
        display_text.set("Error")
        current_expression = ""

def calc_cube():
    global current_expression
    try:
        current_expression = str(float(current_expression) ** 3)
        display_text.set(current_expression)
    except Exception:
        display_text.set("Error")
        current_expression = ""

def calc_reciprocal():
    global current_expression
    try:
        current_expression = str(1 / float(current_expression))
        display_text.set(current_expression)
    except Exception:
        display_text.set("Error")
        current_expression = ""

def calc_sin():
    global current_expression
    try:
        current_expression = str(math.sin(math.radians(float(current_expression))))
        display_text.set(current_expression)
    except Exception:
        display_text.set("Error")
        current_expression = ""

def calc_cos():
    global current_expression
    try:
        current_expression = str(math.cos(math.radians(float(current_expression))))
        display_text.set(current_expression)
    except Exception:
        display_text.set("Error")
        current_expression = ""

def calc_tan():
    global current_expression
    try:
        current_expression = str(math.tan(math.radians(float(current_expression))))
        display_text.set(current_expression)
    except Exception:
        display_text.set("Error")
        current_expression = ""

def calc_log():
    global current_expression
    try:
        current_expression = str(math.log10(float(current_expression)))
        display_text.set(current_expression)
    except Exception:
        display_text.set("Error")
        current_expression = ""

def calc_ln():
    global current_expression
    try:
        current_expression = str(math.log(float(current_expression)))
        display_text.set(current_expression)
    except Exception:
        display_text.set("Error")
        current_expression = ""

# Initialize main window
root = tk.Tk()
root.title("Phone Calculator")
root.geometry("380x750")
root.configure(bg="#000000")

display_text = tk.StringVar()

# Display entry widget
display = tk.Entry(
    root,
    textvariable=display_text,
    font=("Arial", 32),
    bg="#000000",
    fg="white",
    bd=0,
    justify="right"
)
display.pack(fill="both", pady=(30, 10), ipady=25)

button_frame = tk.Frame(root, bg="#000000")
button_frame.pack(fill="both", expand=True)

# Button creation helper
def create_button(text, bg, fg, row, col, command, colspan=1):
    btn = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 20),
        bg=bg,
        fg=fg,
        activebackground=bg,
        bd=0,
        relief="flat",
        command=command
    )
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=6, pady=6)

# Color scheme
number_bg = "#333333"
number_fg = "white"
operator_bg = "#ff9f0a"
function_bg = "#a5a5a5"
function_fg = "black"

# Scientific buttons
create_button("√", function_bg, function_fg, 0, 0, calc_sqrt)
create_button("x²", function_bg, function_fg, 0, 1, calc_square)
create_button("x³", function_bg, function_fg, 0, 2, calc_cube)
create_button("1/x", function_bg, function_fg, 0, 3, calc_reciprocal)

create_button("sin", function_bg, function_fg, 1, 0, calc_sin)
create_button("cos", function_bg, function_fg, 1, 1, calc_cos)
create_button("tan", function_bg, function_fg, 1, 2, calc_tan)
create_button("log", function_bg, function_fg, 1, 3, calc_log)

create_button("ln", function_bg, function_fg, 2, 0, calc_ln)
create_button("(", function_bg, function_fg, 2, 1, lambda: add_to_expression("("))
create_button(")", function_bg, function_fg, 2, 2, lambda: add_to_expression(")"))
create_button("⌫", function_bg, function_fg, 2, 3, remove_last_char)

# Normal calculator buttons
create_button("C", function_bg, function_fg, 3, 0, clear_expression)
create_button("π", function_bg, function_fg, 3, 1, lambda: add_to_expression(str(math.pi)))
create_button("e", function_bg, function_fg, 3, 2, lambda: add_to_expression(str(math.e)))
create_button("/", operator_bg, "white", 3, 3, lambda: add_to_expression("/"))

create_button("7", number_bg, number_fg, 4, 0, lambda: add_to_expression("7"))
create_button("8", number_bg, number_fg, 4, 1, lambda: add_to_expression("8"))
create_button("9", number_bg, number_fg, 4, 2, lambda: add_to_expression("9"))
create_button("*", operator_bg, "white", 4, 3, lambda: add_to_expression("*"))

create_button("4", number_bg, number_fg, 5, 0, lambda: add_to_expression("4"))
create_button("5", number_bg, number_fg, 5, 1, lambda: add_to_expression("5"))
create_button("6", number_bg, number_fg, 5, 2, lambda: add_to_expression("6"))
create_button("-", operator_bg, "white", 5, 3, lambda: add_to_expression("-"))

create_button("1", number_bg, number_fg, 6, 0, lambda: add_to_expression("1"))
create_button("2", number_bg, number_fg, 6, 1, lambda: add_to_expression("2"))
create_button("3", number_bg, number_fg, 6, 2, lambda: add_to_expression("3"))
create_button("+", operator_bg, "white", 6, 3, lambda: add_to_expression("+"))

create_button("+/-", number_bg, number_fg, 7, 0, toggle_sign)
create_button("0", number_bg, number_fg, 7, 1, lambda: add_to_expression("0"))
create_button(".", number_bg, number_fg, 7, 2, lambda: add_to_expression("."))
create_button("=", operator_bg, "white", 7, 3, calculate_result)

# Make grid cells expandable
for i in range(8):
    button_frame.rowconfigure(i, weight=1)
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

root.mainloop()
