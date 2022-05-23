# AaaS - Adages as a Service v1.0

# Project Goals
# Display a start message/greeting.
# Return a line from each column.
# Combine lines to create a new adage.

import random
import time

FIRST_COLUMN = "column-1.txt"
SECOND_COLUMN = "column-2.txt"

def get_adage(file):
    adage_list = []
    try:
        openfile = open(file, 'r')
    except IOError:
        print("Unable to open adage file.")
    line = openfile.readline()
    while line != '':
        adage_list.append(line)
        line = openfile.readline()
    openfile.close()
    num_items = len(adage_list)
    index = random.randint(0, num_items - 1)
    return adage_list[index]

def header():

    print()
    print("---------------------------------------------")
    print(" = Welcome to Adages as a Service (AaaS) =")
    print("---------------------------------------------")
    print()
    time.sleep(1.5)
    print("Searching the internet for \"advice\"...")
    time.sleep(1.5)
    print("Compiling millions of life experiences...")
    time.sleep(1.5)
    print("Exporting best attempt at advice. Bad advice possible.")
    time.sleep(2)

def main():

    again = 'y'
    while again.lower() == 'y':

        # Call forth the Adages
        first_column = get_adage(FIRST_COLUMN)
        second_column = get_adage(SECOND_COLUMN)

        # r.strip removes mark to end line, aka help to combine.
        first_word = first_column.rstrip()
        second_word = second_column.rstrip()
        
        # Concatenate adages and display.
        time.sleep(1.5)
        print()
        print("Well, you know what they always say...")
        time.sleep(1.5)
        print()
        print("===")
        print(f"{first_word} {second_word}!")
        print("===")
        time.sleep(2)

        # Continue?
        print()
        print("Would you like to extend your AaaS free trial?")
        print()
        time.sleep(1.5)
        again = input("(Press 'y' for yes, or " +
                        "any other key for no) ")
        if again.lower() != "y":
            break
    print()
    print("Thanks for using AaaS, a bill based on your daily usage will be withdrawn soon. Goodbye.")
    print()

# Call Header, 1st time only.
header()
main()