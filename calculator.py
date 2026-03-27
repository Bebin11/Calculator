"""
Simple Calculator UI
Run: python calculator.py
"""

import tkinter as tk

# --- Create window ---
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# --- Display ---
display = tk.Entry(root, font=("Arial", 24), justify="right", bd=5, relief="sunken")
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
display.insert(0, "0")

# --- Calculator state ---
calculator_state = {
    "display": "0",
    "previous_value": None,
    "operation": None,
    "new_number": True,
}


def update_display(text):
    """Update the display with new text."""
    display.delete(0, tk.END)
    display.insert(0, text)
    calculator_state["display"] = text


def on_button_click(text):
    """Called when any button is clicked."""
    state = calculator_state
    current_display = state["display"]
    
    # Handle number buttons
    if text.isdigit() or text == ".":
        if state["new_number"] and text != ".":
            update_display(text)
            state["new_number"] = False
        elif text == "." and "." not in current_display:
            update_display(current_display + text)
            state["new_number"] = False
        elif text != ".":
            update_display(current_display + text)
            state["new_number"] = False
    
    # Handle operator buttons (+, -, and *)
    elif text in ["+", "-", "*"]:
        current_value = float(current_display)
        
        # If there's a pending operation, calculate it first
        if state["operation"] and not state["new_number"]:
            result = calculate(state["previous_value"], current_value, state["operation"])
            update_display(str(result))
            state["previous_value"] = result
        else:
            state["previous_value"] = current_value
        
        state["operation"] = text
        state["new_number"] = True
    
    # Handle +/- button
    elif text == "+/-":
        current_value = float(current_display)
        update_display(str(-current_value))
        state["new_number"] = True


def on_clear():
    """Called when C is pressed."""
    calculator_state["display"] = "0"
    calculator_state["previous_value"] = None
    calculator_state["operation"] = None
    calculator_state["new_number"] = True
    update_display("0")


def on_backspace():
    """Called when backspace is pressed."""
    current_display = calculator_state["display"]
    if len(current_display) > 1:
        update_display(current_display[:-1])
    else:
        update_display("0")
        calculator_state["new_number"] = True


def calculate(previous, current, operation):
    """Perform the calculation based on the operation."""
    if operation == "+":
        return previous + current
    elif operation == "-":
        return previous - current
    elif operation == "*":
        return previous * current
    return current


def on_equals():
    """Called when = is pressed."""
    state = calculator_state
    
    if state["operation"] and state["previous_value"] is not None:
        current_value = float(state["display"])
        result = calculate(state["previous_value"], current_value, state["operation"])
        update_display(str(result))
        state["previous_value"] = None
        state["operation"] = None
        state["new_number"] = True


# --- Button layout ---
buttons = [
    ["C", "⌫"],
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["+/-", "0", "."],
    ["-", "+", "*", "="],
]

for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        if text == "C":
            cmd = on_clear
        elif text == "⌫":
            cmd = on_backspace
        elif text == "=":
            cmd = on_equals
        else:
            cmd = lambda t=text: on_button_click(t)

        btn = tk.Button(
            root, text=text, font=("Arial", 16),
            width=4, height=2, command=cmd
        )
        btn.grid(row=r+1, column=c, padx=2, pady=2, sticky="nsew")

# --- Make buttons expand evenly ---
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

# --- Run ---
root.mainloop()