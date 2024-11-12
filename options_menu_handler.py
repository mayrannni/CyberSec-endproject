#!/usr/bin/python3
"""Manage main menu."""

import argparse
import hashlib
import datetime
import os
import subprocess
import sys
import time
from main_menu import main


def path_finder():
    """Find the path where the script is located."""
    main_path = os.path.dirname(os.path.abspath(__file__))
    return main_path


def scripts_execution_info(file_path):
    """Show hash and datetime."""
    # execution date
    get_date = datetime.datetime.now()
    date = get_date.strftime("%d-%m-%Y %H:%M:%S.%f")
    print("Script successfully completed its task at: %s" % date)
    try:
        file_ob = open(file_path, "rb")
    except Exception:
        print("File Not Found.")
    else:
        # hash value from file
        file_to_hash = file_ob.read()
        hash_info = hashlib.sha512(file_to_hash)
        hash_value = hash_info.hexdigest()
        print(
            ">> File HASH is: %s\n>> Generated report PATH by script is: %s"
            % (hash_value, file_path)
        )
        file_ob.close()


def input_help_validator(help_command):
    """Validate help command."""
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
    "-submenu_option",
    dest="submenu_option",
    help="Option to be selected from the main menu.",
    type=str,
)
param = parser.parse_args()

operating_system = sys.platform #Check the operating system
if operating_system == "win32":
    if param.menu_option == "1":
        if param.submenu_option == "1":
            main_path = path_finder()
            module_path = os.path.join(
                "CyberSec_Tasks", "PowerShell", "Get-PCInformation.psm1"
            )
            abs_module_path = os.path.join(main_path, module_path)
            abs_module_path = os.path.abspath(abs_module_path)
            if os.path.exists(abs_module_path):
                # import powershell module
                import_command = f"Import-Module '{abs_module_path}'; Get-PCInformation"
                help_command = [
                    "PowerShell",
                    "-Command",
                    "Get-Help -Name Get-PCInformation -Full",
                ]
                input_help_validator(help_command)
                print(
                    "Hello ===================================================================="
                )
                print(
                    "Select the resources to be analysed, when the script is finished you will see the results in the report."
                )
                subprocess.run(["PowerShell", "-Command", import_command])
                report_path = os.path.join(
                    "CyberSec_Tasks",
                    "PowerShell",
                    "ps-reports",
                    "Get-PCInformation.html",
                )
                abs_report_path = os.path.join(main_path, report_path)
                abs_report_path = os.path.abspath(abs_report_path)
                scripts_execution_info(abs_report_path)
            else:
                print("File does not exist. Sorry.")
                time.sleep(1.5)
        elif param.submenu_option == "2":
            main_path = path_finder()
            module_path = os.path.join(
                "CyberSec_Tasks", "PowerShell", "Request-ApiHashBased.psm1"
            )
            abs_module_path = os.path.join(main_path, module_path)
            abs_module_path = os.path.abspath(abs_module_path)
            if os.path.exists(abs_module_path):
                import_command = (
                    f"Import-Module '{abs_module_path}'; Request-ApiHashBased"
                ) # import powershell module
                help_command = [
                    "PowerShell",
                    "-Command",
                    "Get-Help -Name Request-ApiHashBased -Full",
                ]
                input_help_validator(help_command)
                print(
                    "Hello ===================================================================="
                )
                subprocess.run(["PowerShell", "-Command", import_command])
                report_path = os.path.join(
                    "CyberSec_Tasks", "PowerShell", "ps-reports", "ReportVT.txt"
                )
                abs_report_path = os.path.join(main_path, report_path)
                abs_report_path = os.path.abspath(abs_report_path)
                scripts_execution_info(abs_report_path)
            else:
                print("File does not exist. Sorry.")
                time.sleep(1.5)
        elif param.submenu_option == "3":
            main_path = path_finder()
            module_path = os.path.join(
                "CyberSec_Tasks", "PowerShell", "Show-HiddenFiles.psm1"
            )
            abs_module_path = os.path.join(main_path, module_path)
            abs_module_path = os.path.abspath(abs_module_path)
            if os.path.exists(abs_module_path):
                import_command = (
                    f"Import-Module '{abs_module_path}'; Show-HiddenFiles"
                    ) # import powershell module
                help_command = [
                    "PowerShell",
                    "-Command",
                    "Get-Help -Name Show-HiddenFiles -Full",
                ]
                input_help_validator(help_command)
                print(
                    "Hello ===================================================================="
                )
                subprocess.run(["PowerShell", "-Command", import_command])
                report_path = os.path.join(
                    "CyberSec_Tasks", "PowerShell", "ps-reports", "Show-HiddenFiles.txt"
                )
                abs_report_path = os.path.join(main_path, report_path)
                abs_report_path = os.path.abspath(abs_report_path)
                scripts_execution_info(abs_report_path)
            else:
                print("File does not exist. Sorry.")
                time.sleep(1.5)
        elif param.submenu_option == "4":
            main_path = path_finder()
            module_path = os.path.join(
                "CyberSec_Tasks", "PowerShell", "Show-LogsLogin.psm1"
            )
            abs_module_path = os.path.join(main_path, module_path)
            abs_module_path = os.path.abspath(abs_module_path)
            if os.path.exists(abs_module_path):
                import_command = (
                    f"Import-Module '{abs_module_path}'; Show-LogsLogin"
                    ) # import powershell module
                help_command = [
                    "PowerShell",
                    "-Command",
                    "Get-Help -Name Show-LogsLogin -Full",
                ]
                input_help_validator(help_command)
                print(
                    "Hello ===================================================================="
                )
                subprocess.run(["PowerShell", "-Command", import_command])
                report_path = os.path.join(
                    "CyberSec_Tasks", "PowerShell", "ps-reports", "Show-LogsLogin.txt"
                )
                abs_report_path = os.path.join(main_path, report_path)
                abs_report_path = os.path.abspath(abs_report_path)
                scripts_execution_info(abs_report_path)
            else:
                print("File does not exist. Sorry.")
                time.sleep(1.5)
        else:
            print("Option is not within the established parameters.")
    elif param.menu_option == "2":
        print("You cannot run this option as your operating system is Windows.")
        print("Redirecting to main menu...")
        time.sleep(2)
    elif param.menu_option == "3":
        main_path = path_finder()
        py_handler_file = os.path.join(
            "CyberSec_Tasks", "Python", "py_scripts_handler.py"
        )
        abs_py_handler_file = os.path.join(main_path, py_handler_file)
        abs_py_handler_file = os.path.abspath(abs_py_handler_file)
        if os.path.exists(abs_py_handler_file):
            subprocess.run(["python", abs_py_handler_file])
        else:
            print("File does not exist. Sorry")
elif operating_system == "linux":
    if param.menu_option == "1":
        print("You cannot run this option,", "as your OS is Linux.")
        print("Redirecting to main menu...")
    elif param.menu_option == "2":
        if param.submenu_option == "1":
            filename = r"/Bash/scanning.sh"
            main_path = path_finder()
            secondary_path = main_path + filename
            if os.path.exists(secondary_path):
                help_command = ["Bash", secondary_path, "-h"]
                input_help_validator(help_command)
                print("\n----------------------------------------- \n")
                subprocess.run(
                    ["Bash", secondary_path],
                    capture_output=True,
                    text=True,
                    shell=True,
                    executable="/bin/bash",
                )
                name = r"/Bash/bash-reports/port_scan.txt"
                scripts_execution_info(main_path, name)
                name = r"/Bash/bash-reports/vulnerabilities_scan.txt"
                scripts_execution_info(main_path, name)
        elif param.submenu_option == "2":
            filename = r"/Bash/ssh_honeypot.sh"
            main_path = path_finder()
            secondary_path = main_path + filename
            if os.path.exists(secondary_path):
                help_command = ["Bash", secondary_path, "-h"]
                input_help_validator(help_command)
                print("\n----------------------------------------- \n")
                subprocess.run(
                    ["Bash", secondary_path],
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
        filename = r"/Python/py_scripts_handler.py"
        main_path = path_finder()
        secondary_path = main_path + filename
        print(secondary_path)
        if os.path.exists(secondary_path):
            subprocess.run("python", secondary_path, capture_output=True, text=True)
        else:
            print("File does not exist.")
elif operating_system == "darwin":
    if param.menu_option == "1":
        print("You cannot run this option,", "as your OS is Linux.")
        print("Redirecting to main menu...\n")
    elif param.menu_option == "2":
        if param.submenu_option == "1":
            filename = r"/Bash/scanning.sh"
            main_path = path_finder()
            secondary_path = main_path + filename
            if os.path.exists(secondary_path):
                help_command = ["Bash", secondary_path, "-h"]
                input_help_validator(help_command)
                print("\n----------------------------------------- \n")
                subprocess.run(
                    ["Bash", secondary_path],
                    capture_output=True,
                    text=True,
                    shell=True,
                    executable="/bin/bash",
                )
                name = r"/Bash/bash-reports/port_scan.txt"
                scripts_execution_info(main_path, name)
                name = r"/Bash/bash-reports/vulnerabilities_scan.txt"
                scripts_execution_info(main_path, name)
        elif param.submenu_option == "2":
            filename = r"/Bash/ssh_honeypot.sh"
            main_path = path_finder()
            secondary_path = main_path + filename
            if os.path.exists(secondary_path):
                help_command = ["Bash", secondary_path, "-h"]
                input_help_validator(help_command)
                print("\n----------------------------------------- \n")
                subprocess.run(
                    ["Bash", secondary_path],
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
        main_path = path_finder()
        secondary_path = main_path + filename
        if os.path.exists(secondary_path):
            subprocess.run("python", secondary_path, capture_output=True, text=True)
        else:
            print("File does not exist.")
else:
    print("No operating system (OS) recognised...")

main()  # call function
