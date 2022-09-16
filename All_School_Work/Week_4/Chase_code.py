import imp
import os
from time import sleep

def CLEAR_CONSOLE():
    # Windows
    if os.name == "nt":
        return os.system('cls')

    # For mac and Linux
    else:
        return os.system('clear')

print("Hello there. ")
sleep(2)
CLEAR_CONSOLE
print('It worked? ')