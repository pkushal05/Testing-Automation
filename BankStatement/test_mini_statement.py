# Group - 8
# Author - Kushal Patel
# Date - 10th April 2025
# Module - Mini Statement

# Imports
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class MiniStatementTestCase(unittest.TestCase):

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

    def test_MS01(self):
        """End of test 1: Account number cannot be empty"""
        mini_statement_btn = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.LINK_TEXT, "Mini Statement")))
        mini_statement_btn.click()
        acc_no = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "accountno")))
        acc_no.click()
        acc_no.send_keys(Keys.TAB)
        self.assertIn("Account Number must not be blank", self.driver.find_element(By.ID, "message2").text)

    def test_MS02(self):
        """End of test 2: Account number must be numeric"""
        acc_no = self.driver.find_element(By.NAME, "accountno")
        acc_no.send_keys("kjh12")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message2").text)
        acc_no.clear()

    def test_MS03(self):
        """End of test 3: Account number cannot have special characters"""
        acc_no = self.driver.find_element(By.NAME, "accountno")
        acc_no.send_keys("123#$%")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message2").text)
        acc_no.clear()

    def test_MS04(self):
        """End of test 4: Account number cannot have a space character"""
        acc_no = self.driver.find_element(By.NAME, "accountno")
        acc_no.send_keys("128 697")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message2").text)
        acc_no.clear()

    def test_MS05(self):
        """*** Failed Test - It accepts account number with space in front ***"""
        acc_no = self.driver.find_element(By.NAME, "accountno")
        acc_no.send_keys(" 897561")
        self.assertIn("First character can not have space", self.driver.find_element(By.ID, "message2").text)
        acc_no.clear()

    def test_MS07(self):
        """*** Failed Test - The page is not working ***"""
        acc_no = self.driver.find_element(By.NAME, "accountno")
        acc_no.send_keys("143968")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.assertIn("Shows account statement", self.driver.find_element(By.CSS_SELECTOR, ".heading3").text)

    def test_MS06(self):
        """End of test 7: Shows alert with invalid account number"""
        acc_no = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "accountno")))
        acc_no.send_keys("123789")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        alert = WebDriverWait(self.driver, 10).until(ec.alert_is_present())
        self.assertIn("Account does not exist", alert.text)
        alert.accept()

    def test_MS08(self):
        """End of test 8: Resets all the fields"""
        self.driver.back()
        acc_no = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "accountno")))
        acc_no.send_keys("123856")
        self.driver.find_element(By.NAME, "res").click()
        self.assertIn("", acc_no.text)

    # Teardown method - Runs after every testcases
    def tearDown(self):
        print("\n" + self.shortDescription())

    # Teardown class - runs once after all the tests are completed
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()