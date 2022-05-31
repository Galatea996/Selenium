from selenium import webdriver
import time 

try:
    link = "http://iot.adani.by:8186/login"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//*[@id="mui-1"]')
    input1.send_keys("admin@adani.by")
    time.sleep(3)
    input2 = browser.find_element_by_xpath('//*[@id="mui-2"]')
    input2.send_keys("1234")
    time.sleep(3)
    button = browser.find_element_by_css_selector("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
