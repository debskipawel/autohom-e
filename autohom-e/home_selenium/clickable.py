from selenium.common.exceptions import ElementNotInteractableException, TimeoutException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .selenium_settings import SELENIUM_SETTINGS


def click(driver, select_by, selector):
    try:
        WebDriverWait(driver, SELENIUM_SETTINGS['timeout_after']).until(
            EC.presence_of_element_located((select_by, selector))
        )
    except TimeoutException:
        print("Waiting for a component has timed out. It's possible the layout may have changed")
        driver.quit()
        exit(-1)

    element = driver.find_element(select_by, selector)

    try:
        element.click()
    except ElementNotInteractableException:
        driver.execute_script('arguments[0].click();', element)


def click_if_detected(driver, select_by, selector, timeout):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((select_by, selector))
        )
    except Exception:
        pass

    element = driver.find_element(select_by, selector)

    try:
        element.click()
    except ElementNotInteractableException:
        driver.execute_script('arguments[0].click();', element)
