import os
import sys
import platform
from colorama import *

# reset the color
reset = Style.RESET_ALL

# Check if the script is run as root
if os.geteuid() != 0:
    print(f'{Fore.LIGHTRED_EX}[-] Please run this script with sudo.{reset}')
    sys.exit(1)

# Get the operating system
OS = platform.system()

if OS == 'Linux':
    os.system('clear')
    print(f'{Back.LIGHTGREEN_EX}{Fore.BLUE}{Style.NORMAL}[x]Created By *(AbdelilahAit)*{reset}')
    print(f'{Fore.LIGHTBLUE_EX}[*] Welcome To : {Fore.LIGHTGREEN_EX}findpsk.py{reset}')
    
    path = '/etc/NetworkManager/system-connections/'
    files = [file for file in os.listdir(path)]#if file.endswith('.nmconnection')]
    for index, file in enumerate(files, 1):
        print(f'{reset}[{Fore.LIGHTCYAN_EX}{index}{reset}]{Fore.LIGHTGREEN_EX}-{reset}[{Fore.LIGHTMAGENTA_EX}{file}{reset}]{Fore.LIGHTBLUE_EX}')
    
    last_index = len(files)
    try:
        while True:
            wifi_index = int(input(f'{Fore.LIGHTBLUE_EX}[+] Enter ESSID From 1 To {last_index} : {Fore.LIGHTGREEN_EX}'))
            if 1 <= wifi_index <= last_index:
                break
            else:
                print(f'{Fore.LIGHTRED_EX}The Number Should Be From 1 To {last_index}{reset}')
    except ValueError:
        print(f'{Fore.LIGHTRED_EX}[-] The Input Should Be [Int] Number{reset}')
        exit()

    FILE = files[wifi_index - 1]
    print(FILE)

    try:
        with open(os.path.join(path, FILE), 'r') as f:
            lines = f.readlines()
            password_line = next((line for line in lines if line.startswith('psk=')), None)
            if password_line:
                password = password_line.split('=')[1].strip()
                print(f'{Fore.LIGHTRED_EX}{Style.BRIGHT}Password : {Back.LIGHTGREEN_EX}{Fore.LIGHTBLACK_EX}', password, f'{reset}')
            else:
                print(f'{Fore.LIGHTRED_EX}[-] Password not found in {FILE}{reset}')
    except FileNotFoundError:
        print(f'{Fore.LIGHTRED_EX}[-] File Not Found: {FILE}{reset}')
    except Exception as e:
        print(f'{Fore.LIGHTRED_EX}[-] An error occurred: {str(e)}{reset}')
else:
    print(f'{Fore.LIGHTRED_EX}[-] This System Is Not Supported For Windows{reset}')
