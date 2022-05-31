from selenium import webdriver
import time
import random

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector("[type='text']")
    city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
    for element in elements:
        element.send_keys(random.choice(city_list))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
   
    time.sleep(5)
    
    browser.quit()