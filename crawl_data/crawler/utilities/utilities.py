from crawler.init.init import InitSelenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import urllib.request
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

    def parse_tagbox(self, tag):
        try:
            return tag.get_attribute("style")
        except:
            return None

    def get_download_images_url(self, img_links):
        urls = []

        for link in img_links:
            if link != "None":
                valid_url_found = False
                self.driver.get(link)

                try:
                    while not valid_url_found:
                        WebDriverWait(self.driver, self.timeout_second).until(EC.presence_of_element_located((By.CLASS_NAME, "spotlight")))
                        element = self.driver.find_element_by_class_name("spotlight")
                        img_url = element.get_attribute('src')

                        if img_url.find('.gif') == -1:
                            valid_url_found = True
                            tag_elements = self.safe_get_elements_by_css_selector(".fbPhotosPhotoTagboxBase")
                            if tag_elements is not None:
                                if len(tag_elements) > 0:
                                    tag_box = [self.parse_tagbox(tag) for tag in tag_elements]
                                    tag_box = [tag for tag in tag_box if tag is not None]
                                    urls.append((img_url, tag_box))
                except Exception as e:
                    print(e)
            else:
                print(e)

        return urls
    
    def create_folder(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

    def get_filename_from_link(self, link):
        return (link.split('.jpg')[0]).split('/')[-1] + '.jpg'

    def download_from_url(self, link, filepath, img_name):
        print("Downloading ", img_name)
        try:
            urllib.request.urlretrieve(link, filepath)
            return link, filepath, img_name
        except:
            return link, filepath, None
        

    def image_downloader(self, img_links, original_link):
        folder_name = original_link.split("/")[-1]

        img_names = []

        try:
            try:
                folder = os.path.join(os.getcwd(),"data", folder_name)
                self.create_folder(folder)
            except Exception:
                print("Error in changing directory.")

            arr_download = [(link, self.get_filename_from_link(link)) for link in img_links]
            arr_download = [(link, filename) for (link, filename) in arr_download if (filename != "10354686_10150004552801856_220367501106153455_n.jpg")]
            arr_download = [(link, os.path.join(folder, filename), filename) for link, filename in arr_download]

            img_names = [self.download_from_url(link,filepath, filename ) for (link, filepath, filename) in arr_download]
            img_names = [(link, filepath, filename) for (link, filepath, filename) in arr_download if filename is not None]
        except Exception as e:
            print("Exception (image_downloader):", e)

        return img_names
