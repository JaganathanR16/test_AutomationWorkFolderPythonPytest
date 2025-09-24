'''
pytest test1.py --html=report1.html
pytest AMITYDownload.py
pytest AmityDownload2.py
pytest test_AI_QA_QP_Download_V3.py
'''

import pytest
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pywinauto.application import Application
import pywinauto

from pywinauto import Application, findwindows
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

import pyautogui, time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import pytest
import time
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestAutomation:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.userid = ""
        cls.password = ""
        print("✅ Browser Launched Successfully")

    @classmethod
    def teardown_class(cls):
        #cls.driver.quit()
        print("✅ Browser Closed Successfully")

    def read_credentials(self, file_path):
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                self.userid = row['UserID']
                self.password = row['Password']
                break

    def test_login(self):
        self.read_credentials('1_AI_QA_MasterData_CSV/useridpw2.csv')
        self.driver.get("https://amizone.net/adminamizone/index.aspx")
        time.sleep(3)

        # Login
        self.driver.find_element(By.NAME, 'txtUser_name').send_keys(self.userid)
        self.driver.find_element(By.NAME, 'txtPass_word').send_keys(self.password)
        time.sleep(10)
        self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/center/input").click()
        print("✅ Login Successful")
        time.sleep(3)

        # Handle popup
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.XPATH, "/html/body/form/div[41]/div/div/div[1]/button").click()
        self.driver.switch_to.default_content()
        time.sleep(1)

        # Navigate menus
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div/table/tbody/tr/td[1]/a/img").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div/table[1]/tbody/tr/td[2]/a/img").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div/div/table/tbody/tr/td[3]/a/img").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div/div/div/table/tbody/tr/td[4]/a/img").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div/div/div/div/table/tbody/tr/td[6]/a").click()
        print("✅ Navigation Successful")
        time.sleep(1)

        # Switch to exam frame
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(2)

        # Select Exam Cycle
        dropdown = Select(self.driver.find_element(By.ID, "ddlExam"))
        dropdown.select_by_visible_text(
            "2025 / Even-AUUP: Special Supplementary Examination, August 2025 (for the courses of Odd and Even Semesters)"
        )
        time.sleep(2)

        # Date filter
        self.driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/table/tbody/tr[2]/td[3]/input').send_keys("20/08/2025", Keys.ENTER)
        self.driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/table/tbody/tr[3]/td[3]/input').send_keys("20/08/2025", Keys.ENTER)
        self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div[2]/table/tbody/tr[6]/td[3]/input[1]").click()
        print("✅ Date filter applied")
        time.sleep(5)

        # Select Subject
        rows = self.driver.find_elements(By.XPATH, "//tr[td[contains(., 'CSIT246')]]")
        for row in rows:
            if "CSIT246" in row.text:
                row.find_element(By.XPATH, ".//input[@type='checkbox']").click()
                print("✅ Selected checkbox for:", row.text)
                break

        # Click Print
        self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div[2]/table/tbody/tr[6]/td[3]/input[2]").click()
        print("✅ Print button clicked")
        time.sleep(5)

        ################################################################################################
        # Window scroll down window
        window_size=5000  #declar the variable called window_size to scroll down window
        self.driver.execute_script(f"window.scrollBy(0, {window_size});")  # Scroll down 500 pixels
        time.sleep(3)
        ################################################################################################
        Print_Button_3 = self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/button")
        Print_Button_3.click()
        print("Print_Button_3 Clicked Successful")
        time.sleep(5)
        ##############################################################################################################################
        ##############################################################################################################################
        #self.driver.switch_to.default_content()
        # -----------------------------
        # System Print Dialog Handling
        # -----------------------------

class TestAutomation:
    @classmethod
    def setup_class(cls):
        # ✅ Chrome Options for auto save as PDF
        app_state = {
            "recentDestinations": [
                {"id": "Save as PDF", "origin": "local", "account": ""}
            ],
            "selectedDestinationId": "Save as PDF",
            "version": 2
        }

        prefs = {
            "printing.print_preview_sticky_settings.appState": json.dumps(app_state),
            "savefile.default_directory": r"D:\Images"   # must exist
        }

        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--kiosk-printing")

        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        cls.driver.maximize_window()
        print("✅ Browser Launched Successfully")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        print("✅ Browser Closed Successfully")

    def test_download_pdf(self):
        self.driver.get("https://example.com")  # 👉 put your actual page here
        time.sleep(3)

        # ✅ Trigger print → auto saved as PDF
        self.driver.execute_script("window.print();")
        print("✅ Print triggered, PDF auto saved to D:\\Images")

        time.sleep(5)  # wait to ensure file is saved
