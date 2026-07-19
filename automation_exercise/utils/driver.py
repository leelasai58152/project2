from selenium import webdriver
from selenium.webdriver.chrome.service import Service
def get_driver():
    service = Service(r"C:\Drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver