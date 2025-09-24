

'''
pytest test_ex1.py
pytest test_Login_Stream_MoreData.py test_Login_Stream_Edit.py --html=report.html

To run multiple  .py files
pytest test_Login_Stream_MoreData.py test_Login_Stream_Edit.py test_ex1.py --html=report3.html

pytest test_qa.py --html=report1.html
pytest test_ex.py --html=report1.html
'''
import pytest

class TestAutomation:
    
    def test_testm11(self):
        print("test 123..")
        
    def test_Assert12(self):
        x = 10
        assert x == 10  # This will pass because the condition is True
        print("Assertion passed.")

    def test_testm112(self):
        print("test 12sdfsdf..")