from celery import Celery
from upscale.upscale import upscale

celery_app = Celery(
    "app", backend="redis://localhost:6379/1", broker="redis://localhost:6379/2"
)

@celery_app.task()
def upscale_image(path_1, path_2):
    result = upscale(path_1, path_2)
    return result
