import requests
import crawler.facebook.crawl_all import AllFacebook

def get_filename_from_link(link):
    return (link.split('.jpg')[0]).split('/')[-1] + '.jpg'

def download_image_from_fb(image_obj):
    image_link, tagboxs = image_obj
    filename = get_filename_from_link(image_link)
    r = requests.get(url)
    # r.content

def crawl_fb_by_url(url):
    pass