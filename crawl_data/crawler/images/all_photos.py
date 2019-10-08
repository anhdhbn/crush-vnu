from crawler.images.photo_all import PhotoAll
from crawler.images.photo_of import PhotoOf

class AllPhoto(PhotoAll, PhotoOf):
    def execute_script(self, link_user: str):
        PhotoOf.execute_script(self, link_user)
        PhotoAll.execute_script(self, link_user)