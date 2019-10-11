import os
import platform
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from crawler.init.download import download_driver
from crawler.init.constants import *

class InitSelenium:
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

        #  Code to disable notifications pop up of Chrome Browser
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        options.add_argument("--start-maximized")
        options.add_argument('user-data-dir={}'.format(self.cookie_dir))
        # options.setBinary("/path/to/other/chrome/binary")
        # options.add_argument("headless")

        return options
    
    def quit(self, e=False):
        self.driver.close()
        if(e): exit()

    def convert_to_dict(self, obj):
        return obj.__dict__


if __name__ == "__main__":
    test = InitSelenium("test", "test")
    test.execute_script()
    test.quit()