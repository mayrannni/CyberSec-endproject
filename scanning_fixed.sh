#!/bin/bash

# $1 is the ip to scan
# $2 is the range ports, it has to be a only one like 8080 or a range like 0-255

path="$PWD/bash-reports/scanning.txt"
errors="$PWD/errorsPortScan.log"
# Create a new file
touch $path
# Extract open ports from a given IP
nmap -p $2 $1 > $path 2> $errors
# Error manage
if [[ -s $errors ]];then
    echo "We have errors which are saved in: $errors"
else
    # If we have no error the error file will be removed
    rm $errors
    echo "The port scan has completed and the file has been saved to: $path"
fi

# Create the path for the port open Scan, vulnerabilities scan, and errors
path="$PWD/bash-reports/vulnerabilities.txt"
pathScan="$PWD/test.txt"
errorsV="$PWD/errorsVuln.log"
# Create a new file for the open ports scan
touch $pathScan
# Chek open ports and extract vulnerabilities
nmap $1 | grep 'open' > $pathScan 2> $errorsV
if [[ -s $errorsV ]];then
    echo "We have errors which are saved in: $errors"
else
    # If the last command executes correctly the error.log file will be deleted 
    rm $errorsV
    # Reviewing the output from the open ports scan to check if there is at least one open port
    if [[ -s $pathScan ]];then
        # Create the vulnerabilites 
        touch $path
        # If we have at least one open port we do the nmap vulnerabilities scan
        nmap -sV --script=vuln $IP > $path 2> $errorsV
        if [ -s $errorsV ];then
            # The error manage
            echo "We have errors which are saved in: $errorsV"
        else
            # If there is no error in the vulnerabilities scan we remove the test ports open scan file and error file
            rm $errorsV
            rm $pathScan
            echo "The port scan has completed and the file has been saved in: $path"
        fi
    else
        # If the file of the open ports scan is empty (that means there are no open ports) the vulnerabilities scan will not realesed
        echo "The scan did not run because there are no ports open"
    fi
fi
