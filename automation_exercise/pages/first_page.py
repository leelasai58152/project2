from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Page:
    h_over=(By.CLASS_NAME,"product-overlay")
    
    
    
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,20)
        
    def open_page(self):
        
        element=self.wait.until(EC.visibility_of_element_located(self.h_over))
        self.driver.execute_script("arguments[0].scrollIntoView();",element)
        actions=ActionChains(self.driver)
        actions.move_to_element(element).perform
        
        self.driver.find_element(By.XPATH,"//a[@class='btn btn-default add-to-cart']").click()
        
