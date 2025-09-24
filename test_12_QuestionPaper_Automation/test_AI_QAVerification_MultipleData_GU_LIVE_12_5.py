'''
Descriotion:
            Login using CSV File 

            Stream Data is inserting herer from CSV file 
            [AI_QA_CSV_File/Unique_StreamCode_StreamName2.csv]

# Run only one class [TestAutomation]
# Run report also  [--html=report1.html]

pytest -v --html=report1.html -k TestAutomation test_Loging1.py::TestAutomation

pytest test_Loging2.py
pytest -v --html=report1.html -k TestAutomation test_Loging2.py::Tes+tAutomation
pytest -v --html=report1.html -k TestAutomation test_Loging2.py::Tes+tAutomation
pytest -v --html=report1.html -k TestAutomation test_Loging2.py::TestAutomation

pytest -v --html=report1.html -k test_Login_Stream_MoreData.py

pytest test_AI_QA_uniq2.py test_AI_QA_Login_Stream_MoreData.py --html=report3.html

pytest test_AI_QA_Stream_MultipleData_1.py --html=report3.html
pytest test_AI_QAVerification_MultipleData.py --html=report3.html
pytest test_AI_QAVerification_MultipleData_GU_LIVE_12_5.py --html=report1.html
'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        #cls.output_file = "AI_QA_CSV_File_12_QPVerification/3_AI_QA_Frag/2_QPVerification_Approval.csv"  # Added here
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
                    'ExamCycle': row['ExamCycle'], #>>>>>>>>>>>>Code 1
                    'ExamSeries': row['ExamSeries'], #>>>>>>>>>>>>Code 1
                    'SubjectCode': row['SubjectCode'], #>>>>>>>>>>>>Code 1
                    'Template': row['Template'], #>>>>>>>>>>>>Code 1
                    'Test_Report_Data': row['Test_Report_Data'] #>>>>>>>>>>>>Code 1
                })
        return stream_data_list
    
    # def wait_for_element(self, by, value, timeout=10):
    #         """Wait for an element to be visible."""
    #         return WebDriverWait(self.driver, timeout).until(
    #             EC.visibility_of_element_located((by, value))
    #         )

    def test_login(self):
        """Tests login functionality."""
        self.read_credentials('AI_QA_CSV_File_12_QPVerification/3_AI_QA_Frag/useridpw.csv')# user id password file name should be here
        self.driver.get("https://gung.intelliexams.com/auth/login") # application user for testing 
        time.sleep(3)
        
        userid_field = self.driver.find_element(By.NAME, 'email')
        userid_field.send_keys(self.userid)
        time.sleep(1)

        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(self.password)
        time.sleep(1)

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/form/div[3]/div[1]/button")
        login_button.click()
        time.sleep(5)
        #assert "Dashboard" in self.driver.title
        print("Login Successful")

    # def test_confirm_login(self):
    #     """Clicks the confirmation button after login."""   #/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]
    #     confirm_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]')
    #     confirm_button.click()
    #     print("Confirmation Successful")
    #     time.sleep(5)

######################################################################################
    def test_QP_Verification(self):
        """Adds multiple streams using CSV data."""
        stream_data_list = self.read_stream_data('AI_QA_CSV_File_12_QPVerification/3_AI_QA_Frag/2_QPVerification_Approval.csv')
        
        #response_status=[]
        for index,stream_data in enumerate(stream_data_list):   #>>>>>>>enumerate() used
            print('stream_data------->',stream_data,index)

            self.ExamCycle = stream_data['ExamCycle']   #>>>>>>>>>>>>Code 2
            self.ExamSeries = stream_data['ExamSeries']   #>>>>>>>>>>>>Name 2
            self.SubjectCode = stream_data['SubjectCode']   #>>>>>>>>>>>>Code 2
            self.Template = stream_data['Template']   #>>>>>>>>>>>>Name 2
            self.Test_Report_Data = stream_data['Test_Report_Data']   #>>>>>>>>>>>>Name 2

            # Main Menu
            stream_menu = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/a/span')
            stream_menu.click()
            time.sleep(2)
            
            # Sub menu
            stream_sub_menu = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/ul/li[3]/a/span')
            stream_sub_menu.click()
            time.sleep(5)
            
            # 1 Exam Cycle Dropdown field data enter
            stream_name_field = self.driver.find_element(By.NAME, 'examcycle_id')
            stream_name_field.click()
            stream_name_field.send_keys(self.ExamCycle)
            # 1 Exam Cycle Dropdown menu clicked
            stream_name_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[2]/div/div/div[2]/div/div[2]/div[1]')
            stream_name_field.click()
            time.sleep(3)
            print("1) Exam cycle dropdown entered and selected")


            # 2 Exam Series Dropdown field data enter
            stream_name_field2 = self.driver.find_element(By.NAME, 'examseries_id')
            stream_name_field2.click()
            stream_name_field2.send_keys(self.ExamSeries)
            # 2 Exam Series Dropdown menu clicked
            stream_name_field2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[3]/div/div[2]/div/div[2]/div')
            stream_name_field2.click()
            #time.sleep(1)
            print("2) Exam Series dropdown entered and selected")

            # 3 Subject Code field data enter
            stream_name_field3 = self.driver.find_element(By.NAME, 'subject_code')
            stream_name_field3.click()
            stream_name_field3.send_keys(self.SubjectCode)
            time.sleep(4)
            print("3) Subject Code dropdown entered and selected")
            
            # 4 Template Name Dropdown field data enter
            stream_name_field4 = self.driver.find_element(By.NAME, 'Templateid')
            stream_name_field4.click()
            stream_name_field4.send_keys(self.Template)
            wait = WebDriverWait(self.driver, 10)
            stream_name_field4 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[5]/div/div[2]/div/div[2]/div')
            stream_name_field4.click()
            time.sleep(5)
            print("4) Template Name dropdown entered and selected")

            # 1. Start Processing QP Button click
            stream_name_field_FragButton1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[6]/div/div/button')
            stream_name_field_FragButton1.click()
            time.sleep(2)

            # Scroll down 2000 pixels using JavaScript
            #driver.execute_script("window.scrollBy(0, 500);")  # Scroll down 500 pixels
            window_size=2000  #declar the variable called window_size to scroll down window
            self.driver.execute_script(f"window.scrollBy(0, {window_size});")  # Scroll down 500 pixels
            time.sleep(3)
            ###########################################################################
            # Verify_Button
            Verify_Button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[4]/div/div/button')
            Verify_Button.click()
            time.sleep(2)

            # Popup_Box_OK_Button
            Popup_Box_OK_Button = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[3]/button')
            Popup_Box_OK_Button.click()
            time.sleep(2)

########################################################################## WRITE To CSV File    / CSV File Report Writeing
        #     output_file = "AI_QA_CSV_File_12_QPVerification/3_AI_QA_Frag/2_QPVerification_Approval.csv"
        #     approve_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[5]/div/div/button[1]')
        #     message = "Button is Enabled" if approve_button.is_enabled() else "Button is Not-enabled"
            
        #     if approve_button.is_enabled():
        #         approve_button.click() #variable called
        #     else:
        #         #self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[1]/div/div[1]/div/button").click()
        #         self.back_button()  #function called
        #     time.sleep(2)

        #     stream_data_list[index]['Test_Report_Data'] = message

        # with open(self.output_file, mode="w", newline="", encoding="utf-8") as file:
        #     fieldnames = stream_data_list[0].keys()
        #     writer = csv.DictWriter(file, fieldnames=fieldnames)
        #     writer.writeheader()
        #     writer.writerows(stream_data_list)
        # print("Verification Completed and Results Saved")
####################################################################################################

########################################################################To Both READ & WRITE report in CSV file
            output_file = "AI_QA_CSV_File_12_QPVerification/3_AI_QA_Frag/2_QPVerification_Approval.csv"
            Approve_Button_Is_Enable_Or_Not = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[5]/div/div/button[1]')

            if Approve_Button_Is_Enable_Or_Not.is_enabled():
                print("Button is enabled ........11............")
                message = "Approved Successfully"
                self.approve_button()  #Add button function Called

            else:
                print("Button is not enabled ........22............")
                message = "Not-Approved-Error"
                self.back_button()

            rows = []
            print('thisis data row-0-0-9--rowa-datata',rows)
            with open(output_file, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                print('this is reader---123',reader)
                for index_d,row in enumerate(reader):
                    print('message--->',message,row,index_d,index)
                    if index_d==index:
                        row['Test_Report_Data'] = message
                    rows.append(row)
            print('')

            with open(output_file, mode="w", newline="", encoding="utf-8") as file:
                fieldnames = ['ExamCycle', 'ExamSeries', 'SubjectCode', 'Template', 'Test_Report_Data']  # Include all column names
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()  # Write the header
                print('rows---',rows)
                writer.writerows(rows)  # Write the updated rows
            #print(f"Message written to {output_file}")
##################################################################################################
    def approve_button(self):
        # Approve_Button
        Approve_Button1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[5]/div/div/button[1]')
        Approve_Button1.click()
        time.sleep(2)

    def back_button(self):
        # Back button clicked
        Back_Button2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[1]/div/div[1]/div/button')
        Back_Button2.click()
        time.sleep(2)
####################################################################################################
