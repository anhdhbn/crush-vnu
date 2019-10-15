import requests

def download_image_from_fb(image_obj):
    image_link, tagboxs = image_obj
    print(image_link)
    print(tagboxs)