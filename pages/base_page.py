from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.login_tab = (By.XPATH, "//a[contains(text(),'Login')]")
        self.email = (By.ID, "email")
        self.password = (By.ID, "password")
        self.login_btn = (By.XPATH, "//button[contains(text(),'Login')]")

    def login(self, email, password):
        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.login_tab)
        )
        self.driver.execute_script("arguments[0].click();", login_btn)
        self.wait.until(EC.visibility_of_element_located(self.email)).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        btn = self.wait.until(
            EC.element_to_be_clickable(self.login_btn)
        )
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait.until(EC.url_contains("notes"))