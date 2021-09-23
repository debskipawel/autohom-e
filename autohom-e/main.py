import sys
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from chromedriver_autoinstaller.utils import download_chromedriver

from automation.fillable import fill_input
from automation.clickable import click
from config.urls import URL_CONFIG
from config.form_config import FORM_CONFIG


def initialize_driver():
    try:
        driver = webdriver.Chrome()
    except WebDriverException:
        try:
            download_chromedriver()
            driver = webdriver.Chrome()
        except Exception:
            return None

    return driver


def main(url_path: str):
    driver = initialize_driver()

    if driver is None:
        print('Driver could not be initialized. Shutting down...')
        return

    try:
        driver.get(url_path)
    except WebDriverException:
        if URL_CONFIG['local'] == url_path:
            print("Connection error: Make sure your local Hom-E runs.")
        else:
            print('Connection error. Make sure your VPN is on')
        print('Shutting down...')
        driver.quit()
        return

    driver.set_window_size(1600, 900)

    # Property page
    click(driver, By.LINK_TEXT, "Recommencer le questionnaire")
    click(driver, By.CSS_SELECTOR, f".ng-star-inserted:nth-child(2) > .row__radioListButton > .radioListButton__checkmark")
    click(driver, By.ID, "field_property_address")
    fill_input(driver, By.ID, "field_property_address", "absolute_gibberish")
    click(driver, By.LINK_TEXT, "Adresse non trouvée")
    click(driver, By.ID, "field_property_address_zipcode")
    fill_input(driver, By.ID, "field_property_address_zipcode", FORM_CONFIG['postcode'])
    click(driver, By.XPATH, '/html/body/app-root/app-home/main/div/section/div/form/app-property-address-zipcode/app-dropdown-search/div/div[1]/div/div/div/div/perfect-scrollbar/div/div[1]/ul/li')
    click(driver, By.CSS_SELECTOR, ".ng-star-inserted:nth-child(2) > .radioButtons__selection__picto > .radioListButton__label")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .ng-star-inserted:nth-child(1) .radioListButton__label")
    click(driver, By.ID, "field_property_rooms_number")
    fill_input(driver, By.ID, "field_property_rooms_number", f'{ FORM_CONFIG["rooms_number"] }')
    click(driver, By.ID, "field_property_rooms_number_extend")
    fill_input(driver, By.ID, "field_property_rooms_number_extend", f'{ FORM_CONFIG["large_rooms_number"] }')
    click(driver, By.ID, "field_property_surface")
    fill_input(driver, By.ID, "field_property_surface", f'{ FORM_CONFIG["property_size"] }')
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .ng-star-inserted:nth-child(1) .radioListButton__checkmark")
    click(driver, By.CSS_SELECTOR, ".row__radioButton:nth-child(2) > label")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .row__radioButton:nth-child(2) > label")
    click(driver, By.CSS_SELECTOR, ".row__submit")

    # Occupants Page
    click(driver, By.CSS_SELECTOR, ".ng-star-inserted:nth-child(1) .radioListButton__checkmark")
    click(driver, By.CSS_SELECTOR, ".row__radioButton:nth-child(2) > label")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .ng-star-inserted:nth-child(1) .radioListButton__checkmark")
    click(driver, By.ID, "field_occupants_move_in_year")
    element = driver.find_element(By.ID, "field_occupants_move_in_year__help")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    fill_input(driver, By.ID, "field_occupants_move_in_year", FORM_CONFIG['move_in_year'])
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .ng-star-inserted:nth-child(1) .radioListButton__checkmark")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .row__radioButton:nth-child(2) > label")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .row__radioButton:nth-child(2) > label")
    click(driver, By.CSS_SELECTOR, ".dropdown__itemsInner:nth-child(4) > .dropdown__item")
    click(driver, By.ID, "field_occupants_birthdate_day")
    fill_input(driver, By.ID, "field_occupants_birthdate_day", FORM_CONFIG['birth_date_day'])
    fill_input(driver, By.ID, "field_occupants_birthdate_month", FORM_CONFIG['birth_date_month'])
    fill_input(driver, By.ID, "field_occupants_birthdate_year", FORM_CONFIG['birth_date_year'])
    click(driver, By.XPATH, '/html/body/app-root/app-home/main/div/section/div/form/app-occupants-marital-status/app-dropdown/div/div[1]/div/div/app-generic-dropdown/div/div[2]/div/perfect-scrollbar/div/div[1]/ul/li[1]')
    click(driver, By.CSS_SELECTOR, ".row__submit")
    click(driver, By.CSS_SELECTOR, ".row__submit")

    # Situation page
    click(driver, By.CSS_SELECTOR, ".row__radioButton:nth-child(1) > label")
    click(driver, By.ID, "field_situation_company")
    fill_input(driver, By.ID, "field_situation_company", "allianz")
    click(driver, By.LINK_TEXT, "Allianz")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .row__radioButton:nth-child(1) > label")
    click(driver, By.CSS_SELECTOR, ".icon-calendar")
    click(driver, By.XPATH, '/html/body/app-root/app-home/main/div/section/div/form/app-situation-current-renewal-date/app-full-date/div/div[1]/div/div/my-date-picker/div/div[2]/table[1]/tr/td[1]/div/div[3]/button')
    click(driver, By.XPATH, '/html/body/app-root/app-home/main/div/section/div/form/app-situation-current-renewal-date/app-full-date/div/div[1]/div/div/my-date-picker/div/div[2]/table[2]/tbody/tr[2]/td[1]/div')
    click(driver, By.CSS_SELECTOR, ".ng-star-inserted:nth-child(4) .radioListButton__checkmark")
    click(driver, By.CSS_SELECTOR, ".dropdown__itemsInner:nth-child(1) > .dropdown__item")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .ng-star-inserted:nth-child(1) .radioListButton__checkmark")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .row__radioButton:nth-child(2) > label")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .row__radioButton:nth-child(2) > label")
    click(driver, By.ID, "field_situation_cars_number")
    fill_input(driver, By.ID, "field_situation_cars_number", f'{ FORM_CONFIG["cars_number"] }')
    click(driver, By.CSS_SELECTOR, ".row__submit")

    while True:
        try:
            title = driver.title
            time.sleep(0.5)
        except Exception:
            break

    print("Shutting down...")
    driver.quit()


if __name__ == '__main__':
    url_key = str(sys.argv[1]) if len(sys.argv) > 1 else URL_CONFIG.keys()[0]
    url_key = url_key if url_key in URL_CONFIG.keys() else URL_CONFIG.keys()[0]
    url = URL_CONFIG[url_key]

    main(url)
