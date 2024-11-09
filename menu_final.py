""""Agregar comentario"""
import argparse, hashlib
import logging, os 
import subprocess, sys, time
from subprocess_menu import menu_principal

def ruta():
    "Busca la ruta donde esta ubicado el script"
    ruta_principal = os.path.dirname(os.path.abspath(__file__))
    return ruta_principal


def input_help_validator(help_command):
    """Validate help command"""
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

mode = """
Run the next command:
python "/ruta/del/archivo/menu_final.py" -opP "1" -opS "3" """

parser = argparse.ArgumentParser(
    description="", 
    epilog= mode, 
    formatter_class=argparse.RawDescriptionHelpFormatter
    )
parser.add_argument(
    '-opP', 
    dest= 'opP',
    help= 'Opcion a seleccionar del menu principal',
    required= True,
    type= str
    )
parser.add_argument(
    '-opS', 
    dest='opS',
    help= 'Opcion a seleccionar del menu principal',
    type= str
    )
param = parser.parse_args() 

sys_op=sys.platform
if sys_op == "win32":
    if param.opP == "1":
        name_file = r"\PowerShell\Get-PcInformation.psm1"
        ruta_principal = ruta()
        sec = ruta_principal+name_file
        print(sec)
        if param.opS == "1":
            if os.path.exists(sec):
                help_command = [
                    "PowerShell", 
                    sec, 
                    "--help"]
                input_help_validator(help_command)
                print("")
                print("\n----------------------------------------- \n")                            
                subprocess.run(
                    [
                        "Powershell",
                        "-ExecutionPolicy", 
                        "Bypass", 
                        sec
                        ]
                        )#Comentario de que hace
                                
            else:
                print("El archivo no existe...")
                time.sleep(2)
        elif param.opS == "2":
            name_file =  r"\PowerShell\Request-ApiHashBased.psm1"
            ruta_principal = ruta()
            sec = ruta_principal+name_file
            if os.path.exists(sec):
                help_command = [
                    "PowerShell", 
                    sec, 
                    "--help"
                    ]
                input_help_validator(help_command)
                print("\n----------------------------------------- \n")
                subprocess.run(
                    [
                        "Powershell", 
                        "-ExecutionPolicy",
                        "Bypass", 
                        sec 
                        ]
                        )
            else:
                print("El archivo no existe.")
                time.sleep(2)
        elif param.opS == "3":
            name_file = r"\PowerShell\Show-HiddenFiles.ps1"
            ruta_principal = ruta()
            sec = ruta_principal+name_file
            if os.path.exists(sec):
                help_command = [
                    "PowerShell", 
                    sec, 
                    "--help"
                    ]
                input_help_validator(help_command)
                print("\n----------------------------------------- \n")
                subprocess.run(
                    [
                        "Powershell", 
                        "-ExecutionPolicy",
                        "Bypass", 
                        sec 
                        ]
                        )
            else:
                print("El archivo no existe.")
                time.sleep(2)
        elif param.opS == "4":
            name_file = r"\PowerShell\Show-LogsLogin.psm1"
            ruta_principal = ruta()
            sec = ruta_principal+name_file
            if os.path.exists(sec):
                help_command = [
                    "PowerShell", 
                    sec, 
                    "--help"
                    ]
                input_help_validator(help_command)
                print("\n----------------------------------------- \n")
                subprocess.run(
                    [
                        "Powershell", 
                        "-ExecutionPolicy",
                        "Bypass", 
                        sec 
                        ]
                        )
            else:
                print("El archivo no existe.")
                time.sleep(2)
        else:
            print("Opciob no valida")
    elif param.opP == "2":
        print(
            'No se puede ejecutar esta opción ya que tu sistema operativo es Windows'
            )
        print('Redirigiendo al menu  pricipal... \n')
        time.sleep(2)
    elif param.opP == "3":
        name_file = r"/Python/main_menu.py"
        ruta_principal = ruta()
        sec = ruta_principal+name_file
        if os.path.exists(sec):
        #mandar a llamar al script ya definido de python
            subprocess.run(
                "python", 
                sec,
                capture_output=True,
                text=True
                )
        else:
            print("El archivo no existe.")
elif sys_op == "linux":
    if param.opP == "1":
        print(
            'No se puede ejecutar esta opción,',
            'ya que tu sistema operativo es Linux'
            )
        print('Redirigiendo al menu principal...\n')
    elif param.opP == "2":
        if param.opS == "1":
            name_file = r"/Bash/scanning.sh"
            ruta_principal = ruta()
            sec = ruta_principal+name_file
            if os.path.exists(sec):
                subprocess.run(
                    ["Bash", 
                    sec],
                    capture_output=True,
                    text=True,
                    shell=True,
                    executable='/bin/bash'
                    )
        elif param.opS == "2":
            name_file = r"/Bash/ssh_honeypot.sh"
            ruta_principal = ruta()
            sec = ruta_principal+name_file
            if os.path.exists(sec):
                subprocess.run(
                    ["Bash", 
                    sec],
                    capture_output=True,
                    text=True,
                    shell=True,
                    executable='/bin/bash'
                    )
        elif param.opS == "0":
            print("Volviendo al menu principal...")
            time.sleep(2)
        else:
            print("La opcion ingresada no se encuentra dentro de los parametros")
    elif param.opP == "3":
        name_file = r"/Python/main_menu.py"
        ruta_principal = ruta()
        sec = ruta_principal+name_file
        if os.path.exists(sec):
        #mandar a llamar al script ya definido de python
            subprocess.run(
                "python", 
                "main_menu.py",
                capture_output=True,
                text=True
                )
        else:
            print("El archivo no existe.")
elif sys_op == "darwin":
    if param.opP == "1":
        print(
            'No se puede ejecutar esta opción,',
            'ya que tu sistema operativo es Linux'
            )
        print('Redirigiendo al menu principal...\n')
    elif param.opP == "2":
        if param.opS == "1":
            name_file = r"/Bash/scanning.sh"
            ruta_principal = ruta()
            sec = ruta_principal+name_file
            if os.path.exists(sec):
                subprocess.run(
                    ["Bash", 
                    sec],
                    capture_output=True,
                    text=True,
                    shell=True,
                    executable='/bin/bash'
                    )
        elif param.opS == "2":
            name_file = r"/Bash/ssh_honeypot.sh"
            ruta_principal = ruta()
            sec = ruta_principal+name_file
            if os.path.exists(sec):
                subprocess.run(
                    ["Bash", 
                    sec],
                    capture_output=True,
                    text=True,
                    shell=True,
                    executable='/bin/bash'
                    )
        elif param.opS == "0":
            print("Volviendo al menu principal...")
            time.sleep(2)
        else:
            print("La opcion ingresada no se encuentra dentro de los parametros")
    elif param.opP == "3":
        name_file = r"/Python/main_menu.py"
        ruta_principal = ruta()
        sec = ruta_principal+name_file
        if os.path.exists(sec):
            subprocess.run(
                "python", 
                "main_menu.py",
                capture_output=True,
                text=True
                )
        else:
            print("El archivo no existe.")
else:
    print("No se reconoce el sistema operativo")

menu_principal()