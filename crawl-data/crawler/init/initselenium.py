import os
import platform

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from crawler.init.downloadselenium import download_driver

class InitSelenium:
    def __init__(self, total_scrolls = 5000, scroll_time = 5):
        self.old_height = 0
        self.current_scrolls = 0
        self.total_scrolls = total_scrolls
        self.scroll_time = scroll_time
        self.time_limit = 0
        self.driver = None
        self.init_selenium()

    def execute_script(self, link_user: str):
        print("InitSelenium class")
        pass

    def init_selenium(self):
        download_driver()
        options = self.get_options()
        try:
            platform_ = platform.system().lower()
            if platform_ in ['linux', 'darwin']:
                executable_path = os.path.join(os.getcwd(), 'chromedriver')
                self.driver = webdriver.Chrome(executable_path=executable_path, options=options)
            else:
                executable_path = os.path.join(os.getcwd(), "chromedriver.exe")
                self.driver = webdriver.Chrome(executable_path=executable_path, options=options)
        except Exception as e:
            print("Kindly replace the Chrome Web Driver with the latest one from "
                    "http://chromedriver.chromium.org/downloads"
                    "\nYour OS: {}".format(platform_)
                    )
            self.quit(True)
                    
    def get_options(self) -> Options:
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        # options.add_argument('user-data-dir={}'.format(self.cookie_dir))
        # options.setBinary("/path/to/other/chrome/binary")
        # options.add_argument("--headless")

        return options
    
    def quit(self, e=False):
        self.driver.close()
        if(e): exit()

    def convert_to_dict(self, obj):
        return obj.__dict__

    def wait_css(self, css_selector):
        try:
            WebDriverWait(self.driver, self.timeout_second).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        except Exception as e:
            print(e)
    
    def safe_get_element_by_css_selector(self, css_selector):
        try:
            return self.driver.find_element_by_css_selector(css_selector)
        except Exception as e:
            print(e)
    
    def safe_get_elements_by_css_selector(self, css_selector):
        try:
            return self.driver.find_elements_by_css_selector(css_selector)
        except Exception as e:
            print(e)

    def safe_get_element_by_xpath(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            print(e)
    
    def safe_get_elements_by_xpath(self, xpath):
        try:
            return self.driver.find_elements_by_xpath(xpath)
        except Exception as e:
            print(e)

    def safe_get_element_by_id(self, elem_id):
        try:
            return self.driver.find_element_by_id(elem_id)
        except NoSuchElementException:
            return None