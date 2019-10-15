from jobqueue import tasks

def download_images_from_fb(images_obj):
    [tasks.download_image_from_fb.delay(image_obj) for image_obj in images_obj]

tasks.download_image_from_fb.delay(("asdasda", []))