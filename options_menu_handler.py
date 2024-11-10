"""Manage main menu"""

import argparse
import hashlib
import datetime
import os
import subprocess
import sys
import time
from main_menu import main


def path():
    """Find the path where the script is located"""
    main_path = os.path.dirname(os.path.abspath(__file__))
    return main_path


def scripts_execution_info(root_path, filename):
    """Show hash and datetime"""
    # execution date
    get_date = datetime.datetime.now()
    date = get_date.strftime("%d-%m-%Y %H:%M:%S.%f")
    print("Script successfully completed its task at: %s" % date)
    # file hash
    path = root_path + filename
    try:
        file_ob = open(path, "rb")
    except Exception:
        print("File Not Found.")
    else:
        # hash value from file
        file_to_hash = file_ob.read()
        hash_info = hashlib.sha512(file_to_hash)
        hash_value = hash_info.hexdigest()
        print(
            "File HASH is: %s \n" % hash_value,
            "Generated report PATH by script is: %s" % path,
        )


def input_help_validator(help_command):
    """Validate help command"""
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        try:
            get_help = input(
                "You want to see the script help first? (Recommended): y/n >> "
            )
            show_help = get_help.strip().lower()
            if show_help == "y":
                print("SHOWING HELP ========== :)")
                time.sleep(3)
                try:
                    subprocess.run(help_command, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Sorry, error when showing help. (Error: {e}) ")
                break
            elif show_help == "n":
                print("Continuing without showing help...")
                time.sleep(3)
                break
            else:
                raise ValueError("Unable to process your input.")
        except ValueError as e:
            attempts += 1
            print(f"{e}. {max_attempts - attempts} attemp(s) remaining.")

    if attempts == max_attempts:
        print("Too many incorrect attempts.")
        print("Continuing without displaying help.")
        time.sleep(3)


mode = """
Run the next command:
python "/the/file/path/options_menu_handler.py" -menu_option "1" -submenu_option "3" """

parser = argparse.ArgumentParser(
    description="", epilog=mode, formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument(
    "-menu_option",
    dest="menu_option",
    help="Option to be selected from the main menu.",
    required=True,
    type=str,
)
parser.add_argument(
    "-submenu_option", dest="submenu_option", help="Option to be selected from the main menu.", type=str
)
param = parser.parse_args()

os = sys.platform
if os == "win32":
    if param.menu_option == "1":
        if param.submenu_option == "1":
            filename = r"\PowerShell\Get-PcInformation.psm1"
            main_path = path()
            secondary_path = main + filename
            if os.path.exists(sec):
                help_command = ["PowerShell", sec, "--help"]
                input_help_validator(help_command)
                print("")
                print("\n----------------------------------------- \n")
                subprocess.run(
                    ["Powershell", "-ExecutionPolicy", "Bypass", sec]
                )  # Comentario de que hace
                name = r"\PowerShell\ps-reports\Get-PCInformation.html"
                scripts_execution_info(main_path, name)
            else:
                print("File does not exist.")
                time.sleep(2)
        elif param.submenu_option == "2":
            filename = r"\PowerShell\Request-ApiHashBased.psm1"
            main_path = path()
            secondary_path = main_path + filename
            if os.path.exists(sec):
                help_command = ["PowerShell", sec, "--help"]
                input_help_validator(help_command)
                print("\n----------------------------------------- \n")
                subprocess.run(["Powershell", "-ExecutionPolicy", "Bypass", sec])
                name = r"\PowerShell\ps-reports\Request-ApiHashBased.log"
                scripts_execution_info(main_path, name)
            else:
                print("File does not exist.")
                time.sleep(2)
        elif param.submenu_option == "3":
            filename = r"\PowerShell\Show-HiddenFiles.psm1"
            main_path = path()
            secondary_path = main_path + filename
            if os.path.exists(sec):
                help_command = ["PowerShell", sec, "--help"]
                input_help_validator(help_command)
                print("\n----------------------------------------- \n")
                subprocess.run(["Powershell", "-ExecutionPolicy", "Bypass", sec])
                name = r"\PowerShell\ps-reports\Show-HiddenFiles.txt"
                scripts_execution_info(main_path, name)
            else:
                print("File does not exist.")
                time.sleep(2)
        elif param.submenu_option == "4":
            filename = r"\PowerShell\Show-LogsLogin.psm1"
            main_path = path()
            secondary_path = main_path + filename
            if os.path.exists(sec):
                help_command = ["PowerShell", sec, "--help"]
                input_help_validator(help_command)
                print("\n----------------------------------------- \n")
                subprocess.run(["Powershell", "-ExecutionPolicy", "Bypass", sec])
                name = r"\PowerShell\ps-reports\Show-LogsLogin.txt"
                scripts_execution_info(main_path, name)
            else:
                print("File does not exist.")
                time.sleep(2)
        else:
            print("Opciob no valida")
    elif param.menu_option == "2":
        print("You cannot run this option as your operating system is Windows.")
        print("Redirigiendo al menu  pricipal... \n")
        time.sleep(2)
    elif param.menu_option == "3":
        filename = r"/Python/main_menu.py"
        main_path = path()
        secondary_path = main_path + filename
        if os.path.exists(sec):
            # mandar a llamar al script ya definido de python
            subprocess.run("python", sec, capture_output=True, text=True)
        else:
            print("File does not exist.")
elif os == "linux":
    if param.menu_option == "1":
        print("You cannot run this option,", "as your OS is Linux.")
        print("Redirecting to main menu...\n")
    elif param.menu_option == "2":
        if param.submenu_option == "1":
            filename = r"/Bash/scanning.sh"
            main_path = path()
            secondary_path = main_path + filename
            if os.path.exists(sec):
                subprocess.run(
                    ["Bash", sec],
                    capture_output=True,
                    text=True,
                    shell=True,
                    executable="/bin/bash",
                )
                name = r"/Bash/bash-reports/scanning.txt"
                scripts_execution_info(main_path, name)
        elif param.submenu_option == "2":
            filename = r"/Bash/ssh_honeypot.sh"
            main_path = path()
            secondary_path = main_path + filename
            if os.path.exists(sec):
                subprocess.run(
                    ["Bash", sec],
                    capture_output=True,
                    text=True,
                    shell=True,
                    executable="/bin/bash",
                )
                name = r"/Bash/bash-reports/ssh_honeypot.txt"
                scripts_execution_info(main_path, name)
        elif param.submenu_option == "0":
            print("Back to main menu, bye!")
            time.sleep(2)
        else:
            print("Option is not within the established parameters.")
    elif param.menu_option == "3":
        filename = r"/Python/main_menu.py"
        main_path = path()
        secondary_path = main_path + filename
        if os.path.exists(sec):
            # mandar a llamar al script ya definido de python
            subprocess.run("python", "main_menu.py", capture_output=True, text=True)
        else:
            print("File does not exist.")
elif os == "darwin":
    if param.menu_option == "1":
        print("You cannot run this option,", "as your OS is Linux.")
        print("Redirecting to main menu...\n")
    elif param.menu_option == "2":
        if param.submenu_option == "1":
            filename = r"/Bash/scanning.sh"
            main_path = path()
            secondary_path = main_path + filename
            if os.path.exists(sec):
                subprocess.run(
                    ["Bash", sec],
                    capture_output=True,
                    text=True,
                    shell=True,
                    executable="/bin/bash",
                )
                name = r"/Bash/bash-reports/scanning.txt"
                scripts_execution_info(main_path, name)
        elif param.submenu_option == "2":
            filename = r"/Bash/ssh_honeypot.sh"
            main_path = path()
            secondary_path = main_path + filename
            if os.path.exists(sec):
                subprocess.run(
                    ["Bash", sec],
                    capture_output=True,
                    text=True,
                    shell=True,
                    executable="/bin/bash",
                )
                name = r"/Bash/bash-reports/ssh_honeypot.txt"
                scripts_execution_info(main_path, name)
        elif param.submenu_option == "0":
            print("Back to main menu, bye!")
            time.sleep(2)
        else:
            print("Option is not within the established parameters.")
    elif param.menu_option == "3":
        filename = r"/Python/main_menu.py"
        main_path = path()
        secondary_path = main_path + filename
        if os.path.exists(sec):
            subprocess.run("python", "main_menu.py", capture_output=True, text=True)
        else:
            print("File does not exist.")
else:
    print("No operating system (OS) recognised...")

main()  # call function
