import os


def clear_screen():
    # check operating system
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


# clear the Screen
clear_screen()
