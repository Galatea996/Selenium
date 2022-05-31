from selenium import webdriver
import time 
import pytest


    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
def test_text1():
    input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
    input1.send_keys("Ivan")
    time.sleep(5)
    input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
    input2.send_keys("Petrov")
    time.sleep(5)
    input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
    input3.send_keys("test@mail.ru")
    time.sleep(5)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(10)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    time.sleep(5)
    browser.quit()

if __name__ == "__main__":
    pytest.main()