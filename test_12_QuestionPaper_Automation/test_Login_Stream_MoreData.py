'''
# Run only one class [TestAutomation]
# Run report also  [--html=report1.html]

pytest -v --html=report1.html -k TestAutomation test_Loging1.py::TestAutomation

pytest test_Loging2.py
pytest -v --html=report1.html -k TestAutomation test_Loging2.py::Tes+tAutomation
pytest -v --html=report1.html -k TestAutomation test_Loging2.py::Tes+tAutomation
pytest -v --html=report1.html -k TestAutomation test_Loging2.py::TestAutomation

pytest -v --html=report1.html -k TestAutomation test_Login_Stream_MoreData.py::TestAutomation
'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

class TestAutomation:
    @classmethod
    def setup_class(cls):
        """Setup method to initialize the browser"""
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.userid = ""
        cls.password = ""
        cls.stream_code = ""
        cls.stream_name = ""
        print("Browser Launched Successfully")

    @classmethod
    def teardown_class(cls):
        """Teardown method to close the browser"""
        cls.driver.quit()
        print("Browser Closed Successfully")

        # setup_class() runs before all tests in the class.
        # teardown_class() runs after all tests in the class.

    def read_credentials(self, file_path):
        """Reads credentials from CSV file."""
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                self.userid = row['UserID']
                self.password = row['Password']
                break




    def read_stream_data(self, file_path):
        """Reads multiple stream data from CSV file."""
        stream_data_list = []
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                stream_data_list.append({
                    'CodeId': row['CodeId'],
                    'Name': row['Name']
                })
        return stream_data_list
    

    # def wait_for_element(self, by, value, timeout=10):
    #         """Wait for an element to be visible."""
    #         return WebDriverWait(self.driver, timeout).until(
    #             EC.visibility_of_element_located((by, value))
    #         )

    def test_login(self):
        """Tests login functionality."""
        self.read_credentials('useridpw.csv')# user id password file name should be here
        self.driver.get("http://172.25.8.162") # application user for testing 
        time.sleep(2)
        
        userid_field = self.driver.find_element(By.NAME, 'email')
        userid_field.send_keys(self.userid)
        time.sleep(1)

        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(self.password)
        time.sleep(3)

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/form/div[3]/div[1]/button")
        login_button.click()
        time.sleep(3)
        #assert "Dashboard" in self.driver.title
        print("Login Successful")

    def test_confirm_login(self):
        """Clicks the confirmation button after login."""
        confirm_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]')
        confirm_button.click()
        print("Confirmation Successful")
        time.sleep(5)

    def test_add_stream(self):
        """Adds multiple streams using CSV data."""
        stream_data_list = self.read_stream_data('stream.csv')
        
        for stream_data in stream_data_list:
            self.stream_code = stream_data['CodeId']
            self.stream_name = stream_data['Name']
            
            # Navigate to the Stream menu
            stream_menu = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/ul/li[1]/a/span')
            stream_menu.click()
            time.sleep(2)
            
            # Click the Add button
            add_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/header/div/div/div[2]/a')
            add_button.click()
            time.sleep(5)
            
            # Enter stream details
            stream_code_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[2]/div/div[2]/input')
            stream_code_field.send_keys(self.stream_code)
            time.sleep(2)
            
            stream_name_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[3]/div/div[2]/input')
            stream_name_field.send_keys(self.stream_name)
            time.sleep(2)
            
            # Try to submit the stream
            try:
                submit_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[4]/div/div/div/div/button')
                submit_button.click()
                time.sleep(4)
                print(f"Stream {self.stream_code} - {self.stream_name} Added Successfully")
            except Exception as e:
                print(f"Error: {e}")
