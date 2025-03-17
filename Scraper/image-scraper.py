from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(executable_path=r'C:\Users\Miguel Cerna\OneDrive\Desktop\objectClassification-\chromedriver.exe')


driver = webdriver.Chrome(service=service)


search_url = "https://www.google.com/imghp"
driver.get(search_url)

#Finds Search Bar
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Military Jet")  # Type query
search_box.send_keys(Keys.RETURN)  # Press Enter

time.sleep(3)  # Wait for results to load

for _ in range(10):  # Scroll 10 times
    driver.execute_script("window.scrollBy(0, 1000);")  # Scroll down
    time.sleep(2)  # Wait for images to load
