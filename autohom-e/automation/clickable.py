from selenium.common.exceptions import ElementNotInteractableException, TimeoutException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click(driver, select_by, selector):
    try:
        WebDriverWait(driver, 20).until(
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
