from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import math

try:
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    #book the right price
    price = driver.find_element(By.ID, "price").text

    dollars100 = WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book = driver.find_element(By.ID, "book")
    book.click()
    
    #solve the problem
    x_value=driver.find_element(By.ID,'input_value').text
    
    calc_function=str(math.log(abs(12*math.sin(int(x_value)))))
    
    solve_problem=driver.find_element(By.NAME,'text').send_keys(calc_function)
    
    driver.find_element(By.XPATH,'/html/body/form/div/div/button').click()

    time.sleep(5)
    
finally:
    driver.quit()
