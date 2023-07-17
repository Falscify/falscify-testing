import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://falscify.pl"


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.get(f"{base_url}/en/login.php")

        username = driver.find_element(By.XPATH,
                                       "//*[@id='email']")
        username.send_keys("galat.konstancja@gmail.com")

        password = driver.find_element(By.XPATH, "//*[@id='password']")
        password.send_keys("Kucyk123")

        login_button = driver.find_element(
            By.XPATH, '/html/body/div/div/div/form/button')
        login_button.click()

        logged_in_element = driver.find_element(By.XPATH, '//*[@id="search"]')

        self.assertTrue(logged_in_element.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
