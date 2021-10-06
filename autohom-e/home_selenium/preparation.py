from selenium.webdriver.common.by import By

from .clickable import click, click_if_detected


def preparation(driver):
    click_if_detected(driver, By.XPATH, '/html/body/div/div[1]/div/div/div/span[2]', 0.5)
    click(driver, By.LINK_TEXT, "Recommencer le questionnaire")
    click_if_detected(driver, By.XPATH, '/html/body/div/div[1]/div/div/div/span[2]', 0.5)
