import sys
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from automation.fillable import fill_input
from automation.clickable import click
from config.urls import URL_CONFIG


def main(url_path: str):
    try:
        driver = webdriver.Chrome()
    except Exception:
        print('chromedriver.exe is not present in the main project directory or is incompatible with your browser.')
        return

    driver.get(url_path)
    driver.set_window_size(1600, 900)

    # Property page
    click(driver, By.LINK_TEXT, "Recommencer le questionnaire")
    click(driver, By.CSS_SELECTOR, ".ng-star-inserted:nth-child(2) > .row__radioListButton > .radioListButton__checkmark")
    click(driver, By.ID, "field_property_address")
    fill_input(driver, By.ID, "field_property_address", "asdasdadasd")
    click(driver, By.LINK_TEXT, "Adresse non trouvée")
    click(driver, By.ID, "field_property_address_zipcode")
    fill_input(driver, By.ID, "field_property_address_zipcode", "75001")
    click(driver, By.LINK_TEXT, "75001 Paris")
    click(driver, By.CSS_SELECTOR, ".ng-star-inserted:nth-child(2) > .radioButtons__selection__picto > .radioListButton__label")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .ng-star-inserted:nth-child(1) .radioListButton__label")
    click(driver, By.ID, "field_property_rooms_number")
    fill_input(driver, By.ID, "field_property_rooms_number", "2")
    click(driver, By.ID, "field_property_rooms_number_extend")
    fill_input(driver, By.ID, "field_property_rooms_number_extend", "0")
    click(driver, By.ID, "field_property_surface")
    fill_input(driver, By.ID, "field_property_surface", "40")
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
    fill_input(driver, By.ID, "field_occupants_move_in_year", "2019")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .ng-star-inserted:nth-child(1) .radioListButton__checkmark")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .row__radioButton:nth-child(2) > label")
    click(driver, By.CSS_SELECTOR, ".ng-untouched > .row__radioButton:nth-child(2) > label")
    click(driver, By.CSS_SELECTOR, ".dropdown__itemsInner:nth-child(4) > .dropdown__item")
    click(driver, By.ID, "field_occupants_birthdate_day")
    fill_input(driver, By.ID, "field_occupants_birthdate_day", "25")
    fill_input(driver, By.ID, "field_occupants_birthdate_month", "09")
    fill_input(driver, By.ID, "field_occupants_birthdate_year", "1999")
    click(driver, By.CSS_SELECTOR, ".ps--active-y .dropdown__itemsInner:nth-child(1) > .dropdown__item")
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
    fill_input(driver, By.ID, "field_situation_cars_number", "0")
    click(driver, By.CSS_SELECTOR, ".row__submit")

    while True:
        try:
            title = driver.title
            time.sleep(0.5)
        except Exception:
            break

    print("Shutting down.")
    driver.quit()


if __name__ == '__main__':
    url_key = str(sys.argv[1])
    url = URL_CONFIG[url_key]

    main(url)
