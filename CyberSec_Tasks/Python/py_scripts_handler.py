#!/usr/bin/python3
"""Do the python scripts management"""

import hashlib
import datetime
import os
import sys
import subprocess
import time
import re
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
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
        time.sleep(1)


def scripts_execution_info(filename):
    """Show hash and datetime."""
    # execution date
    get_date = datetime.datetime.now()
    date = get_date.strftime("%d-%m-%Y %H:%M:%S.%f")
    print("Script successfully completed its task at: %s" % date)
    # file hash
    try:
        file_ob = open(filename, "rb")
    except Exception:
        print("File Not Found.")
    else:
        # hash value from file
        file_to_hash = file_ob.read()
        hash_info = hashlib.sha512(file_to_hash)
        hash_value = hash_info.hexdigest()
        print(
            ">> File HASH is: %s\n>> Generated report PATH by script is: %s"
            % (hash_value, filename)
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
        pyfile = os.path.join("web_scanning.py")
        main_path = path_finder()
        abs_pyfile = os.path.join(main_path, pyfile)
        abs_pyfile = os.path.abspath(abs_pyfile)
        help_command = ["python", abs_pyfile, "--help"]
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
        ws_html_path = r"\py-reports\WebPentest.*html"
        pattern = re.compile(ws_html_path)
        for root, dirs, files in os.walk(main_path):
            for file in files:
                if pattern.match(file):
                    file_name = file
        print(f"The file name created is {file_name}")
        web_pentest_report = os.path.join(main_path, "py-reports",file_name)
        web_pentest_report = os.path.abspath(web_pentest_report)
        scripts_execution_info(web_pentest_report)
        py_menu()
    elif choice == "2":
        pyfile = os.path.join("open_ports.py")
        main_path = path_finder()
        abs_pyfile = os.path.join(main_path, pyfile)
        abs_pyfile = os.path.abspath(abs_pyfile)
        help_command = ["python", abs_pyfile, "--help"]
        input_help_validator(help_command)
        print("-----------------------------------------------------------")
        print("VERIFY OPEN PORTS WITH SHODAN")

        ip = input("Enter the IP to scan (e.g. '8.8.8.8'): ")
        subprocess.run(["python", "open_ports.py", "-ip", ip])
        # Show the file-generated info
        print("The files name created is: \n"
              ">> open_ports_report.txt",
              ">> open_ports_all_info.txt")
        # Open ports report file
        open_port_report = os.path.join(main_path,"py-reports", 
                                        "open_ports_report.txt")
        open_port_report = os.path.abspath(open_port_report)
        scripts_execution_info(open_port_report)
        print("-"*40)
        # Full response from the API file
        print("The file name with all info from the IP using the Shdan API"
              "are created in open_ports_all_info.txt")
        full_response_report = os.path.join(main_path,"py-reports",
                                            "open_ports_all_info.txt")
        full_response_report = os.path.abspath(full_response_report)
        scripts_execution_info(full_response_report)
        py_menu()
    elif choice == "3":
        pyfile = os.path.join("ip_inspector.py")
        main_path = path_finder()
        abs_pyfile = os.path.join(main_path, pyfile)
        abs_pyfile = os.path.abspath(abs_pyfile)
        help_command = ["python", abs_pyfile, "--help"]
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
        print("The files name created are: \n"
              ">> check_ip.txt",
              ">> black_list.txt",
              ">> check_block.txt")
        # Show the file-generated info
        # chek_ip.txt file
        vuln_ip_report = os.path.join(main_path, "py-reports","check_ip.txt")
        vuln_ip_report = os.path.abspath(vuln_ip_report)
        scripts_execution_info(vul_ip_report)
        print("-"*40)
        # black_list.txt
        black_list_report = os.path.join(main_path, "py-reports","black_list_.txt")
        black_list_report = os.path.abspath(black_list_report)
        scripts_execution_info(black_list_report)
        print("-"*40)
        # check_block
        check_block_report = os.path.join(main_path, "py-reports","check_block_.txt")
        check_block_report = os.path.abspath(check_block_report)
        scripts_execution_info(check_block_report)
        py_menu()
    elif choice == "4":
        pyfile = os.path.join("ip_scanning.py")
        main_path = path_finder()
        abs_pyfile = os.path.join(main_path, pyfile)
        abs_pyfile = os.path.abspath(abs_pyfile)
        help_command = ["python", abs_pyfile, "--help"]
        input_help_validator(help_command)
        print("-----------------------------------------------------------")
        print("SCANNING IP ADDRESSES WITH NMAP")

        ip_nmap = input("Enter the IP to scan with nmap: ")
        ports_range = input("Enter port/range ports (e.g. 80 or 25-30): ")
        subprocess.run(
            ["python", abs_pyfile, "-ip", ip_nmap, "-ports", ports_range]
        )
        # Show the file-generated info
        print("The file name created is VulnerabilityScanning.txt")
        vul_scan_report = os.path.join(main_path, "py-reports","VulnerabilityScanning.txt")
        vul_scan_report = os.path.abspath(vul_scan_report)
        scripts_execution_info(vul_scan_report)
        py_menu()
    elif choice == "5":
        pyfile = os.path.join("report_ip.py")
        main_path = path_finder()
        abs_pyfile = os.path.join(main_path, pyfile)
        abs_pyfile = os.path.abspath(abs_pyfile)
        help_command = ["python", abs_pyfile, "--help"]
        input_help_validator(help_command)
        print("-----------------------------------------------------------")
        print("REPORT AN IP WITH IP ABUSE DB")

        file_path = os.path.join(main_path,"py-reports","VulnerabilityScanning.txt")
        subprocess.run(["python", abs_pyfile, "-file", file_path])
        # Show the file-generated info
        print("The file name created is report_ip.txt")
        ip_reports_report = os.path.join(main_path,"py-reports","report_ip.txt")
        scripts_execution_info(ip_reports_report)
        py_menu()
    elif choice == "6":
        main()

    else:
        print("Invalid option. Please try again.")
        py_menu()

if __name__ == "__main__":
    py_menu()
