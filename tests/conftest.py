import pytest
from selenium import webdriver

driver = None


# use conftest when you think you will have to use data or fixtures across multiple test cases

# example of how to do is docs.pytest.org/en/latest/example.simple.html
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="this tells what browser to run tests on"
    )  # --browser_name is the keyword variable to use in cmd, if you don't evoke an additional word default is used
    # when you do pass in a value in cmd, the method has to be able to retrieve that value


@pytest.fixture(scope="class")
# have to set the scope to class level, so it only executes once instead of each test case
# need to set up a way to invoke whatever browser you want to run test cases on via command line
def setup(request):
    global driver
    # need to create a global driver so that the screenshot function later on can reference driver correctly
    browser_name = request.config.getoption("browser_name")
    # this line will grab the option for browser type that is passed in via cmd
    match browser_name:
        case "chrome":
            from selenium import webdriver
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("detach", True)

            driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
        case "firefox":
            from selenium import webdriver
            from selenium.webdriver.firefox.service import Service
            from webdriver_manager.firefox import GeckoDriverManager
            driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
        case "edge":
            from selenium import webdriver
            from selenium.webdriver.edge.options import Options
            from selenium.webdriver.edge.service import Service as EdgeService
            from webdriver_manager.microsoft import EdgeChromiumDriverManager
            options = Options()
            options.add_experimental_option("detach", True)
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    # during teardown after tests you have to be able to close the browser
    request.cls.driver = driver
    # this code will send driver to the class. CLS allows you to return a variable without closing the code
    # CLS assigns local variable to a class variable
    yield
    # yield will wait until all test cases are done before executing the rest of the code
    # driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
