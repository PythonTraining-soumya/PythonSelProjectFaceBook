# for invoking any browser in cmd give the command py.test --browser_name firefox/IE/chrome
# in order to pass command line options go through the website below
# https://docs.pytest.org/en/latest/example/simple.html#package-directory-level-fixtures-setups


import pytest
from selenium import webdriver


def pytest_addoption(parser):  # this is how we pass the command line hook
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def test_driverInitialization(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                                  "folder\\chromedriver_win32\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                                   "folder\\geckodriver-v0.26.0-win64\\geckodriver.exe")
    elif browser_name == "IE":
        driver = webdriver.Ie(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                              "folder\\IEDriverServer_x64_3.150.1\\IEDriverServer.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver  # here we are assigning the local driver to the class(cls)driver
    yield
    driver.close()
