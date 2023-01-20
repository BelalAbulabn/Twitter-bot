import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Twitter home page
driver.get("https://twitter.com")

# Check if the user is already logged in
try:
    profile_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='UserProfileHeader_Items']"))
    )
    print("User is already logged in.")
except:
    # Navigate to the Twitter login page
    driver.get("https://twitter.com/login")
    try:
        #find login form
        login_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form[data-testid='LoginForm_Login_Form']"))
        )
        #klick on login form
        login_form.click()
        #find username field
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='session[username_or_email]']"))
        )
        #enter username
        username_field.send_keys("username")
        #find password field
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='session[password]']")))

    driver.quit()
    # # Find the username and password fields and enter the login credentials
    # username = driver.find_element_by_name("session[username_or_email]")
    # username.send_keys("at23kuzfuzf5470@gmail.com")
    # password = driver.find_element_by_name("session[password]")
    # password.send_keys("ijijij!")
    #
    # # Find the login button and click it
    # login_button = driver.find_element_by_css_selector("div[data-testid='LoginForm_Login_Button']")
    # login_button.click()
    # print("User has been logged in.")

# Close the browser

