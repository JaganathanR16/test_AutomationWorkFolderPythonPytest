'''
# Run only one class [TestAutomation]
# Run report also  [--html=report1.html]
pytest test_Loging2.py
pytest -v --html=report1.html -k TestAutomation test_Loging1.py::TestAutomation
pytest -v --html=report1.html -k TestAutomation test_Login_Stream_MoreData.py::TestAutomation
pytest test_Frag1.py --html=report1.html

pytest test_qp_fragmentation_automation_Expriment.py --html=report1.html

pytest test_AI_QA_qp_fragmentation_automation_Expriment.py --html=report1.html

'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select   # Dropdown field

from selenium.webdriver.common.keys import Keys  # Tab key

class TestAutomation:
    #Declar Class Methods
    @classmethod
    def setup_class(cls):
        """Setup method to initialize the browser"""
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        #Variable declaration for UserID and Password field 
        cls.userid = ""
        cls.password = ""

        #Variable declaration for ExamCycle, ExamSeries, SubjectCode, Template dropdown fields
        cls.ExamCycle=""
        cls.ExamSeries=""
        cls.SubjectCode=""
        cls.Template=""       
        print("Browser Launched Successfully")

    #Declar Class Methods
    @classmethod
    def teardown_class(cls):
        """Teardown method to close the browser"""
        cls.driver.quit()
        print("Browser Closed Successfully")

        # setup_class() runs before all tests in the class.
        # teardown_class() runs after all tests in the class.

##################################################################################################
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

    #Declar for fragmentation mark / quesion number / question entry firld     # Multi line read
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
    
    # wait untill field get load 
    # def wait_for_element(self, by, value, timeout=10):    
    #         """Wait for an element to be visible."""
    #         return WebDriverWait(self.driver, timeout).until(
    #             EC.visibility_of_element_located((by, value))
    #         )

##############################################################################
    #Login Page
    def test_login(self):
        """Tests login functionality."""
        self.read_credentials('AI_QA_CSV_File_Folder/useridpw1.csv')# user id password file name should be here
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
        print("QP Fragmentation User Login Successfully..")

    def test_confirm_popup_window_login(self):
        """Clicks the confirmation button after login."""    
        confirm_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]')  
        confirm_button.click()
        print("Login, PopUp Window Confirmation is Success..")
        time.sleep(5)

########################################################################################################################
    def test_QP_Frag_Dropdown_Field_Selection_1(self):
        """Adds fragmentation using CSV excel file."""
        stream_data_list = self.read_stream_data('AI_QA_CSV_File_Folder/fragDropdown2.csv')    #######################################
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
            print("Main menu clicked successfully")

            # Navigate to the QP Frag Main menu [QP Frag Submenu Clicked]
            stream_menu2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/div[2]/ul/div/div[1]/div[2]/div/div/div/li[4]/ul/li[3]/a/span')
            stream_menu2.click()
            time.sleep(2)
            print("Sub-menu clicked successfully")  
            ######################################################################  
            # 1 Exam Cycle Dropdown field data enter

            stream_name_field = self.driver.find_element(By.NAME, 'examcycle_id')
            stream_name_field.click()
            stream_name_field.send_keys(self.ExamCycle)
            # 1 Exam Cycle Dropdown menu clicked
            stream_name_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[2]/div/div/div[2]/div/div[2]')
            stream_name_field.click()
            time.sleep(5)
            print("1) Exam cycle dropdown entered and selected")


# // Create a Select object
# Select select = new Select(dropdown);

# // Select by visible text
# select.selectByVisibleText("OptionText");


            # # Find the dropdown by its NAME attribute
            # stream_name_field = self.driver.find_element(By.NAME, "examcycle_id")
            # stream_name_field.click()

            # # Type in the search field
            # #stream_name_field.send_keys("Winter")

            # # Create Select object
            # select = Select(stream_name_field)

            # # Select "Winter"
            
            # stream_name_field.click(select.select_by_visible_text("Winter"))
            # # Verify selection
            # assert select.first_selected_option.text == "Winter"

            ######################################################################  ExamCycle,ExamSeries,SubjectCode,Template


            # 2 Exam Series Dropdown field data enter
            stream_name_field2 = self.driver.find_element(By.NAME, 'examseries_id')
            stream_name_field2.click()
            stream_name_field2.send_keys(self.ExamSeries)
            # 2 Exam Cycle Dropdown menu clicked
            stream_name_field2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[3]/div/div[2]/div/div[2]/div')
            stream_name_field2.click()

            time.sleep(5)
            print("2) Exam Series dropdown entered and selected")
            ###################################################################### ExamCycle,ExamSeries,SubjectCode,Template

            # 3 Subject Code field data enter
            stream_name_field3 = self.driver.find_element(By.NAME, 'subject_code')
            stream_name_field3.click()
            stream_name_field3.send_keys(self.SubjectCode)
            # 3 Subject Code text box clicked
            #stream_name_field3 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[3]/div/div[2]/div/div[2]/div')
            #stream_name_field3.click()

            time.sleep(8)
            print("3) Subject Code dropdown entered and selected")
            ###################################################################### Subject code M002T2

            ######################################################################  ExamCycle,ExamSeries,SubjectCode,Template
            # 4 Template Name Dropdown field data enter
            stream_name_field4 = self.driver.find_element(By.NAME, 'Templateid')
            stream_name_field4.click()
            stream_name_field4.send_keys(self.Template)
            # 4 Template Name Dropdown field data enter and clicked
            stream_name_field4 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/form/div[5]/div/div[2]/div/div[2]/div')
            stream_name_field4.click()

            time.sleep(5)
            print("4) Template Name dropdown entered and selected")
            ###################################################################### ExamCycle,ExamSeries,SubjectCode,Template

            # 1. Start Processing QP Button click   
            stream_name_field_FragButton1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[6]/div/div/button')
            stream_name_field_FragButton1.click()
            time.sleep(5)

            # Start Processing QP Button click  -> 2.Details link click           /html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[5]/div/div/span
            stream_name_field_FragLinkText1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[5]/div/div/span')
            stream_name_field_FragLinkText1.click()
            time.sleep(5)

            # 3.Add Question Button Clicked                                            /html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/button[1]
            stream_name_field_Frag_AddQu_Button1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/button[1]')
            stream_name_field_Frag_AddQu_Button1.click()
            time.sleep(5)
###################################################################### QuestionNumbe NumberOfQuestions

    #Enter 1) Question Number field and 2) Number Of Questions field text box
    def test_QP_Frag_QuestionNumber_NoofQuestion_Field_Entry_2(self):
        print("Start to entering individual question from csv file ..")  #questionnumber

        self.read_credentials_NumberOfQuestion('AI_QA_CSV_File_Folder/fragNumberOfQuestions3.csv')   ######################################
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

################################################################################################### Marks1     QuestionNumber2   QuestionsIndividual3
    # Enter Each Individual Questions one by one from here using Index start from 0, 1, 2, ...... 
    def create_question(self,marks,question_number,question_indivi,index):    #self and index variable required + 3 variables [marks,question_number,question_indivi]

        QPFrag1 = self.driver.find_element(By.NAME, f'questions.{index}.mark')  
        QPFrag1.click()
        QPFrag1.send_keys(marks)
        #time.sleep(1)
        print("Mark.....")

        QPFrag2 = self.driver.find_element(By.NAME, f'questions.{index}.qdisplay')
        QPFrag2.click()
        QPFrag2.send_keys(question_number) #stream_data_list_Individual_Questions[0]['QuestionNumber2']
        #time.sleep(5)
        print("Question Number.......")

        QPFrag3 = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[{index+1}]/div/div[2]/div[2]/div[2]/div')
        QPFrag3.click()
        QPFrag3.send_keys(question_indivi)
        time.sleep(2)
        print("Question .......")

    #Individual_Questions#############################################################################################################################
    def test_QP_Frag_Individual_Questions3(self):
        stream_data_list_Individual_Questions = self.read_stream_data_Individual_Questions('AI_QA_CSV_File_Folder/fragIndividualQuestions4.csv') ########################

        print('stream_data_list_Individual_Questions',stream_data_list_Individual_Questions)
        window_size=300  #declar the variable called window_size to scroll down window
        #Marks1     QuestionNumber2   QuestionsIndividual3 stream_data_list_Individual_Questions[0]['Marks1']
        for index,stream_data_Individual_Questions in enumerate(stream_data_list_Individual_Questions) :
            print('index--',index,'stream_data_Individual_Questions',stream_data_Individual_Questions)

            self.Marks1 = stream_data_Individual_Questions['Marks1']
            self.QuestionNumber2 = stream_data_Individual_Questions['QuestionNumber2']
            self.QuestionsIndividual3 = stream_data_Individual_Questions['QuestionsIndividual3']

            # Scroll using JavaScript
            #driver.execute_script("window.scrollBy(0, 500);")  # Scroll down 500 pixels

            # Scroll Down by Pixel # Scroll down 500 pixels
            # window_size+=50
            self.driver.execute_script(f"window.scrollBy(0, {window_size});")  # Scroll down 500 pixels
            time.sleep(5)

            #Called from Function called [create_question()]
            self.create_question(self.Marks1,self.QuestionNumber2,self.QuestionsIndividual3,index)


######################  Final Submit  ########################################################################################################
    #Create Button Click Final
    def test_Create_Button(self):
        # Create Fragmentation Button Cliced finally to submit fragmentation
        QPFrag_Create_Button1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[9]/div/div/div/div/button')
        QPFrag_Create_Button1.click()
        time.sleep(2)
##############################################################################################################################


############################################################## /html/body/div[3]/div/div/div[1]/div[2]
    def test_popup_message_Frag_Submitted_Result_msg(self):
        try:
            # Locate the popup message element
            popup_message_a121 = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]')
        
            # Capture the text of the popup message
            popup_text = popup_message_a121.text
            print(f"Captured Popup Message: {popup_text}")
        
            # Assert the popup text is the expected message
            expected_message = "Question Template Mapping Details Created Successfully."
            if popup_text != expected_message:
                pytest.fail(f"Test Failed: Expected '{expected_message}', but got '{popup_text}'")
            else:
                print("Test Passed: Popup message matches the expected text, Fragmentation Is Success.........")
        except Exception as e:
                print(f"Error occurred: {e}")
                pytest.fail(f"Test Failed due to exception: {e}")


# Question Template Mapping Details Created Successfully.
# /html/body/div[3]/div/div[1]/div[1]/div[2]

# Fragmentation completed sucussfully.
# /html/body/div[3]/div/div[2]/div[1]/div[2]

        #Stream created successfully.
        #Please enter a unique stream code.
        #Please enter a unique stream name.
##############################################################