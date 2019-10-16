from crawler.facebook.images.photo_all import PhotoAll
from crawler.facebook.images.photo_of import PhotoOf
from crawler.init.constants import IMAGE

class AllPhoto(PhotoAll, PhotoOf):
    def execute_script(self, link_user: str):
        self.driver.get(self.get_link_all_photos(link_user))
        elements = self.safe_get_elements_by_css_selector(IMAGE['CSS_TAB'])
        if elements is None:
            raise Exception('Error in get all photo')
        result = []
        if len(elements) == 4:
            result = result + PhotoOf.execute_script(self, link_user)
        
        result = result + PhotoAll.execute_script(self, link_user)
        from jobqueue.producer import facebook
        facebook.download_images_from_fb(result)
    
    def get_link_all_photos(self, link_user: str) -> str:
        original_link = self.create_original_link(link_user)
        link_photo_all = original_link + "/photos"
        return link_photo_all.replace("//", "/")