from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Test:

    driver = webdriver.Chrome()
    url = "https://www.saucedemo.com/"

    def empty_username(self):
        self.driver.get(self.url)
        sleep(1)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(1)
        errorSection = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        result = errorSection.text == "Epic sadface: Username is required"
        print(f"Test result: {result}")
    
    def empty_password(self):
        self.driver.get(self.url)
        sleep(1)
        usernameSection = self.driver.find_element(By.ID,"user-name")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        usernameSection.send_keys("placeholder")
        loginBtn.click()
        sleep(1)
        errorSection = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        result = errorSection.text == "Epic sadface: Password is required"
        print(f"Test result: {result}")

    def locked_out_user(self):
        self.driver.get(self.url)
        sleep(1)
        usernameSection = self.driver.find_element(By.ID,"user-name")
        passwordSection = self.driver.find_element(By.ID,"password")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(1)
        usernameSection.send_keys("locked_out_user")
        passwordSection.send_keys("secret_sauce")
        loginBtn.click()
        errorSection = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        result = errorSection.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test result: {result}")
    
    def error_icon(self):
        self.driver.get(self.url)
        sleep(1)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(1)
        errorIcons = self.driver.find_elements(By.CLASS_NAME,"error_icon")
        errorBtn = self.driver.find_element(By.CLASS_NAME,"error-button")
        result1 = len(errorIcons) == 2
        errorBtn.click()
        errorIcons = self.driver.find_elements(By.CLASS_NAME,"error_icon")
        result2 = len(errorIcons) == 0

        print(f"Test result 1: {result1}\nTest result 2: {result2}")
        sleep(3)
    
    def valid_login(self):
        self.driver.get(self.url)
        sleep(1)
        usernameSection = self.driver.find_element(By.ID,"user-name")
        passwordSection = self.driver.find_element(By.ID,"password")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        usernameSection.send_keys("standard_user")
        passwordSection.send_keys("secret_sauce")
        loginBtn.click()
        sleep(1)
        result = self.driver.current_url == self.url + "inventory.html"
        print(f"Test result: {result}")
    
    def product_count(self):
        self.driver.get(self.url)
        sleep(1)
        usernameSection = self.driver.find_element(By.ID,"user-name")
        passwordSection = self.driver.find_element(By.ID,"password")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        usernameSection.send_keys("standard_user")
        passwordSection.send_keys("secret_sauce")
        loginBtn.click()
        sleep(1)
        itemList = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        result = len(itemList) == 6
        print(f"Test result: {result}")


#locked_out_user
#secret_sauce

test = Test()
test.empty_username()
test.empty_password()
test.locked_out_user()
test.error_icon()
test.valid_login()
test.product_count()