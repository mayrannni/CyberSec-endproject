import subprocess
import time
import os

def main():
    """ Comentario de lo que hace la función """
    print(
        'Los scripts de ciberseguridad fueron desarrollados en los siguientes lenguajes,',
        'selecciona uno de ellos para poder desplegar un submenu de las tareas.'
        )
    print("1. PowerShell")
    print("2. Bash")
    print("3. Python")
    print("Para salir escribe el numero 0")


def PowerShell():
    print(
        'A continuacion se desplegaran las opciones',
        'de tareas de ciberseguridad creadas a traves de PowerShell.'
        'Elige cual quieres realizar'
        )
    print("1. Get-PCInformation")
    print("2. Request-ApiHashBased")
    print("3. Show-HiddenFiles")
    print("4. Show-LogsLogin")
    print("Para regresar al menu principal ingresa 0")


def Bash():
    print(
        'A continuacion se desplegaran las opciones',
        'de tareas de ciberseguridad creadas a traves de bash.'
        'Elige cual quieres realizar'
        )
    print("1. Scanning ")
    print("2. HoneyPot")
    print("Para regresar al menu principal ingresa 0")


def ruta():
    "Busca la ruta donde esta ubicado el script"
    ruta_principal = os.path.dirname(os.path.abspath(__file__))
    name_file = "\menu_final.py"
    rutaf = ruta_principal+name_file
    return rutaf

def menu_principal():
    rutaf = ruta()
    opP = None
    while opP != "0":
        main()
        opP=input("Ingrese la opcion seleccionada ")
        if opP == """1""":
            while True:
                PowerShell()
                opS = input("Ingrese la opcion seleccionada ")
                if opS == "1":
                    subprocess.run(["python", rutaf, "-opP", opP, "-opS", opS])
                elif opS == "2":
                    subprocess.run(["python", rutaf, "-opP", opP, "-opS", opS])
                elif opS == "3":
                    subprocess.run(["python", rutaf, "-opP", opP, "-opS", opS])
                elif opS == "4":
                    subprocess.run(["python", rutaf, "-opP", opP, "-opS", opS])
                elif opS == "0":
                    time.sleep(2)
                    break
                else:
                    print("La opcion no se encuentra dentro de los parametros establecidos")
        elif opP == "2":
            Bash()
            opS=input("Ingrese la opcion seleccionada ")
            if opS == "1":
                subprocess.run(["python", rutaf, "-opP", opP, "-opS", opS])
            elif opS == "2":
                subprocess.run(["python", rutaf, "-opP", opP, "-opS", opS])
            elif opS == "0":
                time.sleep(2)
                break
        elif opP == "3":
            subprocess.run(["python", rutaf, "-opP", opP])
        elif opP == "0":
            print("Adios...")
            exit    
        else:
            print("La opcion no se encuentra dentro de los parametros establecidos")

if __name__ == "__main__":
    menu_principal()