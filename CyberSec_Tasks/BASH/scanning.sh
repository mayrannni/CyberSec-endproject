#!/bin/bash

show_help() {
    echo "Usage: scanning.sh [-h] [-p PORT] [-ip IP]"
    echo "This script makes a ports and vulnerabilities scan"
    echo ""
    echo "Options:"
    echo "-h, --help		shows this help"
    echo "-p <port(s)>		give the ports or port"
    echo "-ip			ip to scan"
    echo "PORT			e.g. 80-100 or 22"
    echo "IP			format: ***.***.***.*** 0-255"
    echo "NAME			enter the file name, not path"
    echo "Script makes a results report and save it on your system"
    echo "We hope the script handling with a menu will make your life easier :)"
}

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -h | --help)
            show_help
            exit 0 ;;
        -p)
            ports="$2"
            shift ;;
       	-ip)
            IP="$3"
	    shift ;;
         *)
            echo "Unrecognized choice: $1"
            show_help
            exit 1 ;;
    esac
    shift
done

#Functions
ports_scan() {
    if [[ -z "$ports"  ]]; then
        read -p ">> ports range or port to scan " ports
    elif [[ -z "$IP" ]]; then
    	read -p ">> ip to scan " IP
    elif [[ -z "$file" ]]; then
    	read -p ">> filename report (where your results will be saved) " file
    fi
    path="$PWD/bash-reports/port_scan.txt"
    errors="$PWD/errorsPortScan.log"
    #Create a new file
    touch $path
    #Extract open ports from a given IP
    nmap -p $ports $IP > $path 2> $errors
    if [[ -s $errors ]];then
        echo "We have an errors wich are saved in: $errors"
    else
        rm $errors
    fi
}

vulnerability_scan() {
    if [[ -z "$ports"  ]]; then
        read -p ">> ports range or port to scan " ports
    elif [[ -z "$IP" ]]; then
    	read -p ">> ip to scan " IP
    elif [[ -z "$file" ]]; then
    	read -p ">> filename report (where your results will be saved) " file
    fi
    path="$PWD/bash-reports/vulnerabilities_scan.txt"
    pathScan="$PWD/test.txt"
    errorsV="$PWD/errorsVuln.log"
    #Create a new file
    touch $pathScan
    #Chek open ports and extract vulnerabilities
    nmap $IP | grep 'open' > $pathScan 2> $errorsV
    if [[ -s $errorsV ]];then
        echo "We have an errors wich are saved in: $errors"
    else
        rm $errorsV
        if [[ -s $pathScan ]];then
            touch $path
            nmap -sV --script=vuln $IP > $path 2> $errorsV
            if [ -s $errorsV ];then
                echo "We have an errors wich are saved in: $errorsV"
            else
                rm $errorsV
                rm $pathScan
            fi
        else
            echo "The scan did not run because there are no ports open"
            touch $path
        fi
    fi
}

ports_scan 
vulnerability_scan 
