from selenium import webdriver
import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
class TestLogin():    #function recalling
    @pytest.fixture(scope="class")   # one time run browser(sessio), now we using class is here(scope = class) here only wrk cls
    def test_setup(self):    # function calling to the class
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProjects/Automation/drivers/chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()


        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_login(self, test_setup):
        driver.get("http://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)  #class name
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

      #  driver.find_element_by_id("txtUsername").send_keys("Admin")
       # driver.find_element_by_id("txtPassword").send_keys("admin123")
        #driver.find_element_by_id("btnLogin").click() // deleting these codes


    def test_logout(self, test_setup):
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        #driver.find_element_by_id("welcome").click()
        #driver.find_element_by_link_text("Logout").click()   //removing these are
