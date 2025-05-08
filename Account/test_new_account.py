# Group - 8
# Author - Kushal Patel
# Date - 10th April 2025
# Module - New Account

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select


class NewAccountTestCase(unittest.TestCase):

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

    def test_NA01(self):
        """End of test 1: ID cannot be empty"""
        new_acc_btn = self.driver.find_element(By.LINK_TEXT, "New Account")
        new_acc_btn.click()
        cus_id = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "cusid")))
        cus_id.click()
        cus_id.send_keys(Keys.TAB)
        self.assertIn("Customer ID is required", self.driver.find_element(By.ID, "message14").text)
        cus_id.clear()

    def test_NA02(self):
        """End of test 2: ID must be numeric"""
        cus_id = self.driver.find_element(By.NAME, "cusid")
        cus_id.send_keys("12abcd")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message14").text)
        cus_id.clear()

    def test_NA03(self):
        """End of test 3: ID cannot have special characters"""
        cus_id = self.driver.find_element(By.NAME, "cusid")
        cus_id.send_keys("12@#12")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message14").text)
        cus_id.clear()

    def test_NA04(self):
        """End of test 4: ID cannot have space in between"""
        cus_id = self.driver.find_element(By.NAME, "cusid")
        cus_id.send_keys("12 1223")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message14").text)
        cus_id.clear()

    def test_NA05(self):
        """End of test 5: ID cannot have first character a space"""
        cus_id = self.driver.find_element(By.NAME, "cusid")
        cus_id.send_keys(" 123456")
        self.assertIn("First character can not have space", self.driver.find_element(By.ID, "message14").text)
        cus_id.clear()

    def test_NA06(self):
        """End of test 6: Initial deposit cannot be empty"""
        initial_dep = self.driver.find_element(By.NAME, "inideposit")
        initial_dep.click()
        initial_dep.send_keys(Keys.TAB)
        self.assertIn("Initial Deposit must not be blank", self.driver.find_element(By.ID, "message19").text)
        initial_dep.clear()

    def test_NA07(self):
        """End of test 7: Initial deposit must be numeric"""
        initial_dep = self.driver.find_element(By.NAME, "inideposit")
        initial_dep.send_keys("12acbs")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message19").text)
        initial_dep.clear()

    def test_NA08(self):
        """End of test 8: Initial deposit cannot have special characters"""
        initial_dep = self.driver.find_element(By.NAME, "inideposit")
        initial_dep.send_keys("12#$$")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message19").text)
        initial_dep.clear()

    def test_NA09(self):
        """End of test 9: Initial deposit cannot have a space in between"""
        initial_dep = self.driver.find_element(By.NAME, "inideposit")
        initial_dep.send_keys("120 56")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message19").text)
        initial_dep.clear()

    def test_NA10(self):
        """End of test 10: Initial deposit cannot have first character space"""
        initial_dep = self.driver.find_element(By.NAME, "inideposit")
        initial_dep.send_keys(" 12345")
        self.assertIn("First character can not have space", self.driver.find_element(By.ID, "message19").text)
        initial_dep.clear()

    def test_NA11(self):
        """End of test 11: Saving account selected"""
        acc_type = Select(self.driver.find_element(By.NAME, "selaccount"))
        selected_option = acc_type.first_selected_option
        self.assertIn("Savings", selected_option.text)

    def test_NA12(self):
        """End of test 12: Current account selected"""
        acc_type = Select(self.driver.find_element(By.NAME, "selaccount"))
        acc_type.select_by_value("Current")
        selected_option = acc_type.first_selected_option
        self.assertIn("Current", selected_option.text)

    def test_NA13(self):
        """ENd of test 13: Resets all the fields"""
        cus_id = self.driver.find_element(By.NAME, "cusid")
        cus_id.send_keys("12345")
        acc_type = self.driver.find_element(By.NAME, "inideposit")
        acc_type.send_keys("10000")
        self.driver.find_element(By.NAME, "reset").click()
        self.assertIn("", cus_id.text)
        self.assertIn("", acc_type.text)
# ******************************************** Sometimes Fails, Please try again ***********************************************

    def test_NA14(self):
        """End of test 14: Shows the error message with incorrect ID"""
        cus_id = self.driver.find_element(By.NAME, "cusid")
        cus_id.send_keys("12345")
        acc_type = self.driver.find_element(By.NAME, "inideposit")
        acc_type.send_keys("10000")
        self.driver.find_element(By.NAME, "button2").click()
        alert = WebDriverWait(self.driver, 10).until(ec.alert_is_present())
        self.assertIn("Customer does not exist!!", alert.text)
        alert.accept()

# ******************************************** Sometimes Fails, Please try again ***********************************************

    def test_NA15(self):
        """End of test 15: Account generated successfully"""
        cus_id = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "cusid")))
        cus_id.clear()
        cus_id.send_keys("19810")
        acc_type = self.driver.find_element(By.NAME, "inideposit")
        acc_type.clear()
        acc_type.send_keys("12000")
        self.driver.find_element(By.NAME, "button2").click()
        success = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".heading3")))
        self.assertIn("Account Generated Successfully!!!", success.text)

    def test_NA16(self):
        """End of test 16: Returning to homepage"""
        continue_btn = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.LINK_TEXT, "Continue")))
        continue_btn.click()
        homepage = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".heading3 > td")))
        self.assertIn("Manger Id : mngr618642", homepage.text)

    # Teardown method - Runs after every testcases
    def tearDown(self):
        print("\n" + self.shortDescription())

    # Teardown class - runs once after all the tests are completed
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()