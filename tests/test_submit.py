import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://falscify.pl"


class TestSubmit(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_submit_button(self):
        driver = self.driver
        driver.get(f"{base_url}/en/home.php")

        submit = driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/a/button')
        submit.click()

        current_url = self.driver.current_url
        is_logged_in = False  # Zmień na True, jeśli użytkownik jest zalogowany

        if all([
            is_logged_in,
            current_url == f"{base_url}/en/submit.php"
        ]):
            self.assertEqual(current_url,
                             f"{base_url}/en/submit.php")

        elif all([
            not is_logged_in,
            current_url == f"{base_url}/en/login.php"
        ]):
            self.assertEqual(current_url, f"{base_url}/en/login.php")
        else:
            self.fail()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
