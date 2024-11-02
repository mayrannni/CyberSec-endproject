"""This script search for the hash and date form a file."""
import hashlib
import os
import time


def file_info(path):
    """Show the hash and date obtained."""
    try:
        file_ob = open(path, 'rb')
    except Exception:
        print("The file doesn't exists")
    else:
        # Hash value from the file
        file_ = file_ob.read()
        hash_info = hashlib.sha512(file_)
        hash_value = hash_info.hexdigest()
        # File date when was created
        file_time = os.path.getctime(path)
        file_date = time.ctime(file_time)
        formated_date = time.strftime("%d-%m-%Y %H:%M:%S",
                                      time.strptime(file_date))
        print("The file hash is: %s" % hash_value,
              "\n"+("-"*50),
              "\nThe creation date of the file is: %s" % formated_date)
