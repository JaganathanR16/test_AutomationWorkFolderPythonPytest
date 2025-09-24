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

#Groups 3)
# ie., example : -m marks #smoke  [meaning]
#@pytest.mark.smoke
#**    5) python -m pytest -m smoke -v -s    ## Run only Tag @ "smoke" availage  #@pytest.mark.smoke
#1 failed, 1 passed, 2 deselected, 2 warnings in 0.16s 


#3) python -m pytest -v -s    
#1 failed, 3 passed, 2 warnings in 0.15s 

#@pytest.mark.skip
#3 passed, 1 skipped, 2 warnings in 0.04s
#   python -m pytest -v -s

#yellow Pass it will run but no status [Pass / Fail]
#2 passed, 1 skipped, 1 xpassed, 2 warnings in 0.04s
#   python -m pytest -v -s
import pytest

@pytest.mark.smoke
def test_firstProgramme():
    print("Hellow1")

@pytest.mark.xfail    #required to run but not required report
def test_secondProgrammeCreditCard():
    print("Hellow2")
    