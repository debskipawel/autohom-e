import sys

from selenium.common.exceptions import WebDriverException

from home_selenium.property import property_page_journey
from home_selenium.situation import situation_page_journey
from home_selenium.occupants import occupants_page_journey
from home_selenium.preparation import preparation

from on_shutdown import wait_for_chrome_shutdown
from on_launch import initialize_driver, prepare_chrome_options

from config.url_config import URL_CONFIG


def main(url_path: str):
    driver = initialize_driver(prepare_chrome_options())

    if driver is None:
        print('Driver could not be initialized. Shutting down...')
        return

    try:
        driver.get(url_path)
    except WebDriverException:
        if URL_CONFIG['local'] == url_path:
            print("Connection error: Make sure your local Hom-E runs.")
        else:
            print('Connection error: Make sure your VPN is on')
        print('Shutting down...')
        driver.quit()
        return

    preparation(driver)
    property_page_journey(driver)
    occupants_page_journey(driver)
    situation_page_journey(driver)

    wait_for_chrome_shutdown(driver)


if __name__ == '__main__':
    dict_keys = list(URL_CONFIG.keys())

    url_key = str(sys.argv[1]) if len(sys.argv) > 1 else dict_keys[0]
    url_key = url_key if url_key in dict_keys else dict_keys[0]
    url = URL_CONFIG[url_key]

    try:
        main(url)
    except Exception:
        print('Unhandled error occured :C')
