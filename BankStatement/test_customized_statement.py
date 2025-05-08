# Group - 8
# Author - Kushal Patel
# Date - 10th April 2025
# Module - Customized Statement

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class CustomStatementTestCase(unittest.TestCase):

    # Setup class - runs once at the start
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://demo.guru99.com/V4/")
        user_id = cls.driver.find_element(By.NAME, "uid")
        user_id.send_keys("mngr618642")
        password = cls.driver.find_element(By.NAME, "password")
        password.send_keys("Adahavu")
        login = cls.driver.find_element(By.NAME, "btnLogin")
        login.click()
        sleep(1)

    def test_CS01(self):
        """End of test 1: Account number cannot be empty"""
        cust_statement_btn = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.LINK_TEXT, "Customised Statement")))
        cust_statement_btn.click()
        acc_no = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "accountno")))
        acc_no.click()
        acc_no.send_keys(Keys.TAB)
        self.assertIn("Account Number must not be blank", self.driver.find_element(By.ID, "message2").text)

    def test_CS02(self):
        """End of test 2: Account number must be numeric"""
        acc_no = self.driver.find_element(By.NAME, "accountno")
        acc_no.send_keys("lao12")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message2").text)
        acc_no.clear()

    def test_CS03(self):
        """End of test 3: Account number cannot have special characters"""
        acc_no = self.driver.find_element(By.NAME, "accountno")
        acc_no.send_keys("(*$&$")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message2").text)
        acc_no.clear()

    def test_CS04(self):
        """End of test 4: Account number cannot have a space character"""
        acc_no = self.driver.find_element(By.NAME, "accountno")
        acc_no.send_keys("870 924")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message2").text)
        acc_no.clear()

    def test_CS05(self):
        """*** Failed Test - It accepts account number with space in front ***"""
        acc_no = self.driver.find_element(By.NAME, "accountno")
        acc_no.send_keys(" 803731")
        self.assertIn("First character can not have space", self.driver.find_element(By.ID, "message2").text)
        acc_no.clear()

    def test_CS06(self):
        """End of test 6: From date field cannot be empty"""
        f_date = self.driver.find_element(By.NAME, "fdate")
        f_date.click()
        self.assertIn("From Date Field must not be blank", self.driver.find_element(By.ID, "message26").text)

    def test_CS07(self):
        """End of test 7: To date field cannot be empty"""
        t_date = self.driver.find_element(By.NAME, "tdate")
        t_date.click()
        self.assertIn("To Date Field must not be blank", self.driver.find_element(By.ID, "message27").text)

    def test_CS08(self):
        """End of test 8: Minimum amount must be numeric"""
        min_transaction = self.driver.find_element(By.NAME, "amountlowerlimit")
        min_transaction.click()
        min_transaction.send_keys("12ywrhg")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message12").text)
        min_transaction.clear()

    def test_CS09(self):
        """End of test 9: Minimum amount cannot have special characters"""
        min_transaction = self.driver.find_element(By.NAME, "amountlowerlimit")
        min_transaction.send_keys("85#$&")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message12").text)
        min_transaction.clear()

    def test_CS10(self):
        """End of test 10: Minimum amount cannot have space in between"""
        min_transaction = self.driver.find_element(By.NAME, "amountlowerlimit")
        min_transaction.send_keys("789 013")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message12").text)
        min_transaction.clear()

    def test_CS11(self):
        """*** Failed Test - It accepts minimum amount with space in front ***"""
        min_transaction = self.driver.find_element(By.NAME, "amountlowerlimit")
        min_transaction.send_keys(" 897561")
        self.assertIn("First character can not have space", self.driver.find_element(By.ID, "message12").text)
        min_transaction.clear()

    def test_CS12(self):
        """End of test 12: Number of transactions must be numeric"""
        transaction_no = self.driver.find_element(By.NAME, "numtransaction")
        transaction_no.click()
        transaction_no.send_keys("85emkek")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message13").text)
        transaction_no.clear()

    def test_CS13(self):
        """End of test 13: Number of transactions cannot have special characters"""
        transaction_no = self.driver.find_element(By.NAME, "numtransaction")
        transaction_no.send_keys("%#&(")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message13").text)
        transaction_no.clear()

    def test_CS14(self):
        """End of test 14: Number of transactions cannot have space in between"""
        transaction_no = self.driver.find_element(By.NAME, "numtransaction")
        transaction_no.send_keys("5879 21")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message13").text)
        transaction_no.clear()

    def test_CS15(self):
        """*** Failed Test - It accepts account number with space in front ***"""
        transaction_no = self.driver.find_element(By.NAME, "numtransaction")
        transaction_no.send_keys(" 178923")
        self.assertIn("First character can not have space", self.driver.find_element(By.ID, "message13").text)
        transaction_no.clear()

    def test_CS16(self):
        """End of test 16: Resets all the fields"""
        acc_no = self.driver.find_element(By.NAME, "accountno")
        acc_no.click()
        acc_no.clear()
        acc_no.send_keys("875694")

        f_date = self.driver.find_element(By.NAME, "fdate")
        f_date.click()
        f_date.__setattr__("value", "2024-01-01")

        t_date = self.driver.find_element(By.NAME, "tdate")
        t_date.click()
        t_date.__setattr__("value", "2024-01-30")

        min_transaction = self.driver.find_element(By.NAME, "amountlowerlimit")
        min_transaction.click()
        min_transaction.clear()
        min_transaction.send_keys("10000")

        transaction_no = self.driver.find_element(By.NAME, "numtransaction")
        transaction_no.click()
        transaction_no.clear()
        transaction_no.send_keys("100")

        self.driver.find_element(By.NAME, "res").click()

        self.assertIn("", acc_no.text)
        self.assertIn("", f_date.text)
        self.assertIn("", t_date.text)
        self.assertIn("", min_transaction.text)
        self.assertIn("", transaction_no.text)

    def test_CS17(self):
        """*** Failed Test - Blank page pops up ***"""
        acc_no = self.driver.find_element(By.NAME, "accountno")
        acc_no.click()
        acc_no.send_keys("143968")

        f_date = self.driver.find_element(By.NAME, "fdate")
        f_date.click()
        f_date.__setattr__("value", "2024-01-01")

        t_date = self.driver.find_element(By.NAME, "tdate")
        t_date.click()
        t_date.__setattr__("value", "2024-01-30")

        min_transaction = self.driver.find_element(By.NAME, "amountlowerlimit")
        min_transaction.click()
        min_transaction.send_keys("5000")

        transaction_no = self.driver.find_element(By.NAME, "numtransaction")
        transaction_no.click()
        transaction_no.send_keys("10")

        self.driver.find_element(By.NAME, "AccSubmit").click()

        alert = self.driver.switch_to.alert
        self.assertIn("Please fill all fields", alert.text)

    # Teardown method - Runs after every testcases
    def tearDown(self):
        print("\n" + self.shortDescription())

    # Teardown class - runs once after all the tests are completed
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()