import tkinter as tk
from tkinter import *

# GUI design
root = Tk()
root.title("SecureShellGen: Secure Reverse Shell Payload Generator")
root.resizable(False, False)
root.geometry("700x500+500+200")
root.configure(bg="black")

# Icon
icon = PhotoImage(file="logo.png")
root.iconphoto(True, icon)

# Logo
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="black").place(x=175, y=7)
Label(root, text="SecureShellGen", bd=3, bg="black", fg="red", font="arial 30 bold").place(x=270, y=20)

# Password label
lhost_label = tk.Label(root, text="IP:", bd=5, fg="white", bg="black", font="arial 12 bold")
lhost_label.place(x=90, y=140)

lport_label = tk.Label(root, text="PORT:", bd=5, fg="white", bg="black", font="arial 12 bold")
lport_label.place(x=350, y=140)

# Text box
lhost_entry = tk.Entry(root, show="", bd=5, fg="black", bg="white", font="arial 12 bold")
lhost_entry.place(x=130, y=140)

lport_entry = tk.Entry(root, show="", bd=5, fg="black", bg="white", font="arial 12 bold")
lport_entry.place(x=420, y=140)

generate_button = tk.Button(root, text="Generate Payload", font="arial 10 bold", command=lambda: generate_reverse_shell_payload())
generate_button.place(x=280, y=250)

# Result label
result_label = tk.Label(root, text="", bd=5, font="arial 13 bold")
result_label.place(x=180, y=330)


# Create and position the payload selection dropdown
payload_options = [

    "Click to Select Payload: ",
    "Windows Meterpreter Staged Reverse TCP(x64)",
    "Windows Meterpreter Stageless Reverse TCP(x64)",
    "Windows Staged Reverse TCP(x64)",
    "Windows Stageless Reverse TCP(x64)",
    "Linux Meterpreter Staged Reverse TCP(x64)",
    "Linux Stageless Reverse TCP(x64)",
    "Windows Bind TCP ShellCode",
    "PHP Meterpreter Stageless Reverse TCP",
    "PHP Reverse PHP",
    "Bash Stageless Reverse TCP",
]
payload_var = tk.StringVar(root)
payload_var.set(payload_options[0])  # Set default value
payload_dropdown = tk.OptionMenu(root, payload_var, *payload_options)
payload_dropdown.configure(font="arial 10 bold")
payload_dropdown.pack()
payload_dropdown.place(x=250, y=200)


def generate_reverse_shell_payload():
    lhost = lhost_entry.get()
    lport = lport_entry.get()
    selected_payload = payload_var.get()

    # Generate the payload based on user inputs
    payload = generate_reverse_shell_payload(lhost, lport, selected_payload)

    # Update the output label with the generated payload
    result_label.configure(text=payload)


# Start the Tkinter event loop
root.mainloop()
