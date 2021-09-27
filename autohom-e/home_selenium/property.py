from selenium.webdriver.common.by import By

from .fillable import fill_input
from .clickable import click


def property_page_journey(driver):
    click(driver, By.LINK_TEXT, "Recommencer le questionnaire")
    click(driver, By.CSS_SELECTOR, f".ng-star-inserted:nth-child(2) > .row__radioListButton > .radioListButton__checkmark")
    click(driver, By.ID, "field_property_address")
    fill_input(driver, By.ID, "field_property_address", "absolute_gibberish")
    click(driver, By.LINK_TEXT, "Adresse non trouvée")
    click(driver, By.ID, "field_property_address_zipcode")
    fill_input(driver, By.ID, "field_property_address_zipcode", '75001')
    click(driver, By.XPATH, '/html/body/app-root/app-home/main/div/section/div/form/app-property-address-zipcode/app-dropdown-search/div/div[1]/div/div/div/div/perfect-scrollbar/div/div[1]/ul/li')
    click(driver, By.CSS_SELECTOR, ".ng-star-inserted:nth-child(2) > .radioButtons__selection__picto > .radioListButton__label")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .ng-star-inserted:nth-child(1) .radioListButton__label")
    click(driver, By.ID, "field_property_rooms_number")
    fill_input(driver, By.ID, "field_property_rooms_number", '2')
    click(driver, By.ID, "field_property_rooms_number_extend")
    fill_input(driver, By.ID, "field_property_rooms_number_extend", '0')
    click(driver, By.ID, "field_property_surface")
    fill_input(driver, By.ID, "field_property_surface", '40')
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .ng-star-inserted:nth-child(1) .radioListButton__checkmark")
    click(driver, By.CSS_SELECTOR, ".row__radioButton:nth-child(2) > label")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .row__radioButton:nth-child(2) > label")
    click(driver, By.CSS_SELECTOR, ".row__submit")
