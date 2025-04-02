from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       service=Service("chromedriver.exe")
       cls.driver = webdriver.Chrome(service=service)

    
    def fill_registration_form(self, registration_url):
        self.driver.get(registration_url)
        try:
            self.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input').send_keys('Robotas')
            self.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input').send_keys('Robotauskas')
            # self.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input').send_keys('robotas.robotauskas@mif.stud.vu.lt')
            self.driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/input').send_keys('+37061234567')
            self.driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div[2]/input').send_keys('Didlaukio g. 59, Vilnius')
            self.driver.find_element(By.XPATH, '/html/body/div/form/button').click()
            self.driver.implicitly_wait(5)
        except NoSuchElementException:
            self.fail("Test failed due to missing element")

    def test_registration1(self):
        self.fill_registration_form("http://suninjuly.github.io/registration1.html")
        success_message= WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located((By.TAG_NAME,'h1'))
        ).text
        self.assertEqual(success_message, 'Congratulations! You have successfully registered!')
        time.sleep(2)

    
    
    def test_registration2(self):
        self.fill_registration_form("http://suninjuly.github.io/registration2.html")
        success_message= WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located((By.TAG_NAME,'h1'))
        ).text
        self.assertEqual(success_message, 'Congratulations! You have successfully registered!')
        time.sleep(2)
     
        
    @classmethod
    def tearDownClass(cls):
        return cls.driver.quit()
        

        
if __name__ == '__main__':
    unittest.main()
    