import os

def take_screenshot(driver, name):
    os.makedirs("screenshots", exist_ok=True)
    file_path = f"screenshots/{name}.png"
    driver.save_screenshot(file_path)
    return file_path