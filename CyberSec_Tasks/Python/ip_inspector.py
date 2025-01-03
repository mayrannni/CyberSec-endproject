#!/usr/bin/python3
"""We use the API-IPAbuseDatabase.

Check how reliable an IP is,
as well as blacklist depending on the trust of the IP
and check a block of IPs.
"""

import argparse
import datetime
import json
import logging
import re
import requests
import os
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
        raise argparse.ArgumentTypeError('The IP address given is invalid.')


def validate_rank(ip_range):
    """Validate an IP block."""
    pattern = re.compile(
        r"^"
        r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
        r"/([1-2]?[0-9]|24)"
        r"$"
    )
    if pattern.match(ip_range):
        return ip_range
    else:
        raise argparse.ArgumentTypeError('The given IP block is invalidated.')


def validate_day(day):
    """Validate that the day is within range."""
    if not day.isdigit() or not 1 <= int(day) <= 365:
        raise argparse.ArgumentTypeError(
            'The assigned number is not within the allowed range.'
            )
    return day


def validate_trust(trust):
    """Validate that the trust is within the allowed range."""
    if not trust.isdigit() or not 25 <= int(trust) <= 100:
        raise argparse.ArgumentTypeError(
            'The assigned number is not within the allowed range.'
            )
    return trust


mode = "How to use: python Nombre-archivo.py -ip 126.0.0.1 \
            -day 5-trust 90 -ip_range 120.0.0.1/24"
parser = argparse.ArgumentParser(
    description='The script reports abusive IP addresses,\
        and view the history of malicious activity associated with an IP or IP range.',
    epilog=mode,
    formatter_class=argparse.RawDescriptionHelpFormatter
    )
parser.add_argument('-ip', dest='ip', type=validate_ip,
                    help='IP to be analyzed.', required=True
                    )
parser.add_argument('-day', dest='day', type=validate_day,
                    help='Days to be investigated.'
                    )
parser.add_argument('-trust', dest='trust', type=validate_trust,
                    help='Minimum confidence limit of IPS (25-100).'
                    )
parser.add_argument('-ip_range', dest='ip_range', type=validate_rank,
                    help='IPS range to check(/24).', required=True
                    )
parameter = parser.parse_args()
api_key = 'bcabc2bfa1f341c5f720d7a3502b7e0b39e42cd127719eb63ed5413aaf06b3bc97d71cfb7966dd02'

date_stamp = datetime.datetime.now()
info = r'ip_abuse_database_'
info += str(date_stamp.strftime('%Y%m%d_%H%M%S'))
info += '.txt'

logging.basicConfig(filename=f'{info}',
                    level=logging.INFO
                    )

logging.info('Chek ip.')
subfolder = r'py-reports'
name1 = r'chek_ip.txt'
main_path = os.path.dirname(os.path.abspath(__file__))
path1 = os.path.join(main_path, subfolder, name1)
logging.info('Check the given IP.')
try:
    url = 'https://api.abuseipdb.com/api/v2/check'
    parameters = {
        "ipAddress": parameter.ip,
        "maxAgeInDays": parameter.day,
    }
    headers = {
        "Accept": "application/json",
        "Key": api_key
    }
    logging.info('Starting the application.')
    response = requests.get(url, headers=headers, params=parameters)
    if response.status_code == 200:
        database = response.json()
        logging.info(f'Creating the file {path1}.')
        with open(f'{path1}', 'w') as f:
            f.write(json.dumps(database, indent=4))
            logging.info('Your file has been successfully saved.')
    else:
        logging.info(
            f'File creation failed, response code {response.status_code}'
            )
except requests.exceptions.RequestException as e:
    logging.error(f'An error occurred while making your request: {e}')
except Exception as e:
    logging.error(f'An unexpected error occurred: {e}')

logging.info('Blacklist')
name2 = r'black_list.txt'
main_path = os.path.dirname(os.path.abspath(__file__))
path2 = os.path.join(main_path, subfolder, name2)
logging.info('Extract a list of IPs depending on their confidence level.')
try:
    url = 'https://api.abuseipdb.com/api/v2/blacklist'
    parameters = {
        "confidenceMinimum": parameter.trust
    }
    headers = {
        "Accept": "application/json",
        "Key": api_key
    }
    logging.info('Starting the application.')
    response = requests.get(url, headers=headers, params=parameters)
    if response.status_code == 200:
        database = response.json()
        logging.info(f'Creating the file {path2}.')
        with open(f'{path2}', 'w') as f:
            f.write(json.dumps(database, indent=4))
        logging.info('Your file has been successfully saved.')
    else:
        logging.info(
            f'File creation failed, response code {response.status_code}'
            )
except requests.exceptions.RequestException as e:
    logging.error(f'An error occurred while making your request: {e}')
except Exception as e:
    logging.error(f'An unexpected error occurred: {e}')

logging.info('Check Block')
subfolder = r'py-reports'
name3 = r'check_block.txt'
main_path = os.path.dirname(os.path.abspath(__file__))
path3 = os.path.join(main_path, subfolder, name3)
logging.info('Scan an IP block.')
try:
    url = 'https://api.abuseipdb.com/api/v2/check-block'
    parameters = {
        "network": parameter.ip_range,
        "maxAgeInDay": parameter.day
    }
    headers = {
        "Accept": "application/json",
        "Key": api_key
    }
    logging.info('Starting the application.')
    response = requests.get(url, headers=headers, params=parameters)
    if response.status_code == 200:
        database = response.json()
        logging.info(f'Creating the file {path3}.')
        with open(f'{path3}', 'w') as f:
            f.write(json.dumps(database, indent=4))
        logging.info('Your file has been successfully saved.')
    else:
        logging.info(
            f'File creation failed, response code {response.status_code}'
            )
except requests.exceptions.RequestException as e:
    logging.error(f'An error occurred while making your request: {e}')
except Exception as e:
    logging.error(f'An unexpected error occurred: {e}')

logging.info('Scan Completion')

py_menu()
