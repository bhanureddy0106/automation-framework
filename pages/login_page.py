from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.login_tab = (By.XPATH, "//a[contains(text(),'Login')]")
        self.email = (By.ID, "email")
        self.password = (By.ID, "password")
        self.login_btn = (By.XPATH, "//button[contains(text(),'Login')]")

    def open_login_page(self):
        self.driver.get("https://practice.expandtesting.com/notes/app")

    def login(self, email, password):

        # ✅ wait page load
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # ✅ scroll to avoid overlay issue
        login_tab = self.wait.until(EC.element_to_be_clickable(self.login_tab))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", login_tab)

        # ✅ JS click (fix intercept issue)
        self.driver.execute_script("arguments[0].click();", login_tab)

        # enter email
        self.wait.until(EC.visibility_of_element_located(self.email)).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)

        # ✅ scroll + JS click login
        login_btn = self.wait.until(EC.element_to_be_clickable(self.login_btn))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", login_btn)
        self.driver.execute_script("arguments[0].click();", login_btn)

        # ✅ wait success
        self.wait.until(EC.url_contains("notes"))