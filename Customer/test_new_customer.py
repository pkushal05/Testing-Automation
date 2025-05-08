# Group - 8
# Author - Kushal Patel
# Date - 10th April 2025
# Module - New Customer

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class NewCustomerTestCase(unittest.TestCase):

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

    def test_NC01(self):
        """End of test 1: Name cannot be empty"""
        customer_btn = self.driver.find_element(By.LINK_TEXT, "New Customer")
        customer_btn.click()
        name_field = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "name")))
        name_field.click()
        name_field.send_keys(Keys.TAB)
        self.assertIn("Customer name must not be blank", self.driver.find_element(By.ID, "message").text)
        name_field.clear()

    def test_NC02(self):
        """End of test 2: Name cannot be numeric"""
        name_field = self.driver.find_element(By.NAME, "name")
        name_field.send_keys("1234")
        self.assertIn("Numbers are not allowed", self.driver.find_element(By.ID, "message").text)
        name_field.clear()

    def test_NC03(self):
        """End of test 3: Name cannot have special characters"""
        name_field = self.driver.find_element(By.NAME, "name")
        name_field.send_keys("@#$")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message").text)
        name_field.clear()

    def test_NC04(self):
        """End of test 4: Name cannot have space as first character"""
        name_field = self.driver.find_element(By.NAME, "name")
        name_field.send_keys(" Kushal")
        self.assertIn("First character can not have space", self.driver.find_element(By.ID, "message").text)
        name_field.clear()

    def test_NC05(self):
        """End of test 5: Address field must not be blank"""
        addr_field = self.driver.find_element(By.NAME, "addr")
        addr_field.send_keys(Keys.TAB)
        self.assertIn("Address Field must not be blank", self.driver.find_element(By.ID, "message3").text)
        addr_field.clear()

    def test_NC06(self):
        """End of test 6: Address field cannot have space as first character"""
        addr_field = self.driver.find_element(By.NAME, "addr")
        addr_field.send_keys(" Simcoe street")
        self.assertIn("First character can not have space", self.driver.find_element(By.ID, "message3").text)
        addr_field.clear()

    def test_NC07(self):
        """End of test: City cannot be empty"""
        city_field = self.driver.find_element(By.NAME, "city")
        city_field.send_keys(Keys.TAB)
        self.assertIn("City Field must not be blank", self.driver.find_element(By.ID, "message4").text)
        city_field.clear()

    def test_NC08(self):
        """End of test: City cannot be numeric"""
        city_field = self.driver.find_element(By.NAME, "city")
        city_field.send_keys("city123")
        self.assertIn("Numbers are not allowed", self.driver.find_element(By.ID, "message4").text)
        city_field.clear()

    def test_NC09(self):
        """End of test: City cannot have special character"""
        city_field = self.driver.find_element(By.NAME, "city")
        city_field.send_keys("city@#$")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message4").text)
        city_field.clear()

    def test_NC10(self):
        """End of test: City cannot have first blank space"""
        city_field = self.driver.find_element(By.NAME, "city")
        city_field.send_keys(" city")
        self.assertIn("First character can not have space", self.driver.find_element(By.ID, "message4").text)
        city_field.clear()

    def test_NC11(self):
        """End of test: State cannot be empty"""
        state_field = self.driver.find_element(By.NAME, "state")
        state_field.send_keys(Keys.TAB)
        self.assertIn("State must not be blank", self.driver.find_element(By.ID, "message5").text)
        state_field.clear()

    def test_NC12(self):
        """End of test: State cannot be numeric"""
        state_field = self.driver.find_element(By.NAME, "state")
        state_field.send_keys("state123")
        self.assertIn("Numbers are not allowed", self.driver.find_element(By.ID, "message5").text)
        state_field.clear()

    def test_NC13(self):
        """End of test: State cannot have special character"""
        state_field = self.driver.find_element(By.NAME, "state")
        state_field.send_keys("state@#$")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message5").text)
        state_field.clear()

    def test_NC14(self):
        """End of test: State cannot have first blank space"""
        state_field = self.driver.find_element(By.NAME, "state")
        state_field.send_keys(" state")
        self.assertIn("First character can not have space", self.driver.find_element(By.ID, "message5").text)
        state_field.clear()

    def test_NC15(self):
        """End of test: PIN cannot be empty"""
        pin_field = self.driver.find_element(By.NAME, "pinno")
        pin_field.send_keys(Keys.TAB)
        self.assertIn("PIN Code must not be blank", self.driver.find_element(By.ID, "message6").text)
        pin_field.clear()

    def test_NC16(self):
        """End of test: PIN must be numeric"""
        pin_field = self.driver.find_element(By.NAME, "pinno")
        pin_field.send_keys("123PIN")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message6").text)
        pin_field.clear()

    def test_NC17(self):
        """End of test: PIN must be 6 digit"""
        pin_field = self.driver.find_element(By.NAME, "pinno")
        pin_field.send_keys("1234")
        self.assertIn("PIN Code must have 6 Digits", self.driver.find_element(By.ID, "message6").text)
        pin_field.clear()

    def test_NC18(self):
        """End of test: PIN cannot have special character"""
        pin_field = self.driver.find_element(By.NAME, "pinno")
        pin_field.send_keys("12@#$")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message6").text)
        pin_field.clear()

    def test_NC19(self):
        """End of test: PIN cannot have first blank space"""
        pin_field = self.driver.find_element(By.NAME, "pinno")
        pin_field.send_keys(" 123")
        self.assertIn("First character can not have space", self.driver.find_element(By.ID, "message6").text)
        pin_field.clear()

    def test_NC20(self):
        """End of test: PIN cannot have blank space in between"""
        pin_field = self.driver.find_element(By.NAME, "pinno")
        pin_field.send_keys("12 23")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message6").text)
        pin_field.clear()

    def test_NC21(self):
        """End of test: Mobile number cannot be empty"""
        mobile_field = self.driver.find_element(By.NAME, "telephoneno")
        mobile_field.send_keys(Keys.TAB)
        self.assertIn("Mobile no must not be blank", self.driver.find_element(By.ID, "message7").text)
        mobile_field.clear()

    def test_NC22(self):
        """End of test: Mobile number cannot have first blank space"""
        mobile_field = self.driver.find_element(By.NAME, "telephoneno")
        mobile_field.send_keys(" 123")
        self.assertIn("First character can not have space", self.driver.find_element(By.ID, "message7").text)
        mobile_field.clear()

    def test_NC23(self):
        """End of test: Mobile number cannot have blank space in between"""
        mobile_field = self.driver.find_element(By.NAME, "telephoneno")
        mobile_field.send_keys("12 23")
        self.assertIn("Characters are not allowed", self.driver.find_element(By.ID, "message7").text)
        mobile_field.clear()

    def test_NC24(self):
        """End of test: Mobile number cannot have special character"""
        mobile_field = self.driver.find_element(By.NAME, "telephoneno")
        mobile_field.send_keys("12@#$")
        self.assertIn("Special characters are not allowed", self.driver.find_element(By.ID, "message7").text)
        mobile_field.clear()

    def test_NC25(self):
        """End of test: Email cannot be empty"""
        email_field = self.driver.find_element(By.NAME, "emailid")
        email_field.send_keys(Keys.TAB)
        self.assertIn("Email-ID must not be blank", self.driver.find_element(By.ID, "message9").text)
        email_field.clear()

    def test_NC26(self):
        """End of test: Email must be valid"""
        email_field = self.driver.find_element(By.NAME, "emailid")
        email_field.send_keys("guru99@")
        self.assertIn("Email-ID is not valid", self.driver.find_element(By.ID, "message9").text)
        email_field.clear()

    def test_NC27(self):
        """*** Failed Test - It accepts email id with a space in it ***"""
        email_field = self.driver.find_element(By.NAME, "emailid")
        email_field.send_keys("abc 23@gmail.com")
        self.assertIn("Email-ID is not valid", self.driver.find_element(By.ID, "message9").text)
        email_field.clear()

    def test_NC28(self):
        """End of test: Password cannot be empty"""
        pass_field = self.driver.find_element(By.NAME, "password")
        pass_field.send_keys(Keys.TAB)
        self.assertIn("Password must not be blank", self.driver.find_element(By.ID, "message18").text)
        pass_field.clear()

    # Teardown method - Runs after every testcases
    def tearDown(self):
        print("\n" + self.shortDescription())

    # Teardown class - runs once after all the tests are completed
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()