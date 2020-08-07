#!/usr/bin/env python3
from os import system, name
# Creates a class for text colors
class colors:
    red = '\033[1;31;1m'
    green = '\033[1;32;1m'
    cyan = '\033[0;36;1m'
    end = '\033[0m'

# Detects if using windows or unix based system and sends 'cls' or 'clear' respectively to clear screen
def clear():

    if name == 'nt':
        l = system('cls')

    else:
        l = system('clear')
clear()

# Prints title and fake copyright stuff

print(colors.cyan + """
███████╗██████╗  █████╗ ███╗   ███╗    ██████╗  ██████╗ ████████╗
██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██╔══██╗██╔═══██╗╚══██╔══╝
███████╗██████╔╝███████║██╔████╔██║    ██████╔╝██║   ██║   ██║
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██╔══██╗██║   ██║   ██║
███████║██║     ██║  ██║██║ ╚═╝ ██║    ██████╔╝╚██████╔╝   ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝  ╚═════╝    ╚═╝""" + colors.end)
print(colors.red + 'Copyright © 2020 Vidun Jayakody. All rights reserved.\n' + colors.end)

print('INSTRUCTIONS:\n')
print('* Enter the word or phrase you would like to spam,\n')
print('* Enter how many times the word should be repeated,\n')
print('* The chatbot requires a messenging app (Messenger, iMessage, Discord, etc.) to be open and the text already selected.'
      ' The countdown timer should be long enough for you to switch over to that app and select the text field.\n')

# Asks user to continue
yn = input(colors.cyan + 'Would you like to continue? (y/n) ' + colors.end)

# If user enters a positive answer proceed with code
if yn == 'y' or yn == 'Y' or yn == 'yes':
    # !/usr/bin/env python
    # pyautogui sends the keystrokes and time is for countdown
    import pyautogui, time
    # Clears screen, imitating next page kinda vibe
    clear()


    def countdown():

        for i in range(t):
            print('Spamming ' + '"' + s + '" ' + str(n) + " times in: " + colors.red + str(t-i) + colors.end)
            time.sleep(1)

    print(colors.cyan + """
███████╗██████╗  █████╗ ███╗   ███╗    ██████╗  ██████╗ ████████╗
██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██╔══██╗██╔═══██╗╚══██╔══╝
███████╗██████╔╝███████║██╔████╔██║    ██████╔╝██║   ██║   ██║
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██╔══██╗██║   ██║   ██║
███████║██║     ██║  ██║██║ ╚═╝ ██║    ██████╔╝╚██████╔╝   ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝  ╚═════╝    ╚═╝""" + colors.end)
    print(colors.red + 'Copyright © 2020 Vidun Jayakody. All rights reserved.\n' + colors.end)

    # Asks the input questions
    s = input('Enter a word or phrase to spam: ')

    # Check if these input is an integer, if not prompt user to enter integer
    while True:

        try:
            n = int(input('How many times should ' + '"' + s + '" ' + 'be repeated? '))

        except ValueError:
            print(colors.red + 'Please enter an integer!' + colors.end)
            continue

        else:
            break

    # Check if these input is an integer, if not prompt user to enter integer
    while True:

        try:
            t = int(input('How long should the timer be set for? '))

        except ValueError:
            print(colors.red + "That's not a valid timer value!" + colors.end)
            continue

        else:
            break

countdown()

# Success message
print(colors.green + '\nSpambot launched successfully!' + colors.end)

# Send keystrokes of the phrase/word x number of times and press enter each time (to send)
for f in range(n):
        pyautogui.typewrite(s)
        time.sleep(0.5)
        pyautogui.press('enter')
# If they select no, exit the script. Why would you even open it then
else:
    exit()