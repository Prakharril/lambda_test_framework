from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertsPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.wait = WebDriverWait(driver, 10)

    def handle_js_alert(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        self.wait.until(EC.alert_is_present()).accept()

    def handle_js_confirm_accept(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        self.wait.until(EC.alert_is_present()).accept()

    def handle_js_confirm_dismiss(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        self.wait.until(EC.alert_is_present()).dismiss()

    def handle_js_prompt(self, text):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys(text)
        alert.accept()
