from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ✅ ADDED (Agentic layer)
from utils.agentic_utils import smart_wait, retry


class NotesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.add_note_btn = (By.XPATH, "//button[@data-testid='add-new-note']")
        self.title = (By.ID, "title")
        self.description = (By.ID, "description")
        self.category = (By.XPATH, "//select")

        self.save_btn = (By.XPATH, "//button[contains(text(),'Create')]")

        self.note_text = (By.XPATH, "//*[contains(text(),'Automation Note')]")

    def create_note(self, title, description, category):

        # open modal (SMART WAIT ADDED)
        add_btn = smart_wait(self.driver, self.add_note_btn)
        self.driver.execute_script("arguments[0].click();", add_btn)

        # wait modal
        self.wait.until(
            EC.visibility_of_element_located(self.title)
        )

        # fill form
        self.driver.find_element(*self.title).clear()
        self.driver.find_element(*self.title).send_keys(title)

        self.driver.find_element(*self.description).clear()
        self.driver.find_element(*self.description).send_keys(description)

        self.driver.find_element(*self.category).send_keys(category)

        # click CREATE button (SMART WAIT ADDED)
        create_btn = smart_wait(self.driver, self.save_btn)
        self.driver.execute_script("arguments[0].click();", create_btn)

        # wait until note appears
        self.wait.until(
            EC.presence_of_element_located(self.note_text)
        )

    def is_note_not_visible(self, title):
        elements = self.driver.find_elements(
            By.XPATH,
            f"//*[contains(text(),'{title}')]"
        )
        return len(elements) == 0

    def delete_note(self, title):

        # locate note dynamically
        note = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//*[contains(text(),'{title}')]/ancestor::div[1]")
            )
        )

        # click delete button
        delete_btn = note.find_element(
            By.XPATH,
            ".//button[contains(text(),'Delete')]"
        )

        self.driver.execute_script("arguments[0].click();", delete_btn)

        # confirm popup (if exists)
        try:
            confirm = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(),'Yes') or contains(text(),'OK') or contains(text(),'Delete')]")
                )
            )
            confirm.click()
        except:
            pass

        # wait until note disappears
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, f"//*[contains(text(),'{title}')]")
            )
        )