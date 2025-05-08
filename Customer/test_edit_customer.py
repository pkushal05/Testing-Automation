# Group - 8
# Author - Kushal Patel
# Date - 10th April 2025
# Module - Edit Customer

# Imports
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class EditCustomerTestCase(unittest.TestCase):

    # Setup class - runs once at the start
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://demo.guru99.com/V4/")
        user_id = cls.driver.find_element(By.NAME, "uid")
        user_id.send_keys("mngr618643")
        password = cls.driver.find_element(By.NAME, "password")
        password.send_keys("UgEpUze")
        login = cls.driver.find_element(By.NAME, "btnLogin")
        login.click()
        sleep(1)
        name_field = cls.driver.find_element(By.LINK_TEXT, "Edit Customer")
        name_field.click()

    def test_EC01(self):
        """End of test 1: Customer id cannot be empty"""
        name_field = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "cusid")))
        name_field.click()
        name_field.send_keys(Keys.TAB)
        self.assertIn("Customer ID is required", self.driver.find_element(By.ID, "message14").text)
        name_field.clear()

    def test_EC02(self):
        """End of test 2: Customer id must be numeric"""
        name_field = self.driver.find_element(By.NAME, "cusid")
        name_field.click()
        name_field.send_keys("1234Acc")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message14").text)
        name_field.clear()

    def test_EC03(self):
        """End of test 3: Customer id cannot have special character"""
        name_field = self.driver.find_element(By.NAME, "cusid")
        name_field.click()
        name_field.send_keys("123!@#")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message14").text)
        name_field.clear()

    def test_EC04(self):
        """End of test 4: Valid Customer ID"""
        name_field = self.driver.find_element(By.NAME, "cusid")
        name_field.click()
        name_field.send_keys("61629")
        name_field = self.driver.find_element(By.NAME, "AccSubmit")
        name_field.click()

    def test_EC05(self):
        """End of test 5: Address cannot be empty"""
        name_field = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "addr")))
        name_field.clear()
        name_field.send_keys(Keys.TAB)
        self.assertIn("Address Field must not be blank", self.driver.find_element(By.ID, "message3").text)

    def test_EC06(self):
        """End of test 6: City cannot be empty"""
        name_field = self.driver.find_element(By.NAME, "city")
        name_field.clear()
        name_field.send_keys(Keys.TAB)
        self.assertIn("City Field must not be blank", self.driver.find_element(By.ID, "message4").text)

    def test_EC07(self):
        """End of test 7: City cannot be numeric"""
        name_field = self.driver.find_element(By.NAME, "city")
        name_field.clear()
        name_field.send_keys("1234")
        self.assertIn("Numbers are not allowed", self.driver.find_element(By.ID, "message4").text)

    def test_EC08(self):
        """End of test 8: City cannot have special character"""
        name_field = self.driver.find_element(By.NAME, "city")
        name_field.clear()
        name_field.send_keys("City!@#")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message4").text)

    def test_EC09(self):
        """End of test 9: state cannot be empty"""
        name_field = self.driver.find_element(By.NAME, "state")
        name_field.clear()
        name_field.send_keys(Keys.TAB)
        self.assertIn("State must not be blank", self.driver.find_element(By.ID, "message5").text)

    def test_EC10(self):
        """End of test 10: State cannot be numeric"""
        name_field = self.driver.find_element(By.NAME, "state")
        name_field.clear()
        name_field.send_keys("1234")
        self.assertIn("Numbers are not allowed", self.driver.find_element(By.ID, "message5").text)

    def test_EC11(self):
        """End of test 11: State cannot have special character"""
        name_field = self.driver.find_element(By.NAME, "state")
        name_field.clear()
        name_field.send_keys("State!@#")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message5").text)

    def test_EC12(self):
        """End of test 12: PIN must be numeric"""
        name_field = self.driver.find_element(By.NAME, "pinno")
        name_field.clear()
        name_field.send_keys("1234PIN")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message6").text)

    def test_EC13(self):
        """End of test 13: PIN cannot be empty"""
        name_field = self.driver.find_element(By.NAME, "pinno")
        name_field.clear()
        name_field.send_keys(Keys.TAB)
        self.assertIn("PIN Code must not be blank", self.driver.find_element(By.ID, "message6").text)

    def test_EC14(self):
        """End of test 14: PIN must have 6 digits"""
        name_field = self.driver.find_element(By.NAME, "pinno")
        name_field.clear()
        name_field.send_keys("1234")
        self.assertIn("PIN Code must have 6 Digits", self.driver.find_element(By.ID, "message6").text)

    def test_EC15(self):
        """End of test 15: PIN cannot have special character"""
        name_field = self.driver.find_element(By.NAME, "pinno")
        name_field.clear()
        name_field.send_keys("123!@#")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message6").text)

    def test_EC16(self):
        """End of test 16: Mobile No. cannot be empty"""
        name_field = self.driver.find_element(By.NAME, "telephoneno")
        name_field.clear()
        name_field.send_keys(Keys.TAB)
        self.assertIn("Mobile no must not be blank", self.driver.find_element(By.ID, "message7").text)

    def test_EC17(self):
        """End of test 17: Mobile No. cannot have special character"""
        name_field = self.driver.find_element(By.NAME, "telephoneno")
        name_field.clear()
        name_field.send_keys("886636!@12")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message7").text)

    def test_EC18(self):
        """End of test 18: Email cannot be empty"""
        name_field = self.driver.find_element(By.NAME, "emailid")
        name_field.clear()
        name_field.send_keys(Keys.TAB)
        self.assertIn("Email-ID must not be blank", self.driver.find_element(By.ID, "message9").text)

    def test_EC19(self):
        """End of test 19: Email must be in format career@guru99.com"""
        name_field = self.driver.find_element(By.NAME, "emailid")
        name_field.clear()
        name_field.send_keys("guru99@gmail")
        self.assertIn("Email-ID is not valid", self.driver.find_element(By.ID, "message9").text)

    def test_EC20(self):
        """*** Failed Test - The page is not Working ***"""
        name_field = self.driver.find_element(By.NAME, "telephoneno")
        name_field.clear()
        name_field.send_keys("4370001234")
        name_field = self.driver.find_element(By.NAME, "sub")
        name_field.click()
        self.assertIn("Update done successfully", self.driver.find_element(By.CSS_SELECTOR, "body").text)

    # Teardown method - Runs after every testcases
    def tearDown(self):
        print("\n" + self.shortDescription())

    # Teardown class - runs once after all the tests are completed
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()