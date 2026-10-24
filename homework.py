
import tkinter as tk
from tkinter import messagebox
from datetime import date

# Function to check in the participant
def check_in():
    name = name_entry.get().strip()

    if not name:
        messagebox.showwarning(
            "Missing Name",
            "Please enter your name before checking in."
        )
        return

    workshop_date = date.today().strftime("%B %d, %Y")

    welcome_message = (
        f"Welcome to the workshop, {name}!\n\n"
        f"We are happy to have you join us.\n"
        f"Workshop Date: {workshop_date}\n\n"
        "Enjoy your learning experience!"
    )

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, welcome_message)
    output_text.config(state="disabled")
root = tk.Tk()
root.title("Workshop Participant Greeting")
root.geometry("500x450")
root.resizable(False, False)
instructions_label = tk.Label(
    root,
    text="Workshop Participant Check-In\n"
         "Please enter your name below to receive your welcome message.",
    font=("Arial", 12),
    wraplength=450,
    justify="center"
)
instructions_label.pack(pady=20)
name_label = tk.Label(
    root,
    text="Participant Name:",
    font=("Arial", 11)
)
name_label.pack(pady=5)
name_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12)
)
name_entry.pack(pady=5)
name_entry.focus()
check_in_button = tk.Button(
    root,
    text="Check In",
    font=("Arial", 11, "bold"),
    command=check_in
)
check_in_button.pack(pady=15)
output_text = tk.Text(
    root,
    height=7,
    width=48,
    font=("Arial", 11),
    wrap="word",
    state="disabled"
)
output_text.pack(pady=10)
root.mainloop()