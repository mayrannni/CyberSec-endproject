# Cybersecurity project 2024
## Contents
  1. Overview
  2. Project structure
  3. Installation
  4. Usage
  5. More about Scripts
     - PowerShell
     - GNU BASH
     - Python
  6. Examples
  7. System requirements
  8. Credits
  9. Contributing
  10. Notes

### 1. Overview
This project provides cybersecurity tools that perform some IT security tasks for specific purposes. With main script **main_menu.py**, script management becomes easier.  

Made with -------------------------------- 🚀✨  
<img src = "https://img.shields.io/badge/powershell-5391FE?style=for-the-badge&logo=powershell&logoColor=white"/>
<img src = "https://img.shields.io/badge/GNU%20Bash-4EAA25?style=for-the-badge&logo=GNU%20Bash&logoColor=white"/>
<img src = "https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>


### 2. Project Structure
/ CyberSec-endproject  
|  
| --- **main_menu.py** (main menu script in Python)  
| --- **options_menu_handler.py** (main menu handler)  
| --- **CyberSec_Tasks**/  
| --- | --- **PowerShell**/ (PowerShell scripts .psm1, 4 tasks)  
| --- | --- | --- **ps-reports**/  
| --- | --- **BASH**/ (BASH scripts .sh, 2 tasks)  
| --- | --- | --- **bash-reports**/  
| --- | --- **Python**/ (Python scripts .py, 5 tasks)  
| --- | --- | --- **py_scripts_handler**/  
| --- | --- | --- **py-reports**/  
| --- **README.md** (markdown documentation file)  

### 3. Installation
1. Clone this repository  
   -> git clone https://github.com/mayrannni/CyberSec-endproject.git  
   -> cd CyberSec-endproject  
3. Preferably have PowerShell, BASH and Python installed. '''However, we consider problems depending on the different operating systems'''.

### 4. Usage
To launch the main menu with Python  
-> python main_menu.py  
The main menu allows you to select and run any of the cybersecurity scripts. Each script corresponds to specific security tasks such as scanning, security API's query or analyzing system information.
The menu consists of two scripts to take advantage of argparse. Just run main_menu.py and it will automatically play with the functionality of options_menu_handler.py.

### 5. More about scripts
#### PowerShell
  - **Hash-based API query**  
    *Request-ApiHashBased.ps1* requests a Virus Total API based on file hashes.
  - **Hidden files review**  
    *Show-HiddenFiles.ps1* displays a list of hidden files.
  - **Computer resources usage display**  
    *Get-PCInformation.ps1* checks detailed information about the use of computer resources.
  - **Information about last logins**  
    *Show-LogsLogin.ps1* checks if logins on a device were successful.
#### GNU Bash
  - **SSH Honeypot**  
    *ssh_honeypot.sh* uses netcat and netstat to listen for connections and filter them.
  - **Scanning ports and vulnerabilities**  
    *scanning.sh* uses nmap for port and vulnerability scanning. 
#### Python
  - **Scan vulnerabilities for websites**  
    *web_scanning.py* uses [ZAP](https://www.zaproxy.org/download/) and [ZAP API](https://pypi.org/project/zaproxy/) to scanning vulnerabilities from websites. 
  - **Check open ports - SHODAN**  
    *open_ports.py* uses Shodan API to scan an IP and returns the open ports of that IP. 
  - **Use IP Abuse Database**  
    *ip_inspector.py* uses IP Abuse Database API and checks how reliable and trusted is the given IP.
  - **Scanning IP addreses - NMAP**  
    *ip_scanning.py* uses nmap to scan the most common vulnerabilities for a given IP address.
  - **Reporting IP addresses**  
    *report_ip.py* uses IP Abuse Database API to report the compromised IP that nmap (based on *ip_scanning.py*) returns with vulnerabilities.

### 6. System requirements
This project is compatible with the following operating systems, also you will see warnings when using the menu if you try to run a script in a programming language that is unlikely to be present in your operating system.
- **Windows**   
  PowerShell: Make sure you have PowerShell 5.1 or later. PowerShell Core (7.x) is also supported.
  BASH (optional): If you use BASH scripts, you will need WSL (Windows Subsystem for Linux) or Git Bash.  
  Python: Python 3.x must be installed. Python can be downloaded from [python.org](https://www.python.org/downloads/).  
- **MacOS**  
  PowerShell (optional): You can install PowerShell Core on MacOS, follow the instructions [here](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-macos?view=powershell-7.4).  
  Bash: MacOS comes with Bash by default. If you want to use modern Bash features, make sure your version is 4.x or later (upgradeable with Homebrew).  
  Python: Python 3.x is required. Install Python via Homebrew using brew install python.  
- **Linux**  
  PowerShell (optional): PowerShell Core is compatible with Linux and can be installed by following the instructions [here](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-linux?view=powershell-7.4).  
  Bash: All Linux systems have Bash by default.  
  Python: Make sure you have Python 3.x installed. On most distributions you can install it using the package manager (sudo apt install python3 on Ubuntu/Debian or sudo yum install python3 on           CentOS/Fedora).  

### 7. Credits
[mayrannni](https://github.com/mayrannni) - Creator  
[Fermaroom](https://github.com/Fermaroom) - Creator  
[Edgar-A23](https://github.com/Edgar-A23) - Creator

### 8. Contributing
Feel free to submit issues or pull requests if you'd like to contribute to this project. Please be respectful and follow standard GitHub collaboration practices.

### 9. Notes
- **Security Considerations**: Do not use this tool on a network without permission. Ensure you have authorization to test any servers or services involved.
- **Legal Notice**: This tool is intended for educational purposes only. The authors (students) are not liable for any misuse.
- **Known Issues**: Occasionally, scripts may be delayed due to the execution of different processes such as scanning or searching for information in the system.
- **Troubleshooting**: If you encounter permission errors, try running the script with elevated privileges.

We hope your visit to our repository will be pleasant and helpful! Use it responsibly. o(*￣▽￣*)o
