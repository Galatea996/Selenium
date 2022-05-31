from selenium import webdriver
import time 

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
    input1.send_keys("Ivan")
    time.sleep(2)
    input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
    input2.send_keys("Petrov")
    time.sleep(2)
    input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
    input3.send_keys("test@mail.ru")
    time.sleep(2)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(6)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
