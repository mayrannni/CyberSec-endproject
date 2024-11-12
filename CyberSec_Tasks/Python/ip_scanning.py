#!/usr/bin/python3
"""Analyzes vulnerabilities that may exist in the target."""

import argparse
import datetime
import logging
import os
import re
import subprocess
import sys
import webbrowser
from py_scripts_handler import py_menu

def validate_ip(ip):
    """Validate a single IP."""
    pattern = re.compile(
        r"^"
        r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
        r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
        r"$"
        )
    if pattern.match(ip):
        return ip
    else:
        raise argparse.ArgumentTypeError(
            'The IP address given is invalid.'
            )
    return ip


def validate_port(ports):
    """Validate port(s)"""
    if re.fullmatch(r'\d{1,5}', ports):
        port = int(ports)
        if 1 <= port <= 65535:
            return ports
        else:
            raise argparse.ArgumentTypeError(
                'The port is not within range'
                )
    if re.fullmatch(r'\d{1,5}-\d{1,5}', ports):
            beginning, end = map(int, ports.split('-'))
            if 1 <= beginning <=65535 and 1 <= end <= 65535 and beginning < end:
                return ports
            else:
                raise argparse.ArgumentTypeError(
                    'Ports are not within range'
                    )


def vulnerability_scanning(param, path):
    """Return the target's vulnerabilities."""
    try:
        operating_system = sys.platform 
        command = ['nmap', '-p', param.ports, '--open', '-Pn',
                   '-T4', '-sV', '--script',
                   'vuln', param.ip]
        if operating_system =="win32":
            ps_line = 'powershell -Executionpolicy Bypass -Command ' + \
                  ' '.join(command)
        elif operating_system == "linux":
            ps_line = 'Bash -Command ' + ' '.join(command)
        elif operating_system == "darwin":
            ps_line = 'Bash -Command ' + ' '.join(command)
        else: 
            print("The operating system is not recognized...")
        results = subprocess.run(ps_line, capture_output=True, text=True)
        logging.info(command)
        logging.info(ps_line)
        logging.info('Starting the process')
        if results.returncode == 0:
            if results:
                logging.info('The nmap scan has completed successfully.')
                with open(f'{path}', 'w') as file:
                    file.write(f'{results.stdout}')
                    logging.info(
                        f'The file has been successfully saved in: {path}.'
                        )
            else:
                logging.info('No known vulnerabilities were found.')
    except subprocess.CalledProcessError as e:
        logging.error(
            f'An error occurred while trying to execute the command: {e}'
            )
    except Exception as e:
        logging.error(f'An unexpected error has occurred: {e}')


mode = """Run the following command:
python "IPVulnerabilities.py" -ip -ports

Ideal scenario
- Install nmap from https://nmap.org/download

Notes
- This script requires nmap to be installed on your computer (https://nmap.org/download)
- The scan usually takes a while to complete"""
parser = argparse.ArgumentParser(
    description='The script scans an IP for its vulnerabilities using nmap.',
    epilog=mode,
    formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-ip', dest='ip', help='Ip to be analyzed',
                    type=validate_ip, required=True)
parser.add_argument('-ports', dest='ports', type=validate_port,
                    help='Port to be analyzed', required=True)
param = parser.parse_args()


subfolder = r'py-reports'
main_path = os.path.dirname(os.path.abspath(__file__))
name = r'VulnerabilityScanning.txt'
path = os.path.join(main_path, subfolder, name)
abs_file_path = os.path.abspath(path)

date = datetime.datetime.now()
info = r'scanner'
info += str(date.strftime('%Y%m%d_%H%M%S'))
info += '.log'

logging.basicConfig(filename=f'{info}', level=logging.INFO)
logging.info(path)

#Check if Nmap is installed
try:
    logging.info('Checking if nmap is installed.')
    result = subprocess.run(['Nmap', '--version'],
                            check=True, capture_output=True, text=True)
    nmap_exist = 'True'
except (subprocess.CalledProcessError, FileNotFoundError):
#Redirect to the installation page
    logging.info('nmap is not installed, redirecting to download page')
    install = webbrowser.open('https://nmap.org/download')
    logging.info(install)
    nmap_exist = 'False'

#Run the function only if Nmap is installed
if nmap_exist == 'True':
    logging.info('Nmap is installed')
    vulnerability_scanning(param, abs_file_path)
