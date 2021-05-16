import time

from selenium import webdriver

driver= webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
checkboxes=driver.find_elements_by_css_selector("input[type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value")=="option2":

        checkbox.click()
        assert checkbox.is_selected()
radiobuttons =driver.find_elements_by_css_selector("input[type='radio']")
print(len(checkboxes))
radiobuttons[2].click()

time.sleep(5)
driver.close()