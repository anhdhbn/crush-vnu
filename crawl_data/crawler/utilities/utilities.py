from crawler.init.init import InitSelenium

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import sys

class CommonUtilities(InitSelenium):
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

        if mfa_code_input is None:
            return

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