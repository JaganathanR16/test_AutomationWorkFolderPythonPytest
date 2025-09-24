'''
Descriotion: To Question Paper Approve code.
            Login using CSV File [AI_QA_CSV_File/Unique_StreamCode_StreamName2.csv]
# Run only one class [TestAutomation]
# Run report also  [--html=report1.html]

pytest test_AI_QA_QPFrag_Approval_GU_LIVE_12_5.py
pytest test_AI_QA_QPFrag_Approval_GU_LIVE_12_5_V1.py --html=report3.html
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
from selenium.webdriver.common.keys import Keys

import os
import winsound
from playsound import playsound
import platform

import pygame
import time

#Word to Sound mp3
import pygame
import time
from gtts import gTTS
#from playsound import playsound  # Import this to play audio

class TestAutomation:
    # @classmethod is a decorator
    @classmethod
    def setup_class(cls):
        """Setup method to initialize the browser"""
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.userid = ""
        cls.password = ""
        cls.stream_code = ""
        cls.stream_name = ""
        cls.output_file = "D:\QA_Automation_Document/2_QPVerification_Approval.csv"  # Added here
        cls.login_file = "D:\QA_Automation_Document/useridpw.csv"  # CSV File Added here
        #stream_data_list = self.read_stream_data('1_AI_QA_MasterData_CSV/3_AI_QA_Frag/2_QPVerification_Approval.csv')  ##........>>>>>
        #stream_data_list = self.read_stream_data('D:\QA_Automation_Document/2_QPVerification_Approval.csv')  ##........>>>>>11
        print("Browser Launched Successfully")

    @classmethod
    def teardown_class(cls):
        """To Sound Function call and call driver quit function"""

        #cls.QA_test_Sound_Effect()        #Function used to play mp3 , below this function is written
        #cls.test_words_to_speech_sound()   #Words to soud mp3 words
        
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
                    #'Template': row['ExamSeries'] + " (" + row['SubjectCode'] + ")",   #>>>>>>>>>>>>Code 1  Mearge two row
                    'Test_Report_Data': row['Test_Report_Data'] #>>>>>>>>>>>>Code 1
                })
        return stream_data_list

    def test_login(self):
        """Tests login functionality."""
        self.read_credentials(self.login_file)           # user id password file name should be here
        self.driver.get("https://gung.intelliexams.com") # application user for testing 
        time.sleep(2)
        
        userid_field = self.driver.find_element(By.NAME, 'email')
        userid_field.send_keys(self.userid)
        time.sleep(1)

        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(self.password)
        time.sleep(2)

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/form/div[3]/div[1]/button")
        login_button.click()
        time.sleep(4)  #10
        #assert "Dashboard" in self.driver.title
        print("Login Successful")


    def test_menu_click(self):
        # Main Menu click
        stream_menu = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/a/span')
        stream_menu.click()
        time.sleep(3)
        
        # Sub menu click
        stream_sub_menu = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/ul/li[3]/a/span')
        stream_sub_menu.click()
        time.sleep(3)  #5
        
######################################################################################
    def test_QP_Verification(self):
        """Adds multiple streams using CSV data."""
        stream_data_list = self.read_stream_data('D:\QA_Automation_Document/2_QPVerification_Approval.csv')  ##........>>>>>
        #output_file = "1_AI_QA_MasterData_CSV/3_AI_QA_Frag/2_QPVerification_Approval.csv"
        #stream_data_list = self.read_stream_data('AI_QA_CSV_File_12_QPVerification/3_AI_QA_Frag/2_QPVerification_Approval.csv')
        
        for index,stream_data in enumerate(stream_data_list):
            print('stream_data------->',stream_data,index)
            
            self.ExamCycle = stream_data['ExamCycle']   #>>>>>>>>>>>>Code 2
            self.ExamSeries = stream_data['ExamSeries']   #>>>>>>>>>>>>Name 2
            self.SubjectCode = stream_data['SubjectCode']   #>>>>>>>>>>>>Code 2
            self.Template = stream_data['Template']   #>>>>>>>>>>>>Name 2
            self.Test_Report_Data = stream_data['Test_Report_Data']   #>>>>>>>>>>>>Name 2
            
            # 1 Exam Cycle Dropdown field data enter
            stream_name_field = self.driver.find_element(By.NAME, 'examcycle_id')
            stream_name_field.click()

            # Use JavaScript to clear the field
            self.driver.execute_script("""
                let field = arguments[0];
                field.value = '';
                field.dispatchEvent(new Event('input'));
                field.dispatchEvent(new Event('change'));
            """, stream_name_field)

            stream_name_field.send_keys(self.ExamCycle)
            stream_name_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[2]/div/div/div[2]/div/div[2]/div[1]')
            stream_name_field.click()
            time.sleep(1)  #3
            print("1) Exam cycle dropdown entered and selected")
#------------------------------------------------------------
            # 2 Exam Series Dropdown field data enter
            # Click the Exam Series Dropdown field
            dropdown_field = self.driver.find_element(By.NAME, 'examseries_id')
            dropdown_field.click()
            dropdown_field.send_keys(self.ExamSeries)
            time.sleep(1)
            # Wait for dropdown options and click exact match
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//div[text()='{self.ExamSeries}']"))
            ).click()
            #time.sleep(1)
#-------000--------------------------------------------------------------------------------
            # 3 Subject Code field data enter
            stream_name_field3 = self.driver.find_element(By.NAME, 'subject_code')
            stream_name_field3.click()
            stream_name_field3.send_keys(self.SubjectCode)
            time.sleep(2)
            print("3) Subject Code dropdown entered and selected")
            
            # 4 Template Name Dropdown field data enter
            stream_name_field4 = self.driver.find_element(By.NAME, 'Templateid')
            stream_name_field4.click()
            stream_name_field4.send_keys(self.Template)
            time.sleep(2)  
            wait = WebDriverWait(self.driver, 10)
            stream_name_field4 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[5]/div/div[2]/div/div[2]/div')
            stream_name_field4.click()
            time.sleep(2)  #5
            print("4) Template Name dropdown entered and selected")

# For loop to execute multiple time when grid button is not loading
            #for attempt in range(3):  # Try 5 times
            for attempt in range(2):  # Try 5 times
                buttons = self.driver.find_elements("xpath", "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[6]/div/div/button")
                
                if buttons:
                    print(f"Button is present.......Attempt {attempt + 1}")
                    break
                else:
                    print(f"Button is not present...4444444444444....Attempt {attempt + 1}")
                    #continue
                    #time.sleep(2)  # Wait before trying again

            
                    # 1 Exam Cycle Dropdown field data enter
                    stream_name_field = self.driver.find_element(By.NAME, 'examcycle_id')
                    stream_name_field.click()

                    # Use JavaScript to clear the field
                    self.driver.execute_script("""
                        let field = arguments[0];
                        field.value = '';
                        field.dispatchEvent(new Event('input'));
                        field.dispatchEvent(new Event('change'));
                    """, stream_name_field)

                    #stream_name_field.clear()

                    stream_name_field.send_keys(self.ExamCycle)
                    stream_name_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[2]/div/div/div[2]/div/div[2]/div[1]')
                    stream_name_field.click()
                    time.sleep(2)  #3
                    print("1) Exam cycle dropdown entered and selected")
                    #------------111----------------------------------------------
                    # 2 Exam Series Dropdown field data enter
                    # Click the dropdown
                    dropdown_field = self.driver.find_element(By.NAME, 'examseries_id')
                    dropdown_field.click()
                    dropdown_field.send_keys(self.ExamSeries)
                    time.sleep(1)
                    # Wait for dropdown options and click exact match
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"//div[text()='{self.ExamSeries}']"))
                    ).click()
                    #------------111-----------------------------------------------
                    # 3 Subject Code field data enter
                    stream_name_field3 = self.driver.find_element(By.NAME, 'subject_code')
                    stream_name_field3.click()
                    stream_name_field3.send_keys(self.SubjectCode)
                    time.sleep(2)
                    print("3) Subject Code dropdown entered and selected")
                    
                    # 4 Template Name Dropdown field data enter
                    stream_name_field4 = self.driver.find_element(By.NAME, 'Templateid')
                    stream_name_field4.click()
                    stream_name_field4.send_keys(self.Template)
                    time.sleep(1)  
                    wait = WebDriverWait(self.driver, 10)
                    stream_name_field4 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[5]/div/div[2]/div/div[2]/div')
                    stream_name_field4.click()
                    time.sleep(3)  #5
                    print("4) Template Name dropdown entered and selected") 

                    # To check button grid is present or not if not then writ Not-Approved-Error"
                    buttons2 = self.driver.find_elements("xpath", "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[6]/div/div/button")
                    if buttons2:
                        print(f"Button is present.......Attempt {attempt + 1}")
                        continue
                    else:
                        message1 = "Not-Approved-Error"
                        stream_data_list[index]['Test_Report_Data'] = message1
                        print("7777777777777777777777777" , stream_data_list)

                        with open(self.output_file, mode="w", newline="", encoding="utf-8") as file:
                            fieldnames = stream_data_list[0].keys()
                            writer = csv.DictWriter(file, fieldnames=fieldnames)
                            writer.writeheader()
                            writer.writerows(stream_data_list)
                        print("Button not available ERROR message Not-Approved-Error")
                        
#########################################################################
            # 1. Start Processing QP Button click
            stream_name_field_FragButton1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[6]/div/div/button')
            stream_name_field_FragButton1.click()
            time.sleep(1)

            # Scroll Down using JavaScript
            # driver.execute_script("window.scrollBy(0, 500);")  # Scroll down 500 pixels
            # Scroll Down by Pixel # Scroll down 500 pixels
            # window_size+=50

            window_size=5000  #declar the variable called window_size to scroll down window
            self.driver.execute_script(f"window.scrollBy(0, {window_size});")  # Scroll down 500 pixels
            time.sleep(2)

            # #Scroll Up using Java Script
            # window_size = 5000  # Declare the variable called window_size to scroll up
            # self.driver.execute_script(f"window.scrollBy(0, -{window_size});")  # Scroll up by 5000 pixels
            # time.sleep(3)
            ###########################################################################
            
            # Verify_Button Clicked
            Verify_Button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[4]/div/div/button')
            Verify_Button.click()
            time.sleep(1)

            # Popup_Box_OK_Button Clicked
            Popup_Box_OK_Button = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[3]/button')
            Popup_Box_OK_Button.click()
            time.sleep(1)

########################################################################## CSV File Report and Writeing
            approve_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[5]/div/div/button[1]')
            
            message = "QPFragmentation Approved Successfully" if approve_button.is_enabled() else "Not-Approved-Error"
            
            if approve_button.is_enabled():
                approve_button.click() #variable called
                time.sleep(2)
            else:
                #Scroll Up using Java Script
                window_size = 5000  # Declare the variable called window_size to scroll up
                self.driver.execute_script(f"window.scrollBy(0, -{window_size});")  # Scroll up by 5000 pixels
                time.sleep(2)
                self.back_button()  #back_button() Function called
            time.sleep(1)

            stream_data_list[index]['Test_Report_Data'] = message
            
            print("55555555555555555555" , stream_data_list)

            with open(self.output_file, mode="w", newline="", encoding="utf-8") as file:
                fieldnames = stream_data_list[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(stream_data_list)
            print("Verification Completed and Results Saved")

            #continue
####################################################################################################

    def approve_button(self):
        # Approve_Button
        Approve_Button1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[5]/div/div/button[1]')
        Approve_Button1.click()
        time.sleep(1)

    def back_button(self):
        # Back button clicked
        Back_Button2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[1]/div/div[1]/div/button')
        Back_Button2.click()
        time.sleep(1)
####################################################################################################


