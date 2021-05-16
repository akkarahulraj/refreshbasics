from selenium import webdriver

driver= webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
validatetext = "rahul"
driver.find_element_by_id("name").send_keys(validatetext)
driver.find_element_by_id("alertbtn").click()
alert= driver.switch_to.alert

print(alert.text)
alert.accept()

