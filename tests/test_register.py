import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

base_url = "https://falscify.pl"


class TestRegister(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_register(self):
        driver = self.driver
        driver.get(f"{base_url}/en/register.php")
        driver.implicitly_wait(5)

        # first name
        first_name = driver.find_element(By.XPATH, "//*[@id='first_name']")
        first_name.send_keys("John")

        # second name
        second_name = driver.find_element(By.XPATH, "//*[@id='last_name']")
        second_name.send_keys("Doe")

        # country of origin
        country_dropdown = driver.find_element(
            By.XPATH, "//html/body/div/div/div/form/select[1]")
        select_country = Select(country_dropdown)
        select_country.select_by_visible_text("United States")

        # institution
        institution_dropdown = driver.find_element(
            By.XPATH, '/html/body/div/div/div/form/select[2]')
        select_institution = Select(institution_dropdown)
        select_institution.select_by_visible_text('Unassociated')

        # username
        username = driver.find_element(By.XPATH,
                                       "//*[@id='email']")
        username.send_keys("galat.konstancja@gmail.com")

        # password
        password = driver.find_element(By.XPATH,
                                       "//*[@id='password']")
        password.send_keys('admin')

        # repeat password
        repeat_password = driver.find_element(
            By.XPATH, "//*[@id='repeat_password']")
        repeat_password.send_keys('admin')

        # checkbox
        checkbox = driver.find_element(By.XPATH, "//*[@id='accept-terms']")
        checkbox.click()

        register_button = driver.find_element(
            By.XPATH, '/html/body/div/div/div/form/button')
        register_button.click()

        registered_element = driver.find_element(
            By.XPATH, '//*[@id="search"]')

        self.assertTrue(registered_element.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
