import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://falscify.pl"


class TestLightMode(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_light_mode(self):
        driver = self.driver
        driver.get(f"{base_url}/en/home.php")
        driver.implicitly_wait(10)

        light_mode = driver.find_element(By.ID, 'theme-toggle-btn')
        light_mode.click()

        body_element = driver.find_element(
            By.XPATH, "//body[contains(@class, 'light-theme')]")
        is_light_theme = body_element.is_displayed()

        # Sprawdź, czy tryb (klasa) faktycznie się zmienił
        self.assertTrue(is_light_theme)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
