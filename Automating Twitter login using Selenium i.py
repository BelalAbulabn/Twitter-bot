from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Navigate to the Twitter login page
driver.get("https://twitter.com/login")

# Find the username and password fields and enter the login credentials
#wait for 5 seconds
wait = WebDriverWait(driver, 100)
username = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')))
username.send_keys("at23kuzfuzf5470@gmail.com")
password = driver.find_element_by_name("session[password]")
password.send_keys("ijijij!")

# Find the login button and click it
login_button = driver.find_element_by_css_selector("div[data-testid='LoginForm_Login_Button']")
login_button.click()

# Wait for the login to complete
# You can use an explicit wait here if you expect the login process to take some time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_element_located((By.ID, "myDynamicElement")))

