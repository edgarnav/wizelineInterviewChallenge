from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import utilities.logger as Log


class ElementsInteractions:

    log = Log.init_logger()

    def __init__(self, web_driver):
        self.web_driver = webdriver.Chrome(ChromeDriverManager().install())

    def locator(self, locator_type):
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "xpath":
            return By.XPATH
        else:
            self.log.error("Locator not defined")

    def open_web_page(self, url):
        self.web_driver.get(url)
        self.log.info("Web page opened wuth url: " + url)

    def verify_page(self, page_name):
        if self.web_driver.title == page_name:
            self.log.info("Page expected is correct")
        else:
            self.log.error("The name of web page is not the expected")
            assert AssertionError

