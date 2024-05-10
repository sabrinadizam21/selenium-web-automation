import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Pages.sidebar import Sidebar
from Pages.loginPage import LoginPage

class LoginFailed(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_invalid_username(self):
        driver = self.driver
        driver.get('https://katalon-demo-cura.herokuapp.com/')
        
        sidebar = Sidebar(driver)
        sidebar.click_menu()
        sidebar.click_login()

        loginPage = LoginPage(driver)
        loginPage.enter_username('userTest')
        loginPage.enter_password('ThisIsNotAPassword')
        loginPage.submit_login()
        time.sleep(1)

        # Validation
        self.driver.find_element(By.XPATH, loginPage.err_message_xpath).is_displayed()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
