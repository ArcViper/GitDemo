from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass


# this imports the base class python file that allows the driver variable to be passed into any class

# its good practice to have your pytests wrapped by class
# GetDemo developer branch test

class TestOne(BaseClass):
    # test cases should not invoke the web browser. This should be in a separate fixture file to prevent duplicate code
    # having a file named "conftest.py" and putting it in there is optimal
    def test_e2e(self, setup):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("Retrieving all the card titles...")
        webProducts = checkoutPage.getProductName()
        # this creates an object from the class you can use to perform actions (ex: homePage.shopItems().click())
        i = -1
        for product in webProducts:
            i = i + 1
            productName = product.text
            log.info("selecting " + productName)
            if productName == "Blackberry":
                checkoutPage.getProductFooter()[i].click()
        # print(availableProducts)
        # you have a new object, so it has to reference itself to grab a variable in that object. the HomePage class
        # also has a variable constructor requirement created in the __init__ definition, so you have to pass driver in
        # self.driver.implicitly_wait(4)

        # if no element is found on page it will wait 5 seconds before giving up

        # def Search(country):
        # confirmPage.enter_country_name('')
        # self.driver.find_element(By.ID, "country").send_keys(country)

        # getting web elements with partial values in CSS and XPATH

        # goal is to click on shop first. It has a href link but one way to do this easy in CSS is to do a[
        # href*='shop'] the * means 'any text'. it must go before the = sign. the single quote contains a partial
        # value instead in XPATH you do //a[contains(@href, 'shop')]
        # self.driver.implicitly_wait(4)
        # this line adds the item to the cart
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

        # here you can use chain or chaining to get the div in chaining it starts from the landing location of the
        # XPATH and can continue onward. You can test just by removing /
        # for product in webProducts:
        #     productName = product.find_element(By.XPATH, "div/h4/a").text
        #     print(productName)
        #     if productName == "Blackberry":
        #         print("found")
        #         product.find_element(By.XPATH, "div/button").click()
        # print(availableProducts)
        checkoutPage.getCartBtn().click()
        log.info("Selecting checkout button to view item(s) in cart...")
        self.driver.implicitly_wait(4)
        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        # verifying web element selectors using inspect console
        # $x("") is used to verify xpath  $x("//button[@class='btn btn-success']")
        # $("")  is used for css selector  $(".button[class='btn btn-success']")

        confirmPage = checkoutPage.getCheckoutBtn()
        log.info("Selecting checkout button to view confirmation page...")
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        # going into an auto-suggest drop down

        # these commands reference the Confirm Page python file
        log.info("Entering country name...")
        confirmPage.enter_country_name('un')
        confirmPage.country_select('United States of America')
        confirmPage.agree_terms_and_conditions()
        confirmPage.purchase_click()
        confirmPage.verify_success()
        successText = confirmPage.verify_success()
        log.info("Confirmation text received from application: " + successText)
        # log.info("Text received from application is " + confirmPage.verify_success())

        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        # successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        # use partial assertion to match text. you have to use text, then "in, then variable
        # assert "Success! Thank you!" in successText
