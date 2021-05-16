import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep((3))
countries= driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(countries)


for country in countries:
    if country.text== "India":
        country.click()
        break

assert driver.find_element_by_id("autosuggest").get_attribute("value")== "Indi", "doesn't match"

