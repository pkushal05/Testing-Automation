# Group - 8
# Author - Kushal Patel
# Date - 10th April 2025
# Module - Delete Customer

# Imports
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class DelCustomerTestCase(unittest.TestCase):

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

    def test_DC01(self):
        """End of test 1: ID cannot be empty"""
        del_customer_btn = self.driver.find_element(By.LINK_TEXT, "Delete Customer")
        del_customer_btn.click()
        cus_id = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "cusid")))
        cus_id.click()
        cus_id.send_keys(Keys.TAB)
        self.assertIn("Customer ID is required", self.driver.find_element(By.ID, "message14").text)
        cus_id.clear()

    def test_DC02(self):
        """End of test 2: ID must be numeric"""
        cus_id = self.driver.find_element(By.NAME, "cusid")
        cus_id.send_keys("123abc")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message14").text)
        cus_id.clear()

    def test_DC03(self):
        """End of test 3: ID cannot have special characters"""
        cus_id = self.driver.find_element(By.NAME, "cusid")
        cus_id.send_keys("12@#12")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message14").text)
        cus_id.clear()

    def test_DC04(self):
        """End of test 4: ID cannot have space in between"""
        cus_id = self.driver.find_element(By.NAME, "cusid")
        cus_id.send_keys("12 1223")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message14").text)
        cus_id.clear()

    def test_DC05(self):
        """End of test 5: ID cannot have first character a space"""
        cus_id = self.driver.find_element(By.NAME, "cusid")
        cus_id.send_keys(" 123456")
        self.assertIn("First character can not have space", self.driver.find_element(By.ID, "message14").text)
        cus_id.clear()

    def test_DC06(self):
        """End of test 6: Shows the error message with incorrect ID"""
        cus_id = self.driver.find_element(By.NAME, "cusid")
        cus_id.send_keys("78912")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        alert1 = self.driver.switch_to.alert
        alert1.accept()
        alert2 = self.driver.switch_to.alert
        self.assertIn(alert2.text, "Customer does not exist!!")
        alert2.accept()

    def test_DC07(self):
        """End of test 7: Shows the error message with correct ID"""
        cus_id = self.driver.find_element(By.NAME, "cusid")
        cus_id.send_keys("19810")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        alert1 = self.driver.switch_to.alert
        alert1.accept()
        alert2 = self.driver.switch_to.alert
        self.assertIn("Customer could not be deleted!!. First delete all accounts of this customer then delete the customer", alert2.text)
        alert2.accept()

    def test_DC08(self):
        """End of test 8: Resets the field"""
        cus_id = self.driver.find_element(By.NAME, "cusid")
        cus_id.send_keys("45678")
        self.driver.find_element(By.NAME, "res").click()
        self.assertIn("", cus_id.text)

    # Teardown method - Runs after every testcases
    def tearDown(self):
        print("\n" + self.shortDescription())

    # Teardown class - runs once after all the tests are completed
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




