
'''
Description: To Fragmentation module [Question Paper Fragmentation]

# Run only one class [TestAutomation]
# Run report also  [--html=report1.html]

pytest -v --html=report1.html -k TestAutomation test_Loging1.py::TestAutomation

pytest test_Loging2.py
pytest -v --html=report1.html -k TestAutomation test_Loging2.py::Tes+tAutomation
pytest -v --html=report1.html -k TestAutomation test_Loging2.py::Tes+tAutomation
pytest -v --html=report1.html -k TestAutomation test_Loging2.py::TestAutomation

pytest -v --html=report1.html -k TestAutomation test_Login_Stream_MoreData.py::TestAutomation
pytest -v --html=report1.html -k TestAutomation test_Login_Stream_MoreData.py::TestAutomation

pytest test_AI_QA_QPFrag_GU_LIVE_12_4.py --html=report1.html

useridpw.csv
fragDropdown.csv
fragNumberOfQuestions.csv'
fragIndividualQuestions.csv
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

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        print("Browser Closed Successfully")
        # setup_class() runs before all tests in the class.
        # teardown_class() runs after all tests in the class.
    ####################################################################
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
                    'ExamCycle': row['ExamCycle'],
                    'ExamSeries': row['ExamSeries'],
                    'SubjectCode': row['SubjectCode'],
                    'Template': row['Template']
                })
        return stream_data_list
    
    def read_credentials_NumberOfQuestion(self, file_path):
        """Reads credentials from CSV file."""
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                self.QuestionNumber = row['QuestionNumber']
                self.NumberOfQuestions = row['NumberOfQuestions']
                break

    #Marks1     QuestionNumber 2   QuestionsIndividual 3
    def read_stream_data_Individual_Questions(self, file_path):
        """Reads multiple stream data from CSV file."""
        stream_data_list_Individual_Questions = []
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                stream_data_list_Individual_Questions.append({
                    'Marks1': row['Marks1'],
                    'QuestionNumber2': row['QuestionNumber2'],
                    'QuestionsIndividual3': row['QuestionsIndividual3']
                })
        return stream_data_list_Individual_Questions
    ####################################################################
    # def wait_for_element(self, by, value, timeout=10):    
    #         """Wait for an element to be visible."""
    #         return WebDriverWait(self.driver, timeout).until(
    #             EC.visibility_of_element_located((by, value))
    #         )
    ####################################################################

    #Login Page
    def test_login(self):
        """Tests login functionality."""
        self.read_credentials('useridpw.csv')# user id password file name should be here
        self.driver.get("https://gung.intelliexams.com") # application user for testing 
        time.sleep(3)
        
        userid_field = self.driver.find_element(By.NAME, 'email')
        userid_field.send_keys(self.userid)
        time.sleep(1)

        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(self.password)
        time.sleep(3)
                                                          
        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/form/div[3]/div[1]/button")
        login_button.click()
        time.sleep(5)
        #assert "Dashboard" in self.driver.title
        print("Login Successful")
    ####################################################################
    # Click on Confirmation Button
    def test_confirm_login(self):
        """Clicks the confirmation button after login."""    
        confirm_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]')
        confirm_button.click()
        print("Confirmation Successful")
        time.sleep(5)
    ########################################################################################################################

    def test_man_menu(self):
        # Navigate to the QP Frag Main menu [Question Paper Main Menu Clicked]
        stream_menu1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/a/span')
        stream_menu1.click()
        time.sleep(2)
        print("Main menu clicked")

        # Navigate to the QP Frag Main menu [QP Frag Submenu Clicked]
        stream_menu2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/ul/li[3]/a/span')
        stream_menu2.click()
        time.sleep(2)
        print("Sub menu clicked")  
    ########################################################################################################################

    # Dropdown field selection
    def test_QP_Frag_Dropdown1(self):
        """Adds fragmentation using CSV excel file."""
        stream_data_list = self.read_stream_data('1_AI_QA_MasterData_CSV/3_AI_QA_Frag/1_fragDropdown.csv')

        #for stream_data in stream_data_list:
        for index, stream_data in enumerate(stream_data_list):
            print(f"\nProcessing row {index+1}: {stream_data}")
            self.ExamCycle = stream_data['ExamCycle']
            self.ExamSeries = stream_data['ExamSeries']
            self.SubjectCode = stream_data['SubjectCode']
            self.Template = stream_data['Template']

            # # Navigate to the QP Frag Main menu [Question Paper Main Menu Clicked]
            # stream_menu1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/a/span')
            # stream_menu1.click()
            # time.sleep(2)
            # print("Main menu clicked")

            # # Navigate to the QP Frag Main menu [QP Frag Submenu Clicked]
            # stream_menu2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/ul/li[3]/a/span')
            # stream_menu2.click()
            # time.sleep(2)
            # print("Sub menu clicked")  
            ######################################################################
              
            # 1 Exam Cycle Dropdown field data enter
            stream_name_field = self.driver.find_element(By.NAME, 'examcycle_id')
            stream_name_field.click()
            stream_name_field.send_keys(self.ExamCycle)
            # 1 Exam Cycle Dropdown menu clicked
            stream_name_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[2]/div/div/div[2]/div/div[2]')
            stream_name_field.click()
            time.sleep(5)
            print("1 Exam cycle entered...")

            # 2 Exam Series Dropdown field data enter
            stream_name_field2 = self.driver.find_element(By.NAME, 'examseries_id')
            stream_name_field2.click()
            stream_name_field2.send_keys(self.ExamSeries)
            # 2 Exam Cycle Dropdown menu clicked
            stream_name_field2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[3]/div/div[2]/div/div[2]/div')
            stream_name_field2.click()
            time.sleep(5)
            print("2 Exam Series Dropdown entered...")

            # 3 Subject Code field data enter
            stream_name_field3 = self.driver.find_element(By.NAME, 'subject_code')
            stream_name_field3.click()
            stream_name_field3.send_keys(self.SubjectCode)
            time.sleep(8)
            print("3 Subject Code entered...")

            # 4 Template Dropdown field data enter
            stream_name_field4 = self.driver.find_element(By.NAME, 'Templateid')
            stream_name_field4.click()
            stream_name_field4.send_keys(self.Template)
            stream_name_field4 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[5]/div/div[2]/div/div[2]/div')
            stream_name_field4.click()
            time.sleep(5)
            print("4 Template entered...")
            ###################################################################### ExamCycle,ExamSeries,SubjectCode,Template

            # Start Processing QP Button click
            stream_name_field_FragButton1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[6]/div/div/button/i')
            stream_name_field_FragButton1.click()
            time.sleep(5)

            # Start Processing QP Button click  -> Details link click
            stream_name_field_FragLinkText1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[5]/div/div/span')
            stream_name_field_FragLinkText1.click()
            time.sleep(5)
 
            #Add Question Button Clicked  /html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/button[1]
            stream_name_field_Frag_AddQu_Button1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/button[1]')
            stream_name_field_Frag_AddQu_Button1.click()
            time.sleep(5)

            print(f"Finished processing row {index+1}\n")
        print("All rows from 1_fragDropdown.csv processed successfully!")
###################################################################### QuestionNumbe NumberOfQuestions

    # 1) Enter Question Number field and 2) Number Of Questions field text box
    def test_QP_Frag_Question2(self):
        print("Entering Question..")  #questionnumber
        self.read_credentials_NumberOfQuestion('1_AI_QA_MasterData_CSV/3_AI_QA_Frag/1_fragNumberOfQuestions.csv')
        time.sleep(2)

        QuestionNumber = self.driver.find_element(By.NAME, 'questionnumber')
        QuestionNumber.click()
        QuestionNumber.send_keys(self.QuestionNumber)
        time.sleep(2)

        NumberOfQuestions = self.driver.find_element(By.NAME, 'numberofquestions')
        NumberOfQuestions.click()
        NumberOfQuestions.send_keys(self.NumberOfQuestions)
        time.sleep(2)

        # Dropdown Selection
        unit_Dropdown_Selection = self.driver.find_element(By.NAME, 'unitId')
        select = Select(unit_Dropdown_Selection)
        select.select_by_index(1)
        time.sleep(2)

        #Fragmentation Continue Button Clicked  
        stream_name_field_Frag_Continue_Button1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[7]/div/div/button[1]')
        stream_name_field_Frag_Continue_Button1.click()
        time.sleep(5)

##############################################  Marks1     QuestionNumber2   QuestionsIndividual3

    # Enter Noof question to create
    def create_question(self,marks,question_number,question_indivi,index):
        QPFrag1 = self.driver.find_element(By.NAME, f'questions.{index}.mark')  
        QPFrag1.click()
        QPFrag1.send_keys(marks)
        time.sleep(5)
        print("Mark.....")

        QPFrag2 = self.driver.find_element(By.NAME, f'questions.{index}.qdisplay')
        QPFrag2.click()
        QPFrag2.send_keys(question_number)#stream_data_list_Individual_Questions[0]['QuestionNumber2']
        time.sleep(5)
        print("Question Number.......")

        QPFrag3 = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[{index+1}]/div/div[2]/div[2]/div[2]/div')
        QPFrag3.click()
        QPFrag3.send_keys(question_indivi)
        time.sleep(4)
        print("Question .......")

    ##############################################################################################################################
    
    # Enter Individual Questions
    def test_QP_Frag_Individual_Questions22(self):
        stream_data_list_Individual_Questions = self.read_stream_data_Individual_Questions('1_AI_QA_MasterData_CSV/3_AI_QA_Frag/1_fragIndividualQuestions.csv')

        print('stream_data_list_Individual_Questions',stream_data_list_Individual_Questions)
        window_size=300
        #Marks1     QuestionNumber2   QuestionsIndividual3 stream_data_list_Individual_Questions[0]['Marks1']
        for index,stream_data_Individual_Questions in enumerate(stream_data_list_Individual_Questions) :
            print('index--',index,'stream_data_Individual_Questions',stream_data_Individual_Questions)
            self.Marks1 = stream_data_Individual_Questions['Marks1']
            self.QuestionNumber2 = stream_data_Individual_Questions['QuestionNumber2']
            self.QuestionsIndividual3 = stream_data_Individual_Questions['QuestionsIndividual3']
            # Scroll Down by Pixel # Scroll down 500 pixels
            # window_size+=50
            self.driver.execute_script(f"window.scrollBy(0, {window_size});")  # Scroll down 500 pixels
            time.sleep(5)
            self.create_question(self.Marks1,self.QuestionNumber2,self.QuestionsIndividual3,index)

        #QPFrag_Create_Button1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[9]/div/div/div/div/button')
        QPFrag_Create_Button1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[3]/div/div/div/div/button')
        #QPFrag_Create_Button1 = self.driver.find_element(By.XPATH, '//button[text()='Create']')
        QPFrag_Create_Button1.click()
        time.sleep(10)


        GoBack_1_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/div/div/button[2]')
        GoBack_1_button.click()
        print("GoBack 1 button Successful")
        time.sleep(5)

        GoBack_2_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/div/div/button')
        GoBack_2_button.click()
        print("GoBack 2 button Successful")
        time.sleep(5)

        #self.test_QP_Frag_Dropdown1()  # Function called
        
        #self.test_two()

##############################################################################################################################

    # def test_one(self):
    #     print("one------------------------------------")

    # def test_two(self):
    #     print("two---------------------------------")

    # def test_three(self): 
    #     print("three-----------------------")