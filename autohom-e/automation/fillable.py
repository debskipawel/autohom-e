from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_input(driver, select_by, selector, keys):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((select_by, selector))
    )

    element = driver.find_element(select_by, selector)

    element.send_keys(keys)
