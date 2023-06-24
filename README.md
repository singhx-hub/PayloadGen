# PayloadGen: Dynamic Reverse Shell Payload Creator

PayloadGen is a graphical user interface (GUI) tool that helps you generate dynamic reverse shell payloads. It utilizes the MSFVenom tool from Metasploit Framework to create payloads for various operating systems and architectures.

## Features

- Generate reverse shell payloads for Windows and Linux.
- Support for staged and stageless payloads.
- Choose from a variety of pre-defined payloads.
- Copy generated payload to the clipboard for easy use.

## Requirements

- Python 3.x
- Tkinter library
- Metasploit Framework (MSFVenom)

## Installation

1. Clone the repository:

         git clone https://github.com/singhx-hub/PayloadGen.git

2. Install the required dependencies:

         pip install -r requirements.txt

## Usage

1. Run the application:

         python3 payloadgen.py

 Enter the IP address (LHOST) and port number (LPORT) for the reverse shell payload.

3. Select the desired MSFVenom payload from the dropdown menu.

4. Click the "Generate Payload" button to generate the payload command.

5. The generated payload command will be displayed in the text box. You can copy it to the clipboard by clicking the "Copy" button.

   ![image](https://github.com/singhx-hub/PayloadGen/assets/126919241/10726836-e5d5-44d0-a1e7-e334a7f2e9c3)


## License

This project is licensed under the [MIT License](LICENSE).
