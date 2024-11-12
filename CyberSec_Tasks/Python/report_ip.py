#!/usr/bin/python3
"""This script makes a report with the file made from nmap script."""

import requests
import logging
import os
import re
import argparse
import json
from py_scripts_handler import py_menu

def file_with_content(file_path):
    """Check if the given file is or not a txt file with the content."""
    if re.search(r'\.txt$', file_path):
        try:
            with open(file_path, 'r') as file_content:
                pattern = "Starting Nmap"
                line = file_content.readline()
                if line:
                    if re.search(pattern, line):
                        logging.info(
                            "The vulnerabilities report scan have been found")
                        return file_path
                    else:
                        logging.error("The file given isn't a nmap scan report")
                        raise argparse.ArgumentTypeError()
                else:
                    logging.error("The file doesn't contain anything")
                    raise argparse.ArgumentTypeError()
        except FileNotFoundError:
            logging.error("The given txt file doesn't exist")
            raise argparse.ArgumentTypeError()
    else:
        logging.error("The file given isn't a txt file")
        raise argparse.ArgumentTypeError()


# Generate a config for the file info
logging.basicConfig(
    filename="report_ip.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)

mode = """
Run the following command:
python report.py -file 'txt file generated from the nmap scanning'
"""
parser = argparse.ArgumentParser(
    description="This script reads a txt file and makes a web report",
    epilog=mode,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

parser.add_argument(
    "-file",
    metavar="TXT_FILE",
    dest="file",
    help="file using to extract the data necessary to make the report",
    required="True",
    type=file_with_content
)

api_key = (
    "429c2b4681c79e8ed2505bde41513f604af76"
    "ec69a4a0d41bcd6146b6b67a6c09d3c6c1a218df66d"
)
# Nmap scan file
arguments = parser.parse_args()
filename = arguments.file
logging.info(f"Using api key to log in {api_key}.")
main_path = os.path.dirname(os.path.abspath(__file__))
name = os.path.join(main_path, "py-reports","report_ip.txt")

if os.path.exists(filename):
    open_ports = False
    with open(filename, "r") as report_file:
        for line_num, line in enumerate(report_file, 1):
            # Check if the report finds an open port for the IP scanned
            if re.search(r"(\d+)/tcp\s+open", line):
                open_ports = True
                raise Exception("The given vulnerabilities scan ")
        if open_ports:
            logging.info("There are open ports in NMAP scan-file.")
            ports = []
            with open(filename, "r") as report_file:
                for nline, line in enumerate(report_file, 1):
                    # Extract info from the nmap scan report file
                    if "Nmap scan report for" in line:
                        ip_address = line.split()[-1].strip("()")
                        logging.info(f"Found an IP in file! >> {ip_address}")
                    elif "/tcp" in line:
                        port = line.split()[0].strip("/tcp")
                        ports.append(port)
                        state = line.split()[1]
                    else:
                        logging.error("Not enough information.")
                        # Store information in the file report about the error
                        with open(name, "w") as f:
                            f.write("Not enough information.")
            try:
                # Report the open ports in the API Abuseip
                for port in ports:
                    try:
                        url = "https://api.abuseipdb.com/api/v2/report"
                        parameters = {
                            "ip": ip_address,
                            "categories": 14,
                            "comment": f"""
                            The IP has been scanned and found the port {port} is open,
                            some vulnerabilities have likely been found.
                            """,
                        }
                        headers = {"Accept": "application/json", "Key": api_key}
                        response = requests.post(url, headers=headers, data=parameters)
                        information = response.json()
                        logging.info(information)
                        with open(name, "w") as f:
                            f.write(json.dumps(information, indent=4))
                        logging.info("Saved file.")
                    except requests.exceptions.RequestException as e:
                        logging.error(
                        f"An error occurred while making your request: {e}")
                        # Store information in the file report about the error
                        with open(name, "w") as f:
                            f.write(f"An error occurred while making your request: {e}")
                    except Exception as e:
                        logging.error(f"Error: {e}")
                        # Store information in the file report about the error
                        with open(name, "w") as f:
                            f.write(e)
            except Exception as error:
                logging.error("Unexpected error: %s" % error)
                # Store information in the file report about the error
                with open(name, "w") as f:
                    f.write("An unespected error have been ocurred")
        else:
            logging.error("There is no valuable information in this report.")
            logging.error("Try again later...")
            # Store information in the file report about the error
            with open(name, "w") as f:
                f.write("The file doesn't have any open port")
else:
    # Store information in the file report about the error
    with open(name, "w") as f:
        f.write("The file doesn't exist")
    print("Check if the vulnerabilities scan have run before")
