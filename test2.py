from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest


class TestRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       service=Service("chromedriver.exe")
       cls.driver = webdriver.Chrome(service=service)

    
    def fill_registration_form(self, registration_url):
        self.driver.get(registration_url)
        self.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input').send_keys('Robotas')
        self.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input').send_keys('Robotauskas')
        self.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input').send_keys('robotas.robotauskas@mif.stud.vu.lt')
        self.driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/input').send_keys('+37061234567')
        self.driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div[2]/input').send_keys('Didlaukio g. 59, Vilnius')
        self.driver.find_element(By.XPATH, '/html/body/div/form/button').click()
        self.driver.implicitly_wait(5)

    def test_registration1(self):
        self.fill_registration_form("http://suninjuly.github.io/registration1.html")
        self.assertEqual(self.driver.find_element(By.TAG_NAME, 'h1').text, 'Congratulations! You have successfully registered!')
    
    def test_registration2(self):
        self.fill_registration_form("http://suninjuly.github.io/registration2.html")
        self.assertEqual(self.driver.find_element(By.TAG_NAME, 'h1').text, 'Congratulations! You have successfully registered!')
    
    @classmethod
    def tearDownClass(cls):
        return cls.driver.quit()
        

        
if __name__ == '__main__':
    unittest.main()
    