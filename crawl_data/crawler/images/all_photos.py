from crawler.images.photo_all import PhotoAll
from crawler.images.photo_of import PhotoOf

class AllPhoto(PhotoAll, PhotoOf):
    def execute_script():
        PhotoOf.execute_script(self)
        PhotoAll.execute_script(self)