"""This script makes a report with the file made from nmap script."""
import requests
import logging
import re
import argparse
import json


def file_with_content(file_path):
    """Check if the given file is or not a txt file with the content."""
    if re.search(r'\.txt$', file_path):
        try:
            with open(file_path, 'r') as file_content:
                pattern = "Starting Nmap"
                line = file_content.readline()
                if line:
                    if re.search(pattern, line):
                        return file_path
                    else:
                        raise argparse.ArgumentTypeError(
                            "The file given isn't a nmap scan report"
                        )
                        return file_path
                else:
                    raise argparse.ArgumentTypeError(
                        "The file doesn't contain anything")
                    return file_path
        except FileNotFoundError:
            raise argparse.ArgumentTypeError(
                "The given txt file doesn't exist")
    else:
        raise argparse.ArgumentTypeError("The file given isn't a txt file")
    return file_path


# Generate a config for the file info
logging.basicConfig(
    filename="Report_info.log",
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
)

# Generate a config for the file error
logging.basicConfig(
    filename="Report_errors.log",
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.ERROR,
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

arguments = parser.parse_args()
filename = arguments.file
logging.info(f"Using api key to log in {api_key}.")
# Check if the report finds an open port for the IP scanned
with open(filename, "r") as report_file:
    for line_num, line in enumerate(report_file, 1):
        if re.search(r"(\d+)/tcp\s+open", line):
            open_ports = True

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
                logging.error("Not enough information. Exit...")
    try:
        for port in ports:
            name = f"Report_Port.txt"
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
                with open(f"{name}", "w") as f:
                    f.write(json.dumps(information, indent=4))
                logging.INFO("Archivo guardado")
            except requests.exceptions.RequestException as e:
                logging.error(
                  f"An error occurred while making your request: {e}")
            except Exception as e:
                logging.error(f"Error: {e}")
    except Exception as error:
        logging.error("Unexpected error: %s" % error)
else:
    logging.error("There is no valuable information in this report.")
    logging.error("Try again later...")
