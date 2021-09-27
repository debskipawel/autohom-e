from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .selenium_settings import SELENIUM_SETTINGS


def fill_input(driver, select_by, selector, keys):
    WebDriverWait(driver, SELENIUM_SETTINGS['timeout_after']).until(
        EC.presence_of_element_located((select_by, selector))
    )

    element = driver.find_element(select_by, selector)

    element.send_keys(keys)
