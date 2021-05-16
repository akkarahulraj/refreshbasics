import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver= webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.double_click(driver.find_element_by_id("double-click")).perform()
time.sleep(5)

alerts= driver.switch_to.alert

alerts.accept()

