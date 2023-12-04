from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import pytest


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        # in order to use fixture you have to invite it into the test case
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("First name: " + getData["firstName"])
        homePage.getName().send_keys(getData["firstName"])
        log.info("Last name: " + getData["lastName"])
        homePage.getEmail().send_keys(getData["lastName"])
        homePage.clickCheckbox()
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.submitForm().click()

        alertText = homePage.getSuccessMessage().text
        assert ("Succcess" in alertText)
        self.driver.refresh()

    # writing a fixture here because the datasets for the homepage test cases will only have to be used here
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    # using a dictionary instead of a tuple (value, value, value) because you can name values in it
    def getData(self, request):
        return request.param
