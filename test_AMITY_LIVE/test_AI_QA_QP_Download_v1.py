'''
pytest test1.py --html=report1.html
pytest AMITYDownload.py
pytest AmityDownload2.py
pytest test_AI_QA_QP_Download.py

'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys  # Tab key
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


from pywinauto import Desktop
from pywinauto import Application, Desktop
import time


from pywinauto.application import Application
from pywinauto import Application

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAutomation:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.userid = ""
        cls.password = ""
        cls.ExamCycle=""
        cls.ExamSeries=""
        cls.SubjectCode=""
        cls.Template=""       
        print("Browser Launched Successfully")

    # @classmethod
    # def teardown_class(cls):
    #     cls.driver.quit()
    #     print("Browser Closed Successfully")

    ####################################################################
    def read_credentials(self, file_path):
        """Reads credentials from CSV file."""
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                self.userid = row['UserID']
                self.password = row['Password']
                break

    #Login Page
    def test_login(self):
        """Tests login functionality."""
        self.read_credentials('1_AI_QA_MasterData_CSV/useridpw2.csv')# user id password file name should be here
        self.driver.get("https://amizone.net/adminamizone/index.aspx") # application user for testing 
        time.sleep(3)
        
        userID_field = self.driver.find_element(By.NAME, 'txtUser_name')
        userID_field.send_keys(self.userid)
        time.sleep(1)

        userPW_field = self.driver.find_element(By.NAME, 'txtPass_word')
        userPW_field.send_keys(self.password)
        time.sleep(10)

        login_button = self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/center/input")
        login_button.click()
        time.sleep(3)
        #assert "Dashboard" in self.driver.title
        print("Login Successful")

        ####################################################################
        #self.driver.switch_to.default_content()   # always reset before switching
        self.driver.switch_to.frame(2)            # change index/name based on your HTML
        message_popup_close = self.driver.find_element(By.XPATH, "/html/body/form/div[41]/div/div/div[1]/button")
        message_popup_close.click()
        time.sleep(1)
        print("message_popup_close Successful")
        ####################################################################


        ##################################  Switched to Fram 1
        self.driver.switch_to.default_content() 
        self.driver.switch_to.frame(1)
        ##################################
        plusbutton_1 = self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div/table/tbody/tr/td[1]/a/img")
        plusbutton_1.click()
        time.sleep(1)
        #assert "Dashboard" in self.driver.title
        print("plusbutton_1 Clicked Successful")

        plusbutton_2 = self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div/table[1]/tbody/tr/td[2]/a/img")
        plusbutton_2.click()
        time.sleep(1)
        #assert "Dashboard" in self.driver.title
        print("plusbutton_2 Clicked Successful")

        plusbutton_3 = self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div/div/table/tbody/tr/td[3]/a/img")
        plusbutton_3.click()
        time.sleep(1)
        #assert "Dashboard" in self.driver.title
        print("plusbutton_3 Clicked Successful")

        plusbutton_4 = self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div/div/div/table/tbody/tr/td[4]/a/img")
        plusbutton_4.click()
        time.sleep(1)
        #assert "Dashboard" in self.driver.title
        print("plusbutton_4 Clicked Successful")

        print_QP_5 = self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div/div/div/div/table/tbody/tr/td[6]/a")
        print_QP_5.click()
        time.sleep(2)
        print("print_QP_5 Clicked Successful")
        ##################################
        #######################################################################################################################################
        # Switch to correct frame (example: frame index 2 or name 'main')
        self.driver.switch_to.default_content()   # always reset before switching
        self.driver.switch_to.frame(2)            # change index/name based on your HTML

        # Locate and select dropdown
        dropdown_element = self.driver.find_element(By.ID, "ddlExam")
        select = Select(dropdown_element)
        select.select_by_visible_text(
            "2025 / Even-AUUP: Special Supplementary Examination, August 2025 (for the courses of Odd and Even Semesters)"
        )
        time.sleep(2)
        #######################################################################################################################################
        fromDate_field = self.driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/table/tbody/tr[2]/td[3]/input')
        fromDate_field.click()
        fromDate_field.send_keys("20/08/2025")
        fromDate_field.send_keys(Keys.ENTER)
        time.sleep(2)

        toDate_field = self.driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/table/tbody/tr[3]/td[3]/input')
        toDate_field.clear()
        toDate_field.send_keys("20/08/2025")
        toDate_field.send_keys(Keys.ENTER)
        time.sleep(2)

        View_Button_Click1 = self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div[2]/table/tbody/tr[6]/td[3]/input[1]")
        View_Button_Click1.click()
        print("View_Button_Click1 Clicked Successful")
        time.sleep(5)

        ##############################################################################################################################
        rows = self.driver.find_elements(By.XPATH, "//tr[td[contains(., 'CSIT246')]]")

        for row in rows:
            if "CSIT246" in row.text:
                checkbox = row.find_element(By.XPATH, ".//input[@type='checkbox']")
                checkbox.click()
                print("Selected checkbox for:", row.text)
                break
        time.sleep(3)
        ##############################################################################################################################
        Print_Button_Click2 = self.driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div[2]/table/tbody/tr[6]/td[3]/input[2]")
        Print_Button_Click2.click()
        print("Print_Button_Click2 Clicked Successful 11")
        time.sleep(5)
        ##############################################################################################################################

        # Sysem window Pring

        # ---------------------------
        # Helper Functions
        # ---------------------------
        def get_window(title_regex, backend="uia", wait_time=10):
            """Attach to a window by title regex."""
            app = Application(backend=backend).connect(title_re=title_regex)
            win = app.window(title_re=title_regex)
            win.wait("visible", timeout=wait_time)
            return win

        def locate_and_click(win, title=None, auto_id=None, control_type=None):
            """Locate an element in a system window and click it."""
            elem = win.child_window(title=title, auto_id=auto_id, control_type=control_type)
            elem.wait("visible", timeout=5)
            elem.click_input()
            return elem

        def locate_and_type(win, text, title=None, auto_id=None, control_type=None):
            """Locate an element in a system window and type text into it."""
            elem = win.child_window(title=title, auto_id=auto_id, control_type=control_type)
            elem.wait("visible", timeout=5)
            elem.set_edit_text(text)
            return elem


        # ---------------------------
        # Main Automation Flow
        # ---------------------------
        # 1. Launch browser
        service = Service("chromedriver.exe")   # adjust path to your chromedriver
        driver = webdriver.Chrome(service=service)

        driver.get("https://example.com")  # replace with your page URL
        time.sleep(2)

        # 2. Scroll down webpage
        window_size = 5000
        driver.execute_script(f"window.scrollBy(0, {window_size});")
        print("Step 1: Page scrolled")
        time.sleep(2)

        # 3. Click the webpage Print button
        Print_Button_3 = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/button")
        Print_Button_3.click()
        print("Step 2: Web Print button clicked")

        time.sleep(3)  # wait for system Print dialog to appear

        # 4. Attach to the Print dialog
        dlg = get_window(".*Print.*")
        dlg.print_control_identifiers()  # <-- debug: see available controls

        # 5. Select Destination → Save as PDF
        try:
            locate_and_click(dlg, control_type="ComboBox")   # click destination dropdown
            time.sleep(1)
            dlg.type_keys("Save as PDF{ENTER}")              # select Save as PDF
            print("Step 3: Destination set to Save as PDF")
        except Exception as e:
            print(f"⚠ Could not set destination: {e}")

        # 6. Click Print button
        locate_and_click(dlg, title="Print", control_type="Button")
        print("Step 4: Print button clicked")

        time.sleep(2)  # wait for Save As dialog

        # 7. Handle Save As dialog
        save_dlg = get_window(".*Save.*")
        save_dlg.print_control_identifiers()  # <-- debug: check available controls

        locate_and_type(save_dlg, r"D:\Images\test11.pdf", auto_id="1001", control_type="Edit")
        locate_and_click(save_dlg, title="Save", control_type="Button")

        print("✅ Step 5: File saved successfully at D:\\Images\\test11.pdf")

        # 8. Close browser
        driver.quit()


