'''
# Run only one class [TestAutomation]
# Run report also  [--html=report1.html]

pytest -v --html=report1.html -k TestAutomation test_Loging1.py::TestAutomation

pytest test_Loging2.py
pytest -v --html=report1.html -k TestAutomation test_Loging2.py::Tes+tAutomation
pytest -v --html=report1.html -k TestAutomation test_Loging2.py::Tes+tAutomation
pytest -v --html=report1.html -k TestAutomation test_Loging2.py::TestAutomation

pytest -v --html=report1.html -k TestAutomation test_Login_Stream_MoreData.py::TestAutomation
pytest -v --html=report1.html -k TestAutomation test_Login_Stream_MoreData.py::TestAutomation

pytest test_Frag1.py --html=report1.html
pytest test_frag_normal_1.py --html=report1.html
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
        """Setup method to initialize the browser"""
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.userid = ""
        cls.password = ""

        # cls.stream_code = ""
        # cls.stream_name = ""
#ExamCycle,ExamSeries,SubjectCode,Template  
        cls.ExamCycle=""
        cls.ExamSeries=""
        cls.SubjectCode=""
        cls.Template=""       
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

#Marks1     QuestionNumber2   QuestionsIndividual3
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
    


    # def wait_for_element(self, by, value, timeout=10):    
    #         """Wait for an element to be visible."""
    #         return WebDriverWait(self.driver, timeout).until(
    #             EC.visibility_of_element_located((by, value))
    #         )


#Login Page
    def test_login(self):
        """Tests login functionality."""
        self.read_credentials('useridpw.csv')# user id password file name should be here
        self.driver.get("http://172.25.8.162") # application user for testing 
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


    def test_confirm_login(self):
        """Clicks the confirmation button after login."""    
        confirm_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]')
        confirm_button.click()
        print("Confirmation Successful")
        time.sleep(5)

########################################################################################################################
    def test_QP_Frag_Dropdown1(self):
        """Adds fragmentation using CSV excel file."""
        stream_data_list = self.read_stream_data('fragDropdown.csv')
#ExamCycle,ExamSeries,SubjectCode,Template
        for stream_data in stream_data_list:
            self.ExamCycle = stream_data['ExamCycle']
            self.ExamSeries = stream_data['ExamSeries']
            self.SubjectCode = stream_data['SubjectCode']
            self.Template = stream_data['Template']

# Navigate to the QP Frag Main menu [Question Paper Main Menu Clicked]
            stream_menu1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/a/span')
            stream_menu1.click()
            time.sleep(2)
            print("Main menu clicked")

# Navigate to the QP Frag Main menu [QP Frag Submenu Clicked]
            stream_menu2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/ul/li[3]/a/span')
            stream_menu2.click()
            time.sleep(2)
            print("Main menu clicked")  
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
            ######################################################################  ExamCycle,ExamSeries,SubjectCode,Template


            # 2 Exam Series Dropdown field data enter
            stream_name_field2 = self.driver.find_element(By.NAME, 'examseries_id')
            stream_name_field2.click()
            stream_name_field2.send_keys(self.ExamSeries)
            # 2 Exam Cycle Dropdown menu clicked
            stream_name_field2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[3]/div/div[2]/div/div[2]/div')
            stream_name_field2.click()

            time.sleep(5)
            print("2 Exam Series Dropdown entered...")
            ###################################################################### ExamCycle,ExamSeries,SubjectCode,Template

            # 3 Subject Code field data enter
            stream_name_field3 = self.driver.find_element(By.NAME, 'subject_code')
            stream_name_field3.click()
            stream_name_field3.send_keys(self.SubjectCode)
            # 3 Exam Cycle Dropdown menu clicked
            #stream_name_field3 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[3]/div/div[2]/div/div[2]/div')
            #stream_name_field3.click()

            time.sleep(8)
            print("2 Exam Series Dropdown entered...")
            ######################################################################  M002T2

            ######################################################################  ExamCycle,ExamSeries,SubjectCode,Template


            # 4 Template Dropdown field data enter
            stream_name_field4 = self.driver.find_element(By.NAME, 'Templateid')
            stream_name_field4.click()
            stream_name_field4.send_keys(self.Template)
            # 2 Exam Cycle Dropdown menu clicked
            stream_name_field4 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[5]/div/div[2]/div/div[2]/div')
            stream_name_field4.click()

            time.sleep(5)
            print("2 Exam Series Dropdown entered...")
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
###################################################################### QuestionNumbe NumberOfQuestions

#Enter 1) Question Number field and 2) Number Of Questions field text box
    def test_QP_Frag_Question2(self):
        print("Entering Question..")  #questionnumber
        self.read_credentials_NumberOfQuestion('fragNumberOfQuestions.csv')
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

        # Dropdown Selection
        # qpds_qpindent_College = self.driver.find_element(By.NAME, 'CollegeID')
        # select = Select(qpds_qpindent_College)
        # select.select_by_index(1)
        # time.sleep(20)

        # qpds_qpindent_ExamSession = self.driver.find_element(By.NAME, 'ExamSessionID')
        # select = Select(qpds_qpindent_ExamSession)
        # select.select_by_visible_text("Morning Session")
        # time.sleep(2)


#Fragmentation Continue Button Clicked  
        stream_name_field_Frag_Continue_Button1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[7]/div/div/button[1]')
        stream_name_field_Frag_Continue_Button1.click()
        time.sleep(5)

###################################################################################################

#questions.0.mark
#questions.0.qdisplay
#/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[1]/div/div[2]/div[2]/div[2]/div/p

#questions.1.mark
#questions.1.qdisplay
#/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div/div[2]/div[2]/div[2]/div/p
#....................................................................
#questions.7.mark
#questions.7.qdisplay
#/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[8]/div/div[2]/div[2]/div[2]/div/p

# Enter Each Individual Questions one by one




##############################################  Marks1     QuestionNumber2   QuestionsIndividual3

    def test_QP_Frag_Individual_Questions22(self):
        stream_data_list_Individual_Questions = self.read_stream_data_Individual_Questions('fragIndividualQuestions.csv')

        #Marks1     QuestionNumber2   QuestionsIndividual3
        for stream_data_Individual_Questions  in stream_data_list_Individual_Questions :
            self.Marks1 = stream_data_Individual_Questions['Marks1']
            self.QuestionNumber2 = stream_data_Individual_Questions['QuestionNumber2']
            self.QuestionsIndividual3 = stream_data_Individual_Questions['QuestionsIndividual3']

############################################## Question 1
            #Marks1     QuestionNumber2   QuestionsIndividual3

            QPFrag1 = self.driver.find_element(By.NAME, 'questions.0.mark')  
            QPFrag1.click()
            QPFrag1.send_keys(self.Marks1)
            time.sleep(5)
            print("Mark.....")

            QPFrag2 = self.driver.find_element(By.NAME, 'questions.0.qdisplay')
            QPFrag2.click()
            QPFrag2.send_keys(self.QuestionNumber2)
            time.sleep(5)
            print("Question Number.......")

            QPFrag3 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[1]/div/div[2]/div[2]/div[2]/div')
            QPFrag3.click()
            QPFrag3.send_keys(self.QuestionsIndividual3)
            time.sleep(4)
            print("Question .......")

########################################################### Question 2
            # Scroll Down by Pixel # Scroll down 500 pixels
            self.driver.execute_script("window.scrollBy(0, 500);")  # Scroll down 500 pixels
            time.sleep(5)

            QPFrag12 = self.driver.find_element(By.NAME, 'questions.1.mark')  
            QPFrag12.click()
            QPFrag12.send_keys(self.Marks1)
            time.sleep(5)
            print("Mark.....")

            QPFrag2 = self.driver.find_element(By.NAME, 'questions.1.qdisplay')
            QPFrag2.click()
            QPFrag2.send_keys(self.QuestionNumber2)
            time.sleep(5)
            print("Question Number.......")

            QPFrag3 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div/div[2]/div[2]/div[2]/div')
            QPFrag3.click()
            QPFrag3.send_keys(self.QuestionsIndividual3)
            time.sleep(4)
            print("Question .......")
######################################################################
########################################################### Question 3
            # Scroll Down by Pixel # Scroll down 500 pixels
            self.driver.execute_script("window.scrollBy(0, 300);")  # Scroll down 500 pixels
            time.sleep(5)

            QPFrag12 = self.driver.find_element(By.NAME, 'questions.2.mark')  
            QPFrag12.click()
            QPFrag12.send_keys(self.Marks1)
            time.sleep(5)
            print("Mark.....")

            QPFrag2 = self.driver.find_element(By.NAME, 'questions.2.qdisplay')
            QPFrag2.click()
            QPFrag2.send_keys(self.QuestionNumber2)
            time.sleep(5)
            print("Question Number.......")

            QPFrag3 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[3]/div/div[2]/div[2]/div[2]/div')
            QPFrag3.click()
            QPFrag3.send_keys(self.QuestionsIndividual3)
            time.sleep(4)
            print("Question .......")
######################################################################

########################################################### Question 4
            # Scroll Down by Pixel # Scroll down 500 pixels
            self.driver.execute_script("window.scrollBy(0, 250);")  # Scroll down 500 pixels
            time.sleep(5)

            QPFrag12 = self.driver.find_element(By.NAME, 'questions.3.mark')  
            QPFrag12.click()
            QPFrag12.send_keys(self.Marks1)
            time.sleep(5)
            print("Mark.....")

            QPFrag2 = self.driver.find_element(By.NAME, 'questions.3.qdisplay')
            QPFrag2.click()
            QPFrag2.send_keys(self.QuestionNumber2)
            time.sleep(5)
            print("Question Number.......")

            QPFrag3 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[4]/div/div[2]/div[2]/div[2]/div')
            QPFrag3.click()
            QPFrag3.send_keys(self.QuestionsIndividual3)
            time.sleep(4)
            print("Question .......")
######################################################################

########################################################### Question 5
            # Scroll Down by Pixel # Scroll down 500 pixels
            self.driver.execute_script("window.scrollBy(0, 250);")  # Scroll down 500 pixels
            time.sleep(5)

            QPFrag12 = self.driver.find_element(By.NAME, 'questions.4.mark')  
            QPFrag12.click()
            QPFrag12.send_keys(self.Marks1)
            time.sleep(5)
            print("Mark.....")

            QPFrag2 = self.driver.find_element(By.NAME, 'questions.4.qdisplay')
            QPFrag2.click()
            QPFrag2.send_keys(self.QuestionNumber2)
            time.sleep(5)
            print("Question Number.......")

            QPFrag3 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[5]/div/div[2]/div[2]/div[2]/div')
            QPFrag3.click()
            QPFrag3.send_keys(self.QuestionsIndividual3)
            time.sleep(4)
            print("Question .......")
######################################################################

########################################################### Question 6
            # Scroll Down by Pixel # Scroll down 500 pixels
            self.driver.execute_script("window.scrollBy(0, 250);")  # Scroll down 500 pixels
            time.sleep(5)

            QPFrag12 = self.driver.find_element(By.NAME, 'questions.5.mark')  
            QPFrag12.click()
            QPFrag12.send_keys(self.Marks1)
            time.sleep(5)
            print("Mark.....")

            QPFrag2 = self.driver.find_element(By.NAME, 'questions.5.qdisplay')
            QPFrag2.click()
            QPFrag2.send_keys(self.QuestionNumber2)
            time.sleep(5)
            print("Question Number.......")

            QPFrag3 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[6]/div/div[2]/div[2]/div[2]/div')
            QPFrag3.click()
            QPFrag3.send_keys(self.QuestionsIndividual3)
            time.sleep(4)
            print("Question .......")
######################################################################

########################################################### Question 7
            # Scroll Down by Pixel # Scroll down 500 pixels
            self.driver.execute_script("window.scrollBy(0, 350);")  # Scroll down 500 pixels
            time.sleep(5)

            QPFrag12 = self.driver.find_element(By.NAME, 'questions.6.mark')  
            QPFrag12.click()
            QPFrag12.send_keys(self.Marks1)
            time.sleep(5)
            print("Mark.....")

            QPFrag2 = self.driver.find_element(By.NAME, 'questions.6.qdisplay')
            QPFrag2.click()
            QPFrag2.send_keys(self.QuestionNumber2)
            time.sleep(5)
            print("Question Number.......")

            QPFrag3 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[7]/div/div[2]/div[2]/div[2]/div')
            QPFrag3.click()
            QPFrag3.send_keys(self.QuestionsIndividual3)
            time.sleep(4)
            print("Question .......")
######################################################################


########################################################### Question 8
            # Scroll Down by Pixel # Scroll down 500 pixels
            self.driver.execute_script("window.scrollBy(0, 350);")  # Scroll down 500 pixels
            time.sleep(5)

            QPFrag12 = self.driver.find_element(By.NAME, 'questions.7.mark')  
            QPFrag12.click()
            QPFrag12.send_keys(self.Marks1)
            time.sleep(5)
            print("Mark.....")

            QPFrag2 = self.driver.find_element(By.NAME, 'questions.7.qdisplay')
            QPFrag2.click()
            QPFrag2.send_keys(self.QuestionNumber2)
            time.sleep(5)
            print("Question Number.......")

            QPFrag3 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[8]/div/div[2]/div[2]/div[2]/div')
            QPFrag3.click()
            QPFrag3.send_keys(self.QuestionsIndividual3)
            time.sleep(4)
            print("Question .......")
######################################################################


########################################################### Final Submit
####################### QP Frag Create_Button Clicked
            # QPFrag_Create_Button1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[9]/div/div/div/div/button')
            # QPFrag_Create_Button1.click()
            # time.sleep(22)
######################################################################