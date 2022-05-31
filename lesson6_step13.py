from selenium import webdriver
import time 
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("test@mail.ru")
 
    #current_dir = os.path.abspath(os.path.dirname()) 
    file_path = os.path.join("C:/Users/kotova-mv/selenium/Dfile.txt")
    browser.find_element_by_name("file").send_keys(file_path)
   

    button = browser.find_element_by_xpath("/html/body/div/form/button")
    button.click()
    
    print("Тест успешно завершен. 10 сек на закрытие браузера...")

finally:
    time.sleep(5)
    browser.quit()
