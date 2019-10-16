from crawler.init.init import InitSelenium

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options

import sys
import os

class CommonUtilities(InitSelenium):
    def __init__(self, email, password, total_scrolls = 5000, scroll_time = 5):
        self.email = email
        self.password = password
        self.old_height = 0
        self.current_scrolls = 0
        self.total_scrolls = total_scrolls
        self.scroll_time = scroll_time
        self.cookie_dir = os.path.join(os.getcwd(), "cookies", email)
        self.output_dir = None
        self.time_limit = 0
        self.driver = None
        self.init_selenium()
        self.timeout_second = 30

    def execute_script(self, link_user: str):
        print("CommonUtilities class")
        pass

    def login(self):
        self.driver.get("https://facebook.com")
        if "News Feed" not in self.driver.page_source: 
            try:
                self.driver.find_element_by_name('email').send_keys(self.email)
                self.driver.find_element_by_name('pass').send_keys(self.password)
                self.driver.find_element_by_id('loginbutton').click()
            except Exception as e:
                print(e)
                print("There's some error in log in.")
                print(sys.exc_info()[0])
                self.quit()
        
        mfa_code_input = self.safe_get_element_by_id('approvals_code')

        if mfa_code_input is not None:
            mfa_code_input.send_keys(input("Enter MFA code: "))
            self.driver.find_element_by_id('checkpointSubmitButton').click()

            # there are so many screens asking you to verify things. Just skip them all
            while self.safe_get_element_by_id('checkpointSubmitButton') is not None:
                dont_save_browser_radio = self.safe_get_element_by_id('u_0_3')
                if dont_save_browser_radio is not None:
                    dont_save_browser_radio.click()

                self.driver.find_element_by_id('checkpointSubmitButton').click()

        if "News Feed" not in self.driver.page_source:
            self.quit()
            return False
        else: return True


    def check_block(self):
        return "Temporarily Blocked" in self.driver.page_source

    def check_height(self):
        new_height = self.driver.execute_script("return document.body.scrollHeight")
        return new_height != self.old_height

    def scroll(self):
        self.current_scrolls = 0

        while (True):
            try:
                if self.current_scrolls == self.total_scrolls:
                    return

                self.old_height = self.driver.execute_script("return document.body.scrollHeight")
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                WebDriverWait(self.driver, self.scroll_time, 0.05).until(lambda driver: self.check_height())
                self.current_scrolls += 1
            except TimeoutException:
                break

        return

    def create_original_link(self, url):
        if url.find(".php") != -1:
            original_link = "https://.facebook.com/" + ((url.split("="))[1])

            if original_link.find("&") != -1:
                original_link = original_link.split("&")[0]

        elif url.find("fnr_t") != -1:
            original_link = "https://.facebook.com/" + ((url.split("/"))[-1].split("?")[0])
        elif url.find("_tab") != -1:
            original_link = "https://.facebook.com/" + (url.split("?")[0]).split("/")[-1]
        else:
            original_link = url

        return original_link
    
    def get_options(self) -> Options:
        options = Options()

        #  Code to disable notifications pop up of Chrome Browser
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        options.add_argument("--start-maximized")
        options.add_argument('user-data-dir={}'.format(self.cookie_dir))
        # options.setBinary("/path/to/other/chrome/binary")
        # options.add_argument("--headless")

        return options