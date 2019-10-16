from crawler.facebook.images.all_photos import AllPhoto
from crawler.facebook.infos.all_infos import AllInfo

class AllFacebook(AllInfo, AllPhoto):
    def execute_script(self, link_user: str):
        AllPhoto.execute_script(self, link_user)
        AllInfo.execute_script(self, link_user)