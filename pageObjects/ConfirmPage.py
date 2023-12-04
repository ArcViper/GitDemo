import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities import BaseClass


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

        # you need to create an __init__ constructor in order to access the correct driver from the test case
        # from there, you need to create a class object in the actual test case

    # country = (By.ID, "country")

    # the variable passed into here should be the locator

    def country_select(self, country):
        # BaseClass.VerifyLinkPresence(country)
        wait = WebDriverWait(self.driver, 10)
        countryLink = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, country)))
        countryLink.click()

    def enter_country_name(self, country_name):
        wait = WebDriverWait(self.driver, 10)
        input_field = wait.until(ec.presence_of_element_located((By.ID, 'country')))
        input_field.send_keys(country_name)

    def agree_terms_and_conditions(self):
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

    def purchase_click(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    def verify_success(self):
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        # use partial assertion to match text. you have to use text, then "in, then variable
        assert "Success! Thank you!" in successText
        return successText
