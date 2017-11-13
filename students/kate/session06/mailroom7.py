#! usr/bin/env python3
"""
mail room refractored!
"""
import math
import unittest

donors_dict = {
    'Hermione Granger': [43.01, 13.13],
    'Molly Weasley':[87.03, 44.55],
    'Luna Lovegood':[61.03, 44.87, 27.77],
    'Sybill Trelawney':[77.56, 33.45,  756.32]
    }

# main menu functions
def main_menu():
    action = input('''
    Thank you donating to Hogwarts School. Choose an action:
    1. - Send a Thank You Owl
    2. - Create a Report
    3. - Test
    4. - Quit
    > ''')
    return action.strip()

def write_ty(donor_input, amount):
    return('''
     Dear {}
     Thank you for your very donation of ${:.2f}.
     You have enabled excellent magical instruction!
                    Sincerely,
                       -Hogwarts School of Witchcraft and Wizardy
     '''.format(donor_input, amount))

def send_owl():
    while True:
        donor_name = input('''
        Enter a donor's name.
        *or*
        Enter 'list' to view donor list
        Enter 'return' to return to main menu

        >
        ''').strip()

        if donor_name == 'list':
            print_donors_list()
        elif donor_name == 'return':
            return
        else:
            break

    while True:
        amount = input('''
        Enter donation amount
        > $
        ''').strip()
        if amount == "return":
            return
        try:
            amount = float(amount)
        except ValueError:
            print("Invali entry! please enter a number!")
        else:
            break

    donors_dict[donor_name].append(amount)
    print(write_ty(donor_name, amount))
    print(send_owl())
    return

def print_donors_list():
    print("Donors: \n ")
    for key in donors_dict:
        print(key)

def sort_key(item):
    return item[1]

def print_report():
    report_rows = []

    for keys, values in donors_dict.items():
        total_gifts = sum(values)
        num_gifts = len(values)
        avg_gift = total_gifts / num_gifts
        report_rows.append((keys, total_gifts, num_gifts, avg_gift))

    report_rows.sort(key=sort_key)

    # print table with spaces for formatting
    print("{:30s}  {:10s}  {:10s}  {:10s}".format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("*" * 66)
    rows = [print("{:30s}   {:10f}   {:10d}   {:10f} ".format(*row)) for row in report_rows]

def quit():
    sys.exit(0)

def test():
    unittest.main()
    return

class MyTests(unittest.TestCase):
    def test_abc(self):
        selection = ("1")
        donor_input = "Helena"
        amount = 55.66
        pass


# dictionary for the menu!!
if __name__ == "__main__":
    running_dict = {
        "1":send_owl,
        "2":print_report,
        "3":test,
        "4":quit
        }
    selection = main_menu()
    try:
        running_dict.get(selection)()
    except (KeyError):
        print("This error again!")
