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

# --- Button click handlers (TODO: add your logic here) ---

def on_button_click(text):
    """Called when any button is clicked. Add your logic here."""
    print(f"Button pressed: {text}")


def on_clear():
    """Called when C is pressed. Add clear logic here."""
    print("Clear pressed")


def on_equals():
    """Called when = is pressed. Add calculation logic here."""
    print("Equals pressed")


# --- Button layout ---
buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="],
]

for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        if text == "C":
            cmd = on_clear
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