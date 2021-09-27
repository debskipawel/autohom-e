from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

from chromedriver_autoinstaller.utils import download_chromedriver

from config.path_config import PATH_CONFIG


def prepare_chrome_options():
    chrome_options = Options()
    chrome_options.add_extension(PATH_CONFIG['redux'])
    chrome_options.add_argument("--start-maximized")

    return chrome_options


def initialize_driver(options: Options):
    try:
        driver = webdriver.Chrome(options=options)
    except WebDriverException:
        try:
            download_chromedriver()
            driver = webdriver.Chrome()
        except Exception:
            return None

    return driver
