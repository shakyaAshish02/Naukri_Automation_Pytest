import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(request,browser):
    if browser=="chrome":
        opt = Options()

        opt.add_experimental_option("debuggerAddress", "localhost:9988")
        driver=webdriver.Chrome(executable_path="C:\\Users\\ashis\\PycharmProjects\\pythonProject4\\chromedriver.exe",chrome_options=opt)
    elif browser=="edge":
        #driver=webdriver.Edge(executable_path="C:\\Users\\ashis\\Desktop\\msedgedriver.exe")
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    wait = WebDriverWait(driver, 10)
    a=ActionChains(driver)
    request.cls.a=a
    request.cls.driver=driver
    request.cls.wait =wait

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class",autouse=True)
def browser(request):
    return request.config.getoption("--browser")