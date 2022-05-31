from selenium import webdriver
import unittest
   
link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)
    
class test_class_name(unittest.TestCase):

    def test_link(self):
        element_registration = browser.find_element_by_css_selector('h1').text
        self.assertEqual(element_registration, 'Registration', "page_open_error")
    
   #def test_text1(self):
        input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("Ivan")
     #   self.assertEqual(input1.get_attribute('placeholder'), 'Input your first name', "input1_past_error")

   # def test_text2(self):
        input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
       # self.assertEqual(input2.get_attribute('placeholder'), 'Input your first name', "input2_past_error")
    
   # def test_text3(self):
        input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("test@mail.ru")
     #   self.assertEqual(input3.get_attribute('placeholder'), 'Input your first name', "input3_past_error")
    
    #def test_text4(self):
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        congratulation = browser.find_element_by_css_selector("h1")
        self.assertEqual(congratulation.text, 'Congratulations! You have successfully registered!', "button_click_error")
 
 if __name__ == "__main__": 
    unittest.main()
