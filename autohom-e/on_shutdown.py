import time


def wait_for_chrome_shutdown(driver):
    while True:
        try:
            title = driver.title
            time.sleep(0.5)
        except Exception:
            break

    print("Shutting down...")
    driver.quit()
