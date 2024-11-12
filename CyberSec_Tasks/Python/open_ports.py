#!/usr/bin/python3
"""Take an ip and scan their open ports using Shodan API."""

import logging
import argparse
import os
import re
import json
import shodan
from py_scripts_handler import py_menu

def validate_ip(ip):
    """Validate a single IP."""
    pattern = re.compile(
        r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
        )
    if pattern.match(ip):
        return ip
    else:
        raise argparse.ArgumentTypeError(
            'The IP address given is invalid.'
            )


# Generate a config for the file error
logging.basicConfig(
    filename="open_ports_api.log",
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.ERROR,
)

# Create an argument for the sripts run
mode = """
Run the next command:
python ip_openports_scan.py -ip 'target ip'
"""
ips = argparse.ArgumentParser(
    description="IPs to make the scan of their ports",
    epilog=mode,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
ips.add_argument(
    "-ip",
    metavar="IP",
    dest="ip",
    type=validate_ip,
    help="IP to analyze their ports",
    required=True,
)

arguments = ips.parse_args()
ip = arguments.ip

# The shodan api key to authenticate our search in the api
api_key = "qYsYnBh8c6vx820iWeJc9VwzFMcIUU5l"
# File to save the results
main_path = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(main_path, "py-reports", "open_ports_report.txt")
try:
    api = shodan.Shodan(api_key)
except shodan.APIError as error:
    print(">> An error occurred with the API: \n%s" % error)
    logging.error(f"Error: {error}")
    # Store information in the file report about the error
    with open(file_name, "w") as file:
        file.write("An error occurred with the API: \n%s" % error)
else:
    # Save the response in a txt file to make reading easier
    with open(file_name, "w") as file:
        try:
            response = api.host(ip)
            file.write(f"<< Open ports in IP : {ip} >>\n")
            for port in response["ports"]:
                file.write(f"> {port} <\n")
            file.write("Scan complete, Have a nice day :D")

        except shodan.APIError as error:
            print(">> An error occurred with the API: \n%s" % error)
            logging.error(f"Error: {error}")
            # Store information in the file report about the error
            with open(file_name, "w") as file:
                file.write("An error occurred with the API: \n%s" % error)

        except Exception as error:
            print(">> An error occurred: \n%s" % error)
            logging.error(f"Error: {error}")
            # Store information in the file report about the error
            with open(file_name, "w") as file:
                file.write("An error occurred: \n%s" % error)
        else:
            response = api.host(ip)
            full_response = os.path.join(main_path, "py-reports", 
                                         "open_ports_all_info.txt")
            with open(full_response, "w") as file:
                data = json.dumps(response, indent=4)
                file.write(data)
            print(
                'Data requested are saved in open_ports_report.txt'
                '\n And the full info requested are in %s'
                % full_response
            )
            print("Scan completed for the ip: %s" % ip)
            print(
                "The full response and info.log files are created"
                " with the IP scan requested"
            )
        finally:
            print("Execution completed have a nice day :D")
