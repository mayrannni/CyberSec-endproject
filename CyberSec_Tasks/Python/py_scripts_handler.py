"""Do the scripts management for the py_scripts_handler."""

import hashlib
import datetime
import os
import subprocess
import sys
import time
import re
from main_menu import main

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


def scripts_execution_info(root_path, filename):
    """Show hash and datetime."""
    # execution date
    get_date = datetime.datetime.now()
    date = get_date.strftime("%d-%m-%Y %H:%M:%S.%f")
    print("Script successfully completed its task at: %s" % date)
    # file hash
    path_file = root_path + filename
    try:
        file_ob = open(path_file, "rb")
    except Exception:
        print("File Not Found.")
    else:
        # hash value from file
        file_to_hash = file_ob.read()
        hash_info = hashlib.sha512(file_to_hash)
        hash_value = hash_info.hexdigest()
        print(
            "File HASH is: %s \n" % hash_value,
            "Generated report PATH by the script is: %s" % path,
        )


def path_finder():
    """Find the path where the script is located."""
    main_path = os.path.dirname(os.path.abspath(__file__))
    return main_path

def py_menu():
    """Show menu for managing scripts."""
    print("Cybersecurity Tasks in Python")
    print("1. Scan vulnerabilities for websites")
    print("2. Check open ports - SHODAN")
    print("3. Use IP Abuse Database")
    print("4. Scanning IP addresses - NMAP")
    print("5. Reporting IP addresses")
    print("6. Return to the main menu")

    choice = input("Select a cybersecurity function to start >> ")

    if choice == "1":
        help_command = ["python", "web_scanning.py", "--help"]
        input_help_validator(help_command)
        print("-----------------------------------------------------------")
        print("SCAN VULNERABILITIES FOR WEBSITES")

        # validating script option 1 parameters
        url_regex = re.compile(
            r"^(https?:\/\/)?"
            r"([a-zA-Z0-9.-]+)"
            r"(\.[a-zA-Z]{2,6})"
            r"(:[0-9]{1,5})?"
            r"(\/.*)?$"
        )
        apikey_regex = re.compile(r"^[a-zA-Z0-9]{20,40}$")

        while True:
            url_msg = "Enter the url to scan (e.g. 'https://example.com'): "
            apikey_msg = "API-KEY (e.g. 'jfacsqm6agh97lf49l923tch46'): "
            target_url = input(url_msg)
            zapikey = input(apikey_msg)
            if url_regex.match(target_url) and apikey_regex.match(zapikey):
                break
            else:
                print("Some parameters are inapplicable. Try again.")
                time.sleep(1)

        subprocess.run(
            ["python", "web_scanning.py", "-url", target_url, "-zapikey",
             zapikey]
        )  # run web scanning
        # Show the file-generated info
        main_path = path_finder()
        path_html_file = r"\py-reports\WebPentest.*html"
        pattern = re.compile(path_html_file)
        for root, dirs, files in os.walk(main_path):
            for file_name in files:
                if pattern.match(file_name):
                    name_file = f"\\{file}"
        print(f"The file name created is {name_file.replace('\\',"")}")
        name = "\\py-reports"
        name =+ name_file
        scripts_execution_info(main_path, name)

    elif choice == "2":
        help_command = ["python", "open_ports.py", "--help"]
        input_help_validator(help_command)
        print("-----------------------------------------------------------")
        print("VERIFY OPEN PORTS WITH SHODAN")

        ip = input("Enter the IP to scan (e.g. '8.8.8.8'): ")
        subprocess.run(["python", "open_ports.py", "-ip", ip])
        # Show the file-generated info
        main_path = path_finder()
        print("The file name created is Full_API_Response.txt")
        name = "\\Python\\py-reports\\Full_API_Response.txt"
        scripts_execution_info(main_path, name)

    elif choice == "3":
        help_command = ["python", "ip_inspector.py", "--help"]
        input_help_validator(help_command)
        print("-----------------------------------------------------------")
        print("INFORMATION FROM IP ABUSE DATABASE")

        ip_to_scan = input("Enter the IP to scan: ")
        day = input("Enter a day from 1 to 365: ")
        trust = input("Confidence limit from 25 to 100: ")
        ip_range = input("Interested IP range (e.g. /24): ")
        subprocess.run(
            [
                "python",
                "ip_inspector.py",
                "-ip",
                ip_to_scan,
                "-day",
                day,
                "-trust",
                trust,
                "-ip_range",
                ip_range,
            ]
        )
        # Show the file-generated info
        main_path = path_finder()
        print("The files name created is: \n"
              ">> check_ip_.txt",
              ">> black_list_.txt",
              ">> check_block_.txt")
        name1 = "\\Python\\py-reports\\check_ip_.txt"
        scripts_execution_info(main_path, name1)
        print("-"*40)
        name2 = "\\Python\\py-reports\\black_list_.txt"
        scripts_execution_info(main_path, name2)
        print("-"*40)
        name3 = "\\Python\\py-reports\\check_block_.txt"
        scripts_execution_info(main_path, name3)

    elif choice == "4":
        help_command = ["python", "ip_scanning.py", "--help"]
        input_help_validator(help_command)
        print("-----------------------------------------------------------")
        print("SCANNING IP ADDRESSES WITH NMAP")

        ip_nmap = input("Enter the IP to scan with nmap: ")
        ports_range = input("Enter port/range ports (e.g. 80 or 25-30): ")
        subprocess.run(
            ["python", "ip_scanning.py", "-ip", ip_nmap, "-ports", ports_range]
        )
        # Show the file-generated info
        main_path = path_finder()
        print("The file name created is VulnerabilityScanning_.txt")
        name = "\\Python\\py-reports\\VulnerabilityScanning_.txt"
        scripts_execution_info(main_path, name)

    elif choice == "5":
        help_command = ["python", "report_ip.py", "--help"]
        input_help_validator(help_command)
        print("-----------------------------------------------------------")
        print("REPORT AN IP WITH IP ABUSE DB")

        file_path = input("Enter the file NMAP scan path: ")
        subprocess.run(["python", "report_ip.py", "-file", file_path])
        # Show the file-generated info
        main_path = path_finder()
        print("The file name created is report_ip.txt")
        name = "\\Python\\py-reports\\report_ip.txt"
        scripts_execution_info(main_path, name)

    elif choice == "6":
        main()

    else:
        print("Invalid option. Please try again.")
        main_menu()


if __name__ == "__main__":
    main_menu()
