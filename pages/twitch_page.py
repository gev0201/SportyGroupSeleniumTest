import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from pages.base_page import BasePage

load_dotenv()

class TwitchPage(BasePage):
    
    URL = os.getenv("TWITCH_URL")
    BROWSE_URL = os.getenv("TWITCH_BROWSE_URL")
    
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[data-a-target='tw-input']")
    SEARCH_RESULT_CHANNEL = (By.XPATH, "//p[contains(@class, 'CoreText-') and text()='StarCraft II']")
    
    COOKIE_BANNER = (By.CSS_SELECTOR, "[data-a-target='consent-banner']")
    COOKIE_ACCEPT_BTN = (By.CSS_SELECTOR, "button[data-a-target='consent-banner-accept']")
    MODAL_CLOSE_BTN = (By.CSS_SELECTOR, "button[aria-label='Close'], [aria-label='Dismiss']")
    MATURE_CONTENT_BTN = (By.XPATH, "//button[contains(text(), 'Start Watching')]")
    
    VIDEO_PLAYER = (By.CSS_SELECTOR, "video, [data-a-target='video-player'], .video-player")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def _after_navigate(self):
        self.handle_popups_if_present()
    
    def handle_popups_if_present(self):
        try:
            if self.is_element_present(self.COOKIE_ACCEPT_BTN):
                self.click(self.COOKIE_ACCEPT_BTN)
                self.explicitly_wait(0.5)
        except (TimeoutException, ElementClickInterceptedException):
            pass
    
    def click_on_search(self):
        self.navigate_to_url(self.BROWSE_URL)
        self.wait_for_load_page()
    
    def search_by_keyword(self, query):
        search_input = self.find_element(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)
    
    def scroll_down_by_attempts(self, attempts=1, pixels=600):
        for attempt in range(attempts):
            self.scroll_down(pixels)

    
    def select_streamer(self, index=0):
        self.explicitly_wait(1)
        streamers = self.driver.find_elements(*self.SEARCH_RESULT_CHANNEL)
        if streamers and len(streamers) > index:
            target = streamers[index]
            try:
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)
                self.explicitly_wait(0.5)
                target.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", target)
        self.explicitly_wait(0.5)
    
    def handle_modals(self):
        self.explicitly_wait(0.5)
        
        try:
            if self.is_element_present(self.MATURE_CONTENT_BTN):
                self.click(self.MATURE_CONTENT_BTN)
                self.explicitly_wait(0.5)
        except (TimeoutException, ElementClickInterceptedException):
            pass
        
        try:
            if self.is_element_present(self.MODAL_CLOSE_BTN):
                self.click(self.MODAL_CLOSE_BTN)
                self.explicitly_wait(0.5)
        except (TimeoutException, ElementClickInterceptedException):
            pass
    
    def wait_for_stream_page(self):
        self.wait_for_load_page()
        self.wait_for_element(self.VIDEO_PLAYER)
