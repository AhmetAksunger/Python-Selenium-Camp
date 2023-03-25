from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
from pathlib import Path
from datetime import date

class Test_Sauce:
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = "https://www.saucedemo.com/"

    # her testten önce çağırılır
    def setup_method(self):
        self.driver.delete_all_cookies()
        self.driver.get(self.url)
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
 
    def wait_until(self,locator: tuple):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(locator))

    #testing the case where the username and password is empty
    #and also the case where the username is empty but the password is not

    @pytest.mark.parametrize("password",[(""),("test_password")])
    def test_empty_username(self,password):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordSection = self.driver.find_element(By.ID,"password")
        passwordSection.send_keys(password)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        #waiting for the error to pop out
        self.wait_until((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3"))
        errorSection = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_username_test_{password}.png")
        assert errorSection.text == "Epic sadface: Username is required"
    
    @pytest.mark.parametrize("username",[("test_username"),("test_username2")])
    def test_empty_password(self,username):

        self.wait_until((By.ID,"login-button"))
        usernameSection = self.driver.find_element(By.ID,"user-name")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        usernameSection.send_keys(username)
        loginBtn.click()
        #waiting for the error to pop out
        self.wait_until((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3"))
        errorSection = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_password_test_{username}.png")
        assert errorSection.text == "Epic sadface: Password is required"

    def test_locked_out_user(self):
                
        self.wait_until((By.ID,"login-button"))
        usernameSection = self.driver.find_element(By.ID,"user-name")
        passwordSection = self.driver.find_element(By.ID,"password")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        usernameSection.send_keys("locked_out_user")
        passwordSection.send_keys("secret_sauce")
        loginBtn.click()
        self.wait_until((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3"))
        errorSection = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_locked_out_user_test.png")
        assert errorSection.text == "Epic sadface: Sorry, this user has been locked out."

    @pytest.mark.parametrize("username,password",[("username1","password1"),("testUser","testPassword"),("kJDsWQ","sdWrq")])
    def test_error_icon(self,username,password):
        self.wait_until((By.ID,"login-button"))
        usernameSection = self.driver.find_element(By.ID,"user-name")
        passwordSection = self.driver.find_element(By.ID,"password")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        usernameSection.send_keys(username)
        passwordSection.send_keys(password)
        loginBtn.click()

        self.wait_until((By.CLASS_NAME,"error_icon"))
        errorIcons = self.driver.find_elements(By.CLASS_NAME,"error_icon")
        self.wait_until((By.CLASS_NAME,"error-button"))
        errorBtn = self.driver.find_element(By.CLASS_NAME,"error-button")
        self.driver.save_screenshot(f"{self.folderPath}/test_error_icons_test_{username,password}.png")
        assert len(errorIcons) == 2
        errorBtn.click()
        errorIcons = self.driver.find_elements(By.CLASS_NAME,"error_icon")
        self.driver.save_screenshot(f"{self.folderPath}/test_error_icons_after_click_test_{username,password}.png")

        assert len(errorIcons) == 0

    def test_valid_login(self):
            self.wait_until((By.ID,"login-button"))
            usernameSection = self.driver.find_element(By.ID,"user-name")
            passwordSection = self.driver.find_element(By.ID,"password")
            loginBtn = self.driver.find_element(By.ID,"login-button")
            usernameSection.send_keys("standard_user")
            passwordSection.send_keys("secret_sauce")
            loginBtn.click()
            WebDriverWait(self.driver,5).until(ec.url_changes(self.url))
            self.driver.save_screenshot(f"{self.folderPath}/test_valid_login.png")
            assert self.driver.current_url == f"{self.url}inventory.html"

    def login(self):
        self.wait_until((By.ID,"login-button"))
        usernameSection = self.driver.find_element(By.ID,"user-name")
        passwordSection = self.driver.find_element(By.ID,"password")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        usernameSection.send_keys("standard_user")
        passwordSection.send_keys("secret_sauce")
        loginBtn.click()
        WebDriverWait(self.driver,5).until(ec.url_changes(self.url))

    def test_product_count(self):
        self.login()
        self.wait_until((By.CLASS_NAME,"inventory_item"))
        itemList = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test_product_count.png") 
        assert len(itemList) == 6

    @pytest.mark.parametrize("n_items",[(2),(6),(5),(3)])
    def test_add_to_cart(self,n_items):
        self.login()
        self.wait_until((By.CLASS_NAME,"btn_inventory"))
        buttons = self.driver.find_elements(By.CLASS_NAME,"btn_inventory")
        for button in buttons[:n_items]:
            button.click()
        self.wait_until((By.CLASS_NAME,"shopping_cart_badge"))
        shopping_cart = self.driver.find_element(By.CLASS_NAME,"shopping_cart_badge")

        self.driver.save_screenshot(f"{self.folderPath}/test_add_to_cart{n_items}.png") 

        assert shopping_cart.text == str(n_items) #checking if the text on the shopping cart symbole has changed

        buttons = self.driver.find_elements(By.CLASS_NAME,"btn_inventory")

        for button in buttons[:n_items]: #removing items back
            button.click()

    @pytest.mark.parametrize("n_items",[(2),(6)])
    def test_shopping_cart(self,n_items):
        self.login()
        self.wait_until((By.CLASS_NAME,"btn_inventory"))
        buttons = self.driver.find_elements(By.CLASS_NAME,"btn_inventory")
        for button in buttons[:n_items]:
            button.click()
        self.wait_until((By.CLASS_NAME,"shopping_cart_link"))
        shopping_cart_btn = self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")

        shopping_cart_btn.click()

        WebDriverWait(self.driver,5).until(ec.url_to_be(f"{self.url}cart.html"))

        self.wait_until((By.CLASS_NAME,"cart_item"))

        cart_items = self.driver.find_elements(By.CLASS_NAME,"cart_item")

        self.driver.save_screenshot(f"{self.folderPath}/test_shopping_cart_count{n_items}.png") 

        assert len(cart_items) == n_items #checking if there actually is 6 items in our shopping cart

        cart_remove_buttons = self.driver.find_elements(By.CLASS_NAME,"cart_button")

        for button in cart_remove_buttons:
            button.click()

        cart_items = self.driver.find_elements(By.CLASS_NAME,"cart_item")

        self.driver.save_screenshot(f"{self.folderPath}/test_shopping_cart_count_after_click{n_items}.png") 

        assert len(cart_items) == 0 #checking the count of item after removing each one of them

    def test_total_amount(self):
        self.login()
        
        self.wait_until((By.CLASS_NAME,"inventory_item_price"))
        itemPrices = self.driver.find_elements(By.CLASS_NAME,"inventory_item_price")

        priceList = []

        for item in itemPrices:
            price = item.text.split("$")[1]
            priceList.append(price)
        
        self.wait_until((By.CLASS_NAME,"btn_inventory"))
        buttons = self.driver.find_elements(By.CLASS_NAME,"btn_inventory")
        for button in buttons:
            button.click()
        
        shopping_cart_btn = self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")

        shopping_cart_btn.click()
        WebDriverWait(self.driver,5).until(ec.url_to_be(f"{self.url}cart.html"))

        self.wait_until((By.CLASS_NAME,"checkout_button"))

        checkout_button = self.driver.find_element(By.CLASS_NAME,"checkout_button")

        checkout_button.click()

        WebDriverWait(self.driver,5).until(ec.url_to_be(f"{self.url}checkout-step-one.html"))

        self.wait_until((By.ID,"first-name"))
        firstNameSection = self.driver.find_element(By.ID,"first-name")
        lastNameSection = self.driver.find_element(By.ID,"last-name")
        postalCodeSection = self.driver.find_element(By.ID,"postal-code")
        continueBtn = self.driver.find_element(By.CLASS_NAME,"submit-button")

        firstNameSection.send_keys("randomName")
        lastNameSection.send_keys("randomLastName")
        postalCodeSection.send_keys("21000")
        continueBtn.click()
        
        WebDriverWait(self.driver,5).until(ec.url_to_be(f"{self.url}checkout-step-two.html"))

        self.wait_until((By.CLASS_NAME,"summary_total_label"))
        totalAmountLabel = self.driver.find_element(By.CLASS_NAME,"summary_total_label")

        price = float(totalAmountLabel.text.split("$")[1])

        self.driver.save_screenshot(f"{self.folderPath}/test_total_amount.png") 

        assert price == 140.34