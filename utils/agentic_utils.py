import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. SELF-HEALING LOCATOR
def find_element_with_fallback(driver, locators):
    for by, value in locators:
        try:
            return driver.find_element(by, value)
        except NoSuchElementException:
            continue
    raise Exception("Element not found using any locator")

# 2. AUTO RETRY MECHANISM
def retry(action, attempts=3, delay=2):
    last_error = None
    for i in range(attempts):
        try:
            return action()
        except Exception as e:
            last_error = e
            time.sleep(delay)
    raise Exception(f"Action failed after {attempts} attempts. Last error: {last_error}")

# 3. INTELLIGENT WAIT SYSTEM
def smart_wait(driver, locator, timeout=20):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

# 4. PERFORMANCE TIMER
def measure_time(action):
    start = time.time()
    result = action()
    end = time.time()
    print(f"[PERFORMANCE] Execution Time: {end - start:.2f} seconds")
    return result