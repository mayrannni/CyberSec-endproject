"""Manage CyberSec-endproject"""

import subprocess
import time
import os


def main_menu():
    """Show menu options"""
    print(
        "CyberSecurity scripts were developed in the following programming languages,",
        "select one of them to be able to display a submenu of the tasks.",
    )
    print("1. PowerShell")
    print("2. BASH")
    print("3. Python")
    print("Enter 0 to exit.")


def submenu_powershell():
    """Show PowerShell scripts options"""
    print(
        "Displaying options...",
        "Note! Options are scripts made with PowerShell"
        "Pick the one you want to see in action! :D",
    )
    print("1. Get-PCInformation")
    print("2. Request-ApiHashBased")
    print("3. Show-HiddenFiles")
    print("4. Show-LogsLogin")
    print("Enter 0 and return to main menu.")


def submenu_bash():
    """Show BASH scripts options"""
    print(
        "Displaying options...",
        "Note! Options are scripts made with BASH"
        "Pick the one you want to see in action! :D",
    )
    print("1. Scanning ports")
    print("2. SSH Honeypot")
    print("Enter 0 and return to main menu.")


def path():
    """Find the path where the script is located"""
    main_path = os.path.dirname(os.path.abspath(__file__))
    filename = "\options_menu_handler.py"
    finalpath = main_path + filename
    return finalpath


def main():
    """Use main and secondary options"""
    finalpath = path()
    menu_option = None
    while menu_option != "0":
        main_menu()
        menu_option = input("Desired option: ")
        if menu_option == """1""":
            while True:
                submenu_powershell()
                submenu_option = input(">> Enter your choice ")
                if submenu_option == "1":
                    subprocess.run(["python", finalpath, "-menu_option", menu_option, "-submenu_option", submenu_option])
                elif submenu_option == "2":
                    subprocess.run(["python", finalpath, "-menu_option", menu_option, "-submenu_option", submenu_option])
                elif submenu_option == "3":
                    subprocess.run(["python", finalpath, "-menu_option", menu_option, "-submenu_option", submenu_option])
                elif submenu_option == "4":
                    subprocess.run(["python", finalpath, "-menu_option", menu_option, "-submenu_option", submenu_option])
                elif submenu_option == "0":
                    time.sleep(2)
                    break
                else:
                    print("Option is not within the established parameters.")
        elif menu_option == "2":
            submenu_bash()
            submenu_option = input(">> Enter your choice ")
            if submenu_option == "1":
                subprocess.run(["python", finalpath, "-menu_option", menu_option, "-submenu_option", submenu_option])
            elif submenu_option == "2":
                subprocess.run(["python", finalpath, "-menu_option", menu_option, "-submenu_option", submenu_option])
            elif submenu_option == "0":
                time.sleep(2)
                break
        elif menu_option == "3":
            subprocess.run(["python", finalpath, "-menu_option", menu_option])
        elif menu_option == "0":
            print("ByeBye!")
            exit
        else:
            print("Option is not within the established parameters.")


if __name__ == "__main__":
    main()
