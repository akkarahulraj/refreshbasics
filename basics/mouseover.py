from selenium import webdriver
from selenium.webdriver import ActionChains

driver= webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/hovers")
action= ActionChains(driver)
driver.find_element_by_class_name("figure")
action.move_to_element(driver.find_element_by_class_name("figure")).perform()
