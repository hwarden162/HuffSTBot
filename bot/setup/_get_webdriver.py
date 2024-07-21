from logging import Logger
from selenium.webdriver import Chrome, Edge, Firefox, Safari
from selenium.webdriver.remote.webdriver import WebDriver

def get_webdriver(logger: Logger, browser: str) -> WebDriver:
    assert isinstance(logger, Logger), "logger should be an instance of Logger"
    assert isinstance(browser, str), "browser should be a string"
    assert browser in ["chrome", "edge", "firefox", "opera"], "browser should be one of chrome, edge, firefox or safari"
    if browser == "chrome":
        driver = Chrome()
    elif browser == "edge":
        driver = Edge()
    elif browser == "firefox":
        driver = Firefox()
    elif browser == "safari":
        driver = Safari()
    else:
        raise ValueError("browser is not one of the accepted values of chrome, edge, firefox or safari")
    logger.info("Connected to the internet")
    return driver
