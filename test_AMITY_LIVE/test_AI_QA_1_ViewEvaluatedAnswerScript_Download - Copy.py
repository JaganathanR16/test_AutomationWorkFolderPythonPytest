'''
Descriotion:
            Login using CSV File 

            Stream Data is inserting herer from CSV file 
            [AI_QA_CSV_File/Unique_StreamCode_StreamName2.csv]

# Run only one class [TestAutomation]
# Run report also  [--html=report1.html]

pytest test_Loging2.py
pytest -v --html=report1.html -k TestAutomation test_Loging2.py::TestAutomation

pytest -v --html=report1.html -k test_Login_Stream_MoreData.py
pytest test_AI_QA_uniq2.py test_AI_QA_Login_Stream_MoreData.py --html=report3.html

pytest test_AI_QA_1_ViewEvaluatedAnswerScript_Download.py --html=report1.html

'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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
        cls.output_file = "1_AI_QA_MasterData_CSV/1_ViewEvaluatedAnswerScript_Download/1_ViewEvaluatedAS_Download.csv"  # Added here
        cls.login_file = "1_AI_QA_MasterData_CSV/1_ViewEvaluatedAnswerScript_Download/useridpw.csv"  # CSV File Added here
        print("Browser Launched Successfully")

    @classmethod
    def teardown_class(cls):
        """Teardown method to close the browser"""
        cls.driver.quit()
        print("Browser Closed Successfully")

        # setup_class() runs before all tests in the class.
        # teardown_class() runs after all tests in the class.
    #########################################################################
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
                stream_data_list.append({    # ExamSeries  EnterUSN SubjectCode Subject  
                    
                    #'ExamSeries': row['ExamSeries'], #>>>>>>>>>>>>Code 1
                    'EnterUSN': row['EnterUSN'], #>>>>>>>>>>>>Code 1
                    'SubjectCode': row['SubjectCode']        , #>>>>>>>>>>>>Code 1
                    'Test_Report_Data': row['Test_Report_Data'] #>>>>>>>>>>>>Code 1

                })
        return stream_data_list

    def test_login(self):
        """Tests login functionality."""
        self.read_credentials(self.login_file)# user id password file name should be here
        self.driver.get("https://amityng.intelliexams.com/auth/login") # application user for testing 
        time.sleep(1)
        
        userid_field = self.driver.find_element(By.NAME, 'email')
        userid_field.send_keys(self.userid)
        time.sleep(1)

        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(self.password)
        time.sleep(1)

        login_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/form/div[3]/div[1]/button')
        login_button.click()
        time.sleep(2)
        #assert "Dashboard" in self.driver.title
        print("Login Successful")

    def test_confirm_login(self):
        """Clicks the confirmation button after login."""   #/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]
        confirm_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]')
        confirm_button.click()
        print("Confirmation Successful")
        time.sleep(2)

    def test_main_sub_menu(self):
        # Main Menu
        time.sleep(1)
        stream_menu = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[5]/a/span')
        stream_menu.click()
        time.sleep(1)
        
        # Sub menu
        stream_sub_menu = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[5]/ul/li[1]/a/span')
        stream_sub_menu.click()
        time.sleep(2)

        # Exam Menu
        # Locate the dropdown element
        examSeries_menu = self.driver.find_element(By.NAME, 'examseries_id')
        dropdown = Select(examSeries_menu)
        if len(dropdown.options) > 1:
            dropdown.select_by_index(1)  # Selects the second option
            print("Successfully selected the second dropdown option:", dropdown.options[1].text)
        else:
            print("Dropdown does not have enough options to select the second element.")
            

######################################################################################
    def test_QP_Verification(self):
        """Adds multiple streams using CSV data."""
        stream_data_list = self.read_stream_data('1_AI_QA_MasterData_CSV/1_ViewEvaluatedAnswerScript_Download/1_ViewEvaluatedAS_Download.csv')  ##........>>>>>

        for index,stream_data in enumerate(stream_data_list):
            print('stream_data------->',stream_data,index)

            #self.ExamSeries = stream_data['ExamSeries']   #>>>>>>>>>>>>Name 2
            self.EnterUSN = stream_data['EnterUSN']   #>>>>>>>>>>>>Code 2
            self.SubjectCode = stream_data['SubjectCode']   #>>>>>>>>>>>>Code 2
            self.Test_Report_Data = stream_data['Test_Report_Data']   #>>>>>>>>>>>>Name 2

            # # 1 Exam Series Dropdown field data enter
            # stream_name_field = self.driver.find_element(By.NAME, 'examseries_id')
            # stream_name_field.click()
            # stream_name_field.send_keys(self.ExamSeries)
            # stream_name_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]/select')
            # stream_name_field.click()
            # time.sleep(1)
            # print("1) Exam Series dropdown selected Successfully .........")
            # print("1) Exam Series dropdown Entered is : ......... ", self.ExamSeries)
            # print("EEEEEExam series........1111111.....", self.ExamSeries)
            # self.exam_series2 = self.ExamSeries
            # print("EEEEEExam series........22222.....", self.exam_series2)

            # 2) USN Text box entry
            stream_name_field3 = self.driver.find_element(By.NAME, 'USN')
            stream_name_field3.clear()
            time.sleep(2)
            stream_name_field3.click()
            stream_name_field3.send_keys(self.EnterUSN)
            time.sleep(3)
            print("2) USN Text Box Entry Successfully .........")
            print("2) Subject Name Text box enter is : ......... ", self.SubjectCode)

            # 3) Subject_dropdown Dropdown field data enter
            time.sleep(3)
            subject_dropdown_element = self.driver.find_element(By.NAME, 'subject_id')
            subject_dropdown_element.click()

            dropdown = Select(subject_dropdown_element)
            if len(dropdown.options) > 1:
                subject_dropdown_element.send_keys(self.SubjectCode)
                subject_dropdown_element.click()
                time.sleep(3)
                print("3) Subject_dropdown Enter is : ......... ", self.SubjectCode)
                
            else:
                print("Dropdown not fully loaded or contains insufficient options")
    
            # 1. View Button click
            View_Button_1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[4]/div/div[2]/div/button')
            View_Button_1.click()
            time.sleep(12)

            downloadPDF_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[4]/div/div[2]/div/button[2]')

            message = "View Evaluated Answer Script Downloaded Successfully" if downloadPDF_button.is_enabled() else "Not-Downloaded-Error"
            
            if downloadPDF_button.is_enabled():
                downloadPDF_button.click()
                time.sleep(10)

            else:
                # Sub menu 2nd time
                stream_sub_menu = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[5]/ul/li[1]/a/span')
                #self.back_button()  #function called
            time.sleep(5)

            stream_data_list[index]['Test_Report_Data'] = message
            

        with open(self.output_file, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = stream_data_list[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(stream_data_list)
        print("Download Completed and Results Saved")

        



