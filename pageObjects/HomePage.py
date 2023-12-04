from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        # you need to create an __init__ constructor in order to access the correct driver from the test case
        # from there, you need to create a class object in the actual test case

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    checkBox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")
    # the variable passed into here should be the locator


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
        # you don't need to do HomePage.self.shop because it is a class variable created in the class outside another
        # definition. Since it's a class you need to pass information back out with 'return'
        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
        # you need the * because you are treating everything after the * as a tuple argument

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def clickCheckbox(self):
        self.driver.find_element(*HomePage.checkBox).click()

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    # def clickSubmit(self):
    #     self.driver.find_element(*HomePage.submitBtn).click()

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)
