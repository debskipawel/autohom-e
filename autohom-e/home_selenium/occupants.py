from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from .fillable import fill_input
from .clickable import click


def occupants_page_journey(driver):
    click(driver, By.CSS_SELECTOR, ".ng-star-inserted:nth-child(1) .radioListButton__checkmark")
    click(driver, By.CSS_SELECTOR, ".row__radioButton:nth-child(2) > label")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .ng-star-inserted:nth-child(1) .radioListButton__checkmark")
    click(driver, By.ID, "field_occupants_move_in_year")
    element = driver.find_element(By.ID, "field_occupants_move_in_year__help")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    fill_input(driver, By.ID, "field_occupants_move_in_year", '2019')
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .ng-star-inserted:nth-child(1) .radioListButton__checkmark")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .row__radioButton:nth-child(2) > label")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .row__radioButton:nth-child(2) > label")
    click(driver, By.CSS_SELECTOR, ".dropdown__itemsInner:nth-child(4) > .dropdown__item")
    click(driver, By.ID, "field_occupants_birthdate_day")
    fill_input(driver, By.ID, "field_occupants_birthdate_day", '25')
    fill_input(driver, By.ID, "field_occupants_birthdate_month", '09')
    fill_input(driver, By.ID, "field_occupants_birthdate_year", '1999')
    click(driver, By.XPATH, '/html/body/app-root/app-home/main/div/section/div/form/app-occupants-marital-status/app-dropdown/div/div[1]/div/div/app-generic-dropdown/div/div[2]/div/perfect-scrollbar/div/div[1]/ul/li[1]')
    click(driver, By.CSS_SELECTOR, ".row__submit")
    click(driver, By.CSS_SELECTOR, ".row__submit")
