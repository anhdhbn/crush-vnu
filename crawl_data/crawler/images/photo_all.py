from crawler.utilities.utilities import CommonUtilities
from crawler.init.constants import IMAGE
import sys

class PhotoAll(CommonUtilities):
    def execute_script(self, link_user: str):
        self.driver.get(self.get_link_photos_all(link_user))
        self.scroll()
        elements = self.safe_get_elements_by_xpath(IMAGE['XPATH_EACH_IMAGE'])
        images = self.get_link_images(elements)
        link_images = self.get_download_images_url(images)
        link_images = [link for link in link_images if link != "None"]
        self.image_downloader(link_images, self.create_original_link(link_user))
        

    def get_link_photos_all(self, link_user: str) -> str:
        original_link = self.create_original_link(link_user)
        link_photo_all = original_link + "/photos_all"
        return link_photo_all.replace("//", "/")

    def get_link_images(self, elements):
        try:
            return [x.get_attribute('href') for x in elements]
        except:
            print("Exception (Images)", sys.exc_info()[0])
        return None