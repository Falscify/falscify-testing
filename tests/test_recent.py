import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://falscify.pl"


class TestRecent(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_recent(self):
        driver = self.driver
        driver.get(f"{base_url}/en/home.php")
        driver.maximize_window()
        driver.implicitly_wait(10)

        recent_btn = driver.find_element(
            By.LINK_TEXT, "Recent")
        recent_btn.click()

        expected_url = f"{base_url}/en/recent.php"
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
