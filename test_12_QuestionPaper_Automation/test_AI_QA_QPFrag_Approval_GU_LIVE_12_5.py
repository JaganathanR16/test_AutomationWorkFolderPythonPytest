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
pytest test_AI_QA_QPFrag_Approval_GU_LIVE_12_5.py --html=report3.html
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
        cls.output_file = "1_AI_QA_MasterData_CSV/3_AI_QA_Frag/2_QPVerification_Approval.csv"  # Added here
        cls.login_file = "1_AI_QA_MasterData_CSV/3_AI_QA_Frag/useridpw.csv"  # CSV File Added here
        #        stream_data_list = self.read_stream_data('1_AI_QA_MasterData_CSV/3_AI_QA_Frag/2_QPVerification_Approval.csv')  ##........>>>>>
        print("Browser Launched Successfully")

    @classmethod
    def teardown_class(cls):
        """Teardown method to close the browser"""
        #cls.test_Sound_Effect()
        
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
        self.read_credentials(self.login_file)# user id password file name should be here
        self.driver.get("https://gung.intelliexams.com") # application user for testing 
        time.sleep(2)
        
        userid_field = self.driver.find_element(By.NAME, 'email')
        userid_field.send_keys(self.userid)
        time.sleep(1)

        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(self.password)
        time.sleep(3)


        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/form/div[3]/div[1]/button")
        login_button.click()
        time.sleep(4)  #10
        #assert "Dashboard" in self.driver.title
        print("Login Successful")

    # def test_confirm_login(self):
    #     """Clicks the confirmation button after login."""   #/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]
    #     confirm_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]')
    #     confirm_button.click()
    #     print("Confirmation Successful")
    #     time.sleep(5)

    def test_menu_click(self):
        # Main Menu
        time.sleep(3)  #5
        stream_menu = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/a/span')
        stream_menu.click()
        time.sleep(2)
        
        # Sub menu
        stream_sub_menu = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/ul/li[3]/a/span')
        stream_sub_menu.click()
        time.sleep(3)  #5
        
######################################################################################
    def test_QP_Verification(self):
        """Adds multiple streams using CSV data."""
        stream_data_list = self.read_stream_data('1_AI_QA_MasterData_CSV/3_AI_QA_Frag/2_QPVerification_Approval.csv')  ##........>>>>>
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
            stream_name_field.send_keys(self.ExamCycle)
            stream_name_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[2]/div/div/div[2]/div/div[2]/div[1]')
            stream_name_field.click()
            time.sleep(3)  #4
            print("1) Exam cycle dropdown entered and selected")

            # 2 Exam Series Dropdown field data enter
            stream_name_field2 = self.driver.find_element(By.NAME, 'examseries_id')
            stream_name_field2.click()
            stream_name_field2.send_keys(self.ExamSeries)
            stream_name_field2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[3]/div/div[2]/div/div[2]/div')
            stream_name_field2.click()
            time.sleep(1)
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
            time.sleep(2)  
            wait = WebDriverWait(self.driver, 10)
            stream_name_field4 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[5]/div/div[2]/div/div[2]/div')
            stream_name_field4.click()
            time.sleep(3)  #5
            print("4) Template Name dropdown entered and selected")

# -----------1 st Time-------------------------------------------------------------------------------1
            buttons = self.driver.find_elements("xpath", "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[6]/div/div/button")

            if buttons:
                print("Button is present................")
            else:
                print("Button is NOT present..................")
            
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
                time.sleep(3)  #4
                print("1) Exam cycle dropdown entered and selected")

                # 2 Exam Series Dropdown field data enter
                stream_name_field2 = self.driver.find_element(By.NAME, 'examseries_id')
                stream_name_field2.click()
                stream_name_field2.send_keys(self.ExamSeries)
                stream_name_field2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[3]/div/div[2]/div/div[2]/div')
                stream_name_field2.click()
                time.sleep(1)
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
                time.sleep(2)  
                wait = WebDriverWait(self.driver, 10)
                stream_name_field4 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[5]/div/div[2]/div/div[2]/div')
                stream_name_field4.click()
                time.sleep(3)  #5
                print("4) Template Name dropdown entered and selected") 
# -----------1 st Time-------------------------------------------------------------------------------1

# -----------2nd Time-------------------------------------------------------------------------------1
            buttons = self.driver.find_elements("xpath", "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[6]/div/div/button")

            if buttons:
                print("Button is present................")
            else:
                print("Button is NOT present..................")
            
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
                time.sleep(3)  #4
                print("1) Exam cycle dropdown entered and selected")

                # 2 Exam Series Dropdown field data enter
                stream_name_field2 = self.driver.find_element(By.NAME, 'examseries_id')
                stream_name_field2.click()
                stream_name_field2.send_keys(self.ExamSeries)
                stream_name_field2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[3]/div/div[2]/div/div[2]/div')
                stream_name_field2.click()
                time.sleep(1)
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
                time.sleep(2)  
                wait = WebDriverWait(self.driver, 10)
                stream_name_field4 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[5]/div/div[2]/div/div[2]/div')
                stream_name_field4.click()
                time.sleep(3)  #5
                print("4) Template Name dropdown entered and selected") 
# -----------2nd Time-------------------------------------------------------------------------------1


# -----------3rd Time-------------------------------------------------------------------------------1
            buttons = self.driver.find_elements("xpath", "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[6]/div/div/button")

            if buttons:
                print("Button is present................")
            else:
                print("Button is NOT present..................")
            
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
                time.sleep(3)  #4
                print("1) Exam cycle dropdown entered and selected")

                # 2 Exam Series Dropdown field data enter
                stream_name_field2 = self.driver.find_element(By.NAME, 'examseries_id')
                stream_name_field2.click()
                stream_name_field2.send_keys(self.ExamSeries)
                stream_name_field2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[3]/div/div[2]/div/div[2]/div')
                stream_name_field2.click()
                time.sleep(1)
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
                time.sleep(2)  
                wait = WebDriverWait(self.driver, 10)
                stream_name_field4 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[5]/div/div[2]/div/div[2]/div')
                stream_name_field4.click()
                time.sleep(3)  #5
                print("4) Template Name dropdown entered and selected") 
# -----------3rd Time-------------------------------------------------------------------------------1

#########################################################################

            # 1. Start Processing QP Button click
            stream_name_field_FragButton1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[6]/div/div/button')
            stream_name_field_FragButton1.click()
            time.sleep(2)

            # Scroll Down using JavaScript
            #driver.execute_script("window.scrollBy(0, 500);")  # Scroll down 500 pixels
            # Scroll Down by Pixel # Scroll down 500 pixels
            # window_size+=50
            window_size=5000  #declar the variable called window_size to scroll down window
            self.driver.execute_script(f"window.scrollBy(0, {window_size});")  # Scroll down 500 pixels
            time.sleep(3)

            # #Scroll Up using Java Script
            # window_size = 5000  # Declare the variable called window_size to scroll up
            # self.driver.execute_script(f"window.scrollBy(0, -{window_size});")  # Scroll up by 5000 pixels
            # time.sleep(3)
            ###########################################################################
            # Verify_Button
            Verify_Button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[4]/div/div/button')
            Verify_Button.click()
            time.sleep(2)

            # Popup_Box_OK_Button
            Popup_Box_OK_Button = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[3]/button')
            Popup_Box_OK_Button.click()
            time.sleep(2)

########################################################################## CSV File Report Writeing
            #output_file = "1_AI_QA_MasterData_CSV/3_AI_QA_Frag/2_QPVerification_Approval.csv"
            approve_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[5]/div/div/button[1]')

            message = "QPFragmentation Approved Successfully" if approve_button.is_enabled() else "Not-Approved-Error"
            
            if approve_button.is_enabled():
                approve_button.click() #variable called
                time.sleep(5)
                
                # # Sub menu 2nd time
                # stream_sub_menu = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/ul/li[3]/a/span')
                # stream_sub_menu.click()
                # time.sleep(2)  #5

            else:
                #self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[1]/div/div[1]/div/button").click()
                
                #Scroll Up using Java Script
                window_size = 5000  # Declare the variable called window_size to scroll up
                self.driver.execute_script(f"window.scrollBy(0, -{window_size});")  # Scroll up by 5000 pixels
                time.sleep(3)

                self.back_button()  #function called
            time.sleep(2)

            stream_data_list[index]['Test_Report_Data'] = message

        with open(self.output_file, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = stream_data_list[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(stream_data_list)
        print("Verification Completed and Results Saved")
####################################################################################################
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

#########################################################################
    @classmethod
    def test_Sound_Effect(cls):
        """Play a sound effect when tests complete"""
        try:
            # ✅ Sound 1: Windows Beep
            frequency = 1000  # Frequency in Hz (37 to 32,767)
            duration = 500  # Duration in milliseconds
            winsound.Beep(frequency, duration)
            print("✅ Beep sound played.")

            # ✅ Sound 2: MP3 Playback
            sound_file = os.path.abspath("1_AI_QA_MasterData_CSV/1_ViewEvaluatedAnswerScript_Download/Chitti.mp3")
            if os.path.exists(sound_file):
                playsound(sound_file)
                print("✅ MP3 sound played successfully.")
            else:
                print(f"❌ Error: Sound file not found - {sound_file}")

        except Exception as e:
            print(f"❌ Sound playback failed: {e}")
#########################################################################