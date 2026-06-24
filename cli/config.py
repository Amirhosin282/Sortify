from time import sleep
from colorama import Fore
import sys
import os
from pyfiglet import figlet_format
from rainbowtext import text
import platform

def ClearCLI():
    """for clear terminal on windows and linux automaticly"""
    if platform.system() == 'Linux':
        os.system("clear")
    elif platform.system() == 'Windows':
        os.system("cls")
    return

line = "_________________________________________________________________"

if __name__ == '__main__': # sey to user
    ClearCLI()
    print(Fore.RED, 'run main.py, this is not main file ')
    sleep(5)
    sys.exit()

def view(): # app banner
    
    """show a minimal CLI banner to user"""
    
    ClearCLI()

    print(Fore.GREEN)

    print(text(figlet_format("Sortify", font="slant")), end = "")

    print(Fore.YELLOW)
    print("_________________________________________________________________", end = "\n\n")

    print(Fore.RED, '    discription: ',Fore.GREEN, "Sortify — A simple file organizer written in Python")
    print(Fore.RED, '    github: ',Fore.GREEN,'     https://github.com/Amirhosin282')
    print(Fore.RED, '    by: ',Fore.BLUE,'         amirhosin282')
    print(Fore.YELLOW, end = "")
    print("_________________________________________________________________")