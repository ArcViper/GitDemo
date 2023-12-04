from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        # you need to create an __init__ constructor in order to access the correct driver from the test case
        # from there, you need to create a class object in the actual test case

    productName = (By.CSS_SELECTOR, ".card-title a")
    productFooterBtn = (By.CSS_SELECTOR, ".card-footer button")
    viewCart = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutBtn = (By.XPATH, "//button[@class='btn btn-success']")

    def getProductName(self):
        return self.driver.find_elements(*CheckoutPage.productName)

    # note that there is a "*" here. It is because it needs to deserialize a 'tuple' which is a variable that stores
    # multiple values

    def getProductFooter(self):
        return self.driver.find_elements(*CheckoutPage.productFooterBtn)

    def getCartBtn(self):
        return self.driver.find_element(*CheckoutPage.viewCart)

    def getCheckoutBtn(self):
        self.driver.find_element(*CheckoutPage.checkoutBtn).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
    # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
