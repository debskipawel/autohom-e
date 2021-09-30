import time

from selenium.webdriver.common.by import By

from .fillable import fill_input
from .clickable import click


def situation_page_journey(driver):
    click(driver, By.CSS_SELECTOR, ".row__radioButton:nth-child(1) > label")
    click(driver, By.ID, "field_situation_company")
    fill_input(driver, By.ID, "field_situation_company", "all")
    time.sleep(1)
    fill_input(driver, By.ID, "field_situation_company", "ianz")
    click(driver, By.LINK_TEXT, "Allianz")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .row__radioButton:nth-child(1) > label")
    click(driver, By.XPATH, '/html/body/app-root/app-home/main/div/section/div/form/app-situation-current-renewal-date/app-full-date/div/div[1]/div/div/button[1]')
    click(driver, By.XPATH, '/html/body/app-root/app-home/main/div/section/div/form/app-situation-current-renewal-date/app-full-date/div/div[1]/div/div/my-date-picker/div/div[2]/table[1]/tr/td[1]/div/div[3]/button')
    click(driver, By.XPATH, '/html/body/app-root/app-home/main/div/section/div/form/app-situation-current-renewal-date/app-full-date/div/div[1]/div/div/my-date-picker/div/div[2]/table[2]/tbody/tr[2]/td[1]/div')
    click(driver, By.CSS_SELECTOR, ".ng-star-inserted:nth-child(4) .radioListButton__checkmark")
    click(driver, By.CSS_SELECTOR, ".dropdown__itemsInner:nth-child(1) > .dropdown__item")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .ng-star-inserted:nth-child(1) .radioListButton__checkmark")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .row__radioButton:nth-child(2) > label")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .row__radioButton:nth-child(1) > label")
    click(driver, By.ID, "field_situation_cars_number")
    fill_input(driver, By.ID, "field_situation_cars_number", '0')
    click(driver, By.CSS_SELECTOR, ".row__submit")
