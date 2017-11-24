#! usr/bin/env python3
"""
mail room refractored!
"""
import math
import unittest
import sys

donors_dict = {
    'Hermione Granger': [43.01, 13.13],
    'Molly Weasley':[87.03, 44.55],
    'Luna Lovegood':[61.03, 44.87, 27.77],
    'Sybill Trelawney':[77.56, 33.45,  756.32]
    }

# main menu functions
def main_menu():
    menu = ('''
    Thank you donating to Hogwarts School. Choose an action:
    1. - Send a Thank You Owl
    2. - Create a Report
    3. - Quit
    > ''')
    print(menu)
    return menu

def ty_menu():
     menu = ('''
     Enter a donor's name.
     *or*
     Enter 'list' to view donor list
     Enter 'return' to return to main menu
     ''')

def user_input():
    action = input("Enter selection:")
    return action.strip()




def quit():
    print("Goodbye!")
    sys.exit(0)

def test():
    unittest.main()
    return

if __name__ == "__main__":
    running_dict = {
        "1":send_owl,
        "2":print_report,
        "3":quit
        }
    user_input


        # else:
        #     try:
        #         running_dict.get(selection)()
        #         print("attempt2")
        #     except KeyError:
        #         print("This error!")
