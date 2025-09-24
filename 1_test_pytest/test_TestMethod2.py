#pytest method requied and starting with test_
#Pytest Rahul Shetty video

#pip install pytest
#1) python -m pytest
#2) python -m pytest -v   #Vargose will give more information [ie., Case directory and etc]
#3) python -m pytest -v -s

def test_threeProgramme():
    #print("Hellow3")
    msg = "Hello 3"
    assert msg == "Hi", "Test Failed"
