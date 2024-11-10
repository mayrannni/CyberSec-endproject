"""Manage CyberSec-endproject"""

import subprocess
import time
import os


def main():
    """Show menu options"""
    print(
        "CyberSecurity scripts were developed in the following programming languages,",
        "select one of them to be able to display a submenu of the tasks.",
    )
    print("1. PowerShell")
    print("2. BASH")
    print("3. Python")
    print("Enter 0 to exit.")


def powershell():
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


def bash():
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
    opP = None
    while opP != "0":
        main()
        opP = input("Desired option: ")
        if opP == """1""":
            while True:
                powershell()
                opS = input(">> Enter your choice ")
                if opS == "1":
                    subprocess.run(["python", finalpath, "-opP", opP, "-opS", opS])
                elif opS == "2":
                    subprocess.run(["python", finalpath, "-opP", opP, "-opS", opS])
                elif opS == "3":
                    subprocess.run(["python", finalpath, "-opP", opP, "-opS", opS])
                elif opS == "4":
                    subprocess.run(["python", finalpath, "-opP", opP, "-opS", opS])
                elif opS == "0":
                    time.sleep(2)
                    break
                else:
                    print("Option is not within the established parameters.")
        elif opP == "2":
            bash()
            opS = input(">> Enter your choice ")
            if opS == "1":
                subprocess.run(["python", finalpath, "-opP", opP, "-opS", opS])
            elif opS == "2":
                subprocess.run(["python", finalpath, "-opP", opP, "-opS", opS])
            elif opS == "0":
                time.sleep(2)
                break
        elif opP == "3":
            subprocess.run(["python", finalpath, "-opP", opP])
        elif opP == "0":
            print("ByeBye!")
            exit
        else:
            print("Option is not within the established parameters.")


if __name__ == "__main__":
    main()
