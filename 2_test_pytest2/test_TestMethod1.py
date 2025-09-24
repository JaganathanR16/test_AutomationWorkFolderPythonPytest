#pytest method requied and starting with test_
#Pytest Rahul Shetty video

#pip install pytest
#1) python -m pytest
#2) python -m pytest -v       #Vargose will give more information [ie., Case directory and etc]
#3) python -m pytest -v -s    #Console print "Hellow"
###########################
#pip install pytest-html
##pytest --html=report.html
###########################HTML Report will create
#python -m pytest -v -s --html=report.html
###########################Copy report.html path and past in browser to display report
#file:///D:/test_AutomationWorkFolderPythonPytest/test_pytest/report.html?sort=result
################################
#3) python -m pytest -v -s                      #Console print "Hellow"
#4) python -m pytest -k CreditCard -v -s        #Run only method name contains "CreditCard" [ie., selected module test case]

def test_firstProgramme():
    print("Hellow1")


def test_secondProgrammeCreditCard():
    print("Hellow2")
    