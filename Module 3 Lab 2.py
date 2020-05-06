"""
CTEC 121
Filipp Kopytyuk
Intro into Programming & Problem Solving
Module 3 Lab 2
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    try:
        print(4/0)
    except ZeroDivisionError:
        print("\nThere was a divide by zero error. Exiting\n")
        exit
    except:
        print("\nThere was a divide by zero error. Exiting\n")
        exit


main()    