from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class InitWebDriver:

    @staticmethod
    def init_web_driver():
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        return web_driver
