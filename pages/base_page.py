import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def navigate_to_url(self, url=None):
        target_url = url or getattr(self, 'URL', None)
        if not target_url:
            raise ValueError("No URL provided for navigation")
        self.driver.get(target_url)
        self.wait_for_load_page()
        self._after_navigate()

    def _after_navigate(self):
        pass
    
    def find_element(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))
    
    def find_clickable_element(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))
    
    def click(self, locator):
        element = self.find_clickable_element(locator)
        element.click()
    
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def scroll_down(self, pixels=500):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
    
    def take_screenshot(self, filename="screenshot.png"):
        screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        filepath = os.path.join(screenshots_dir, filename)
        self.driver.save_screenshot(filepath)
        return filepath
    
    def is_element_present(self, locator, timeout=1):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def wait_for_element(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(locator)
        )
    
    def wait_for_load_page(self, timeout=3):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    @staticmethod
    def explicitly_wait(seconds=1):
        time.sleep(seconds)
