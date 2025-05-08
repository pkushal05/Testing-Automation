# Group - 8
# Author - Kushal Patel
# Date - 10th April 2025
# Module - Test Suites (Menu Driven automation)

# Imports
import unittest
from Account.test_new_account import NewAccountTestCase
from Account.test_edit_account import EditAccountTestCase
from Account.test_delete_account import DelAccountTestCase
from Customer.test_new_customer import NewCustomerTestCase
from Customer.test_delete_customer import DelCustomerTestCase
from Customer.test_edit_customer import EditCustomerTestCase
from BankStatement.test_mini_statement import MiniStatementTestCase
from BankStatement.test_customized_statement import CustomStatementTestCase
from BankStatement.test_balance_enquiry import BalanceEnquiryTestCase


def run_tests(choice):
    """Function which loads all the test cases on specific choice input"""

    suite = unittest.TestSuite()

    if choice == 1:

        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(NewCustomerTestCase))

    elif choice == 2:

        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(DelCustomerTestCase))

    elif choice == 3:

        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(EditCustomerTestCase))

    elif choice == 4:

        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(NewAccountTestCase))

    elif choice == 5:

        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(EditAccountTestCase))

    elif choice == 6:

        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(DelAccountTestCase))

    elif choice == 7:

        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(BalanceEnquiryTestCase))

    elif choice == 8:

        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(MiniStatementTestCase))

    elif choice == 9:

        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(CustomStatementTestCase))
    else:
        print("Invalid Choice")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)


def validate_choice(prompt):
    """Function to return the user input after validating."""
    while True:
        user_input = input(prompt).strip()
        try:
            user_input = int(user_input)
            if 0 <= user_input <= 9: # Checking if the input is between 0 and 9 (inclusive)
                return user_input
            else:
                print("**** Enter a valid number from menu ****")
        except ValueError:
            print("**** Please enter a number ****")


while True:

    # Printing the Menu
    print("\n==================================================================================")
    print("                           INFT 1207 - Group 8 Project")
    print("====================================================================================")
    print("1. Run New Customer Test")
    print("2. Run Delete Customer Test")
    print("3. Run Edit Customer Test")
    print("4. Run New Account Test")
    print("5. Run Edit Account Test")
    print("6. Run Delete Account Test")
    print("7. Run Balance Enquiry Test")
    print("8. Run Mini Statement Test")
    print("9. Run Customized Statement Test")
    print("0. Exit")
    print("====================================================================================")

    user_choice = validate_choice("Enter a choice => ") # Asking for user input

    if user_choice == 0: # Exiting if input is 0
        print("Exiting.....")
        break
    else: # Calling the run_tests function
        run_tests(user_choice)

    while True: # Asking the user, if they want to run more tests.
        repeat_program = input("Do you want to run tests further (Y/N)?  ").strip().lower()

        if repeat_program == "y":
            break
        elif repeat_program == "n":
            print("Exiting....")
            exit(0)
        else:
            print("**** Please enter Y or N ****")
